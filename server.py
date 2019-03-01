"""Sound server used to sync sounds between players"""
import datetime
import hashlib
import os
import signal
import socket
from threading import Lock, Thread

from packets_pb2 import PacketInfo, GameEvent, SoundRequest, SoundResponse, ClientUpdate, PlaySound
from config import SOUND_SERVER_PORT

rare_events = [ GameEvent.Type.MVP, GameEvent.Type.SUICIDE, GameEvent.Type.TEAMKILL, GameEvent.Type.KNIFE, GameEvent.Type.COLLATERAL ]
shared_events = [ GameEvent.Type.ROUND_WIN, GameEvent.Type.ROUND_LOSE, GameEvent.Type.ROUND_START, GameEvent.Type.TIMEOUT ]

CLIENT_TIMEOUT = 120
MAX_CLIENTS = 100

# Thread-safe printing
print_lock = Lock()
unsafe_print = print
def print(*a, **b):
	with print_lock:
		unsafe_print(*a, **b)

def small_hash(hash):
	hex = hash.hex()
	return '%s-%s' % (hex[0:4], hex[-4:])

class Shard:
	def __init__(self, name):
		self.name = name
		self.clients = []
		self.lock = Lock()
		self.round = 0
		self.round_events = []
	
	def play(self, steamid, hash):
		packet = PlaySound()
		packet.steamid = steamid
		packet.hash = hash
		raw_packet = packet.SerializeToString()

		header = PacketInfo()
		header.type = PacketInfo.Type.PLAY_SOUND
		header.length = len(raw_packet)
		raw_header = header.SerializeToString()

		print('[%s] %d : %s (%d clients)' % (self.name, steamid, small_hash(hash), len(self.clients)))

		with self.lock:
			for client in self.clients:
				if client.ingame:
					with client.lock:
						client.sock.send(raw_header)
						client.sock.send(raw_packet)

					if client.round > self.round or round < self.round - 1:
						self.round = client.round
						self.round_events = []
	
	def play_shared(self, event, hash):
		should_play = False
		with self.lock:
			if event not in self.round_events:
				self.round_events.append(event)
				should_play = True
		if should_play:
			self.play(b'', hash)


class Client:
	def __init__(self, server, sock, addr):
		self.server = server
		self.lock = Lock()
		self.sock = sock
		self.addr = addr
		self.steamid = 0
		self.shard = None
		self.map = ''
		self.round = 0
		self.ingame = False
		
		self.sock.settimeout(CLIENT_TIMEOUT)
	
	def check_or_request_sound(self, hash):
		"""Request sound if we don't have it in cache"""
		request_sound = False
		with self.server.cache_lock:
			if hash not in self.server.cache:
				request_sound = True
		if request_sound:
			sound_request = SoundRequest()
			sound_request.sound_hash.add(hash)
			raw_request = sound_request.SerializeToString()

			header = PacketInfo()
			header.type = PacketInfo.Type.SOUND_REQUEST
			header.length = len(raw_request)

			with self.lock:
				print('Requesting %s from %d' % (small_hash(hash), self.steamid))
				self.sock.send(header.SerializeToString())
				self.sock.send(raw_request)

	def get_event_class(self, packet):
		if packet.update in rare_events: return 'rare'
		if packet.update in shared_events: return 'shared'
		if packet.update == GameEvent.Type.KILL and packet.kill_count > 3: return 'rare'
		return 'normal'

	def handle_event(self, packet):
		with self.lock:
			self.round = packet.round
			if self.shard == None:
				return

		event_class = self.get_event_class(packet)
		self.check_or_request_sound(packet.proposed_sound_hash)

		if event_class == 'shared':
			self.shard.play_shared(packet.update, packet.proposed_sound_hash)
		else:
			self.shard.play(self.steamid if event_class == 'normal' else b'', packet.proposed_sound_hash)
	
	def send_sound(self, packet):
		with self.server.cache_lock:
			if not packet.sound_hash in self.server.cache:
				return
		
		with os.open('cache/' + packet.sound_hash) as infile:
			data = infile.read()

		res = SoundResponse()
		res.data = data
		res.hash = packet.sound_hash
		raw_res = res.SerializeToString()

		header = PacketInfo()
		header.type = PacketInfo.Type.SOUND_RESPONSE
		header.length = len(raw_res)

		with self.lock:
			print('Sending %s to %d' % (small_hash(packet.sound_hash), self.steamid))
			self.sock.send(header.SerializeToString())
			self.sock.send(raw_res)
	
	def save_sound(self, packet):
		verif = hashlib.blake2b()
		verif.update(packet.data)
		if packet.hash != verif.digest():
			print("Hashes do not match, dropping file.")
			return

		with self.server.cache_lock:
			if packet.hash in self.server.cache:
				# Sound already saved
				return
		with os.open('cache/' + packet.hash) as outfile:
			outfile.write(packet.data)
		with self.server.cache_lock:
			self.server.cache.append(packet.hash)
		with self.lock:
			print('Saved %s from %d' % (small_hash(packet.hash), self.steamid))
		
	def update(self, packet):
		with self.lock:
			self.ingame = packet.status == ClientUpdate.PlayerStatus.CONNECTED
			self.map = packet.map
			self.steamid = packet.steamid

			# Update shard
			if self.shard.name != packet.shard_code:
				old_shard = self.server.get_shard(self.shard.name)
				with old_shard.lock:
					old_shard.clients.remove(self)

				new_shard = self.server.get_shard(packet.shard_code)
				with new_shard.lock:
					new_shard.clients.append(self)
					self.shard = new_shard

	def handle(self, packet_type, raw_packet):
		if packet_type == PacketInfo.Type.GAME_EVENT:
			packet = GameEvent()
			packet.ParseFromString(raw_packet)
			self.handle_event(packet)
		elif packet_type == PacketInfo.Type.SOUND_REQUEST:
			packet = SoundRequest()
			packet.ParseFromString(raw_packet)
			self.send_sound(packet)
		elif packet_type == PacketInfo.Type.SOUND_RESPONSE:
			packet = SoundResponse()
			packet.ParseFromString(raw_packet)
			self.save_sound(packet)
		elif packet_type == PacketInfo.Type.CLIENT_UPDATE:
			packet = ClientUpdate()
			packet.ParseFromString(raw_packet)
			self.update(packet)
		elif packet_type == PacketInfo.Type.SOUNDS_LIST:
			packet = SoundRequest()
			packet.ParseFromString(raw_packet)
			for hash in packet.sound_hash:
				self.check_or_request_sound(hash)
		else:
			print(str(self.addr) + ": Unhandled packet type!")
	
	def listen(self):
		print(str(self.addr) + " joined.")

		while self.server.running:
			try:
				# 255 bytes should be more than enough for the PacketInfo message
				with self.lock:
					data = self.sock.recv(255)
				if len(data) == 0:
					break
				
				packet_info = PacketInfo()
				packet_info.ParseFromString(data)
				
				if packet_info.length > 2 * 1024 * 1024:
					# Don't allow files or packets over 2 Mb
					break

				with self.lock:
					data = self.sock.recv(packet_info.length)
				if len(data) == 0:
					break
				
				self.handle(packet_info.type, data)
			except ConnectionResetError:
				break
			except socket.error as msg:
				print("Error: " + msg)
				break

		if self.shard != None:
			with self.shard.lock:
				self.shard.clients.remove(self)

		print(str(self.addr) + " left.")


class Server:
	def __init__(self):
		self.running = True
		self.init_sound_cache()
		self.clients_lock = Lock()
		self.clients = []

		self.shards_lock = Lock()
		self.shards = {}

	def shutdown(self):
		self.running = False
	
	def init_sound_cache(self):
		self.cache_lock = Lock()
		self.cache = []

		for file in os.listdir('cache'):
            # Only add valid files
			if file.startswith('.git') or not os.path.isfile(file):
				continue
			self.cache.append(file)

	def get_shard(self, name):
		with self.shards_lock:
			if name in self.shards:
				return self.shards[name]
			else:
				self.shards[name] = Shard(name)
				return self.shards[name]
				

	def serve(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind(("0.0.0.0", SOUND_SERVER_PORT))
		self.sock.listen(MAX_CLIENTS)

		while self.running:
			csock, addr = self.sock.accept()
			with self.clients_lock:
				client = Client(self, csock, addr)
				self.clients.append(client)
				Thread(target=client.listen, daemon=True).start()


if __name__ == "__main__":
	server = Server()
	signal.signal(signal.SIGTERM, server.shutdown)
	server.serve()
