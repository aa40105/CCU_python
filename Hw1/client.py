#This is a client program about DHCP
#20160420 by HKK
#github link:

import socket
import struct
from uuid import getnode as get_mac
from random import randint

def getMacBytes():
	mac = str(hex(get_mac()))
	mac = mac[2:]
	while len(mac) < 12:
		mac = '0' + mac
	macb = b''
	for i in range(0, 12, 2):
		m = int(mac[i:i +2], 16)
		macb += struct.pack('!B', m)
	return macb

class	DHCPDiscover:
	def __init__(self):
		self.transactionID = b''
		for i in range(4):
			t = randint(0, 255)
			self.transactionID += struct.pack('!B', t)
	
	def DHCPPacket(self):
		macb = getMacBytes()
		packet = b''
		packet += b'\x02'		#OP
		packet += b'\x01'		#HTYPE
		packet += b'\x06'		#HLEN
		packet += b'\x00'		#HOPS
		packet += b'\x39\x03\xF3\x26'	#XID
		packet += b'\x00\x00'		#SECS
		packet += b'\x80\x00'		#FLAGS
		packet += b'\x00\x00\x00\x00'	#CIADDR(client IP address)
		packet += b'\x00\x00\x00\x00'	#YIADDR(Your IP address)
		packet += b'\x00\x00\x00\x00'	#SIADDR(Server IP address)
		packet += b'\x00\x00\x00\x00'	#GIADDR(Gateway IP address)
		packet += macb			#CHADDR(client hardware address)
		packet += b'\x00\x00\x00\x00'	#Client hardware address padding
		packet += b'\x00\x00\x00\x00'	#Client hardware address padding
		packet += b'\x00\x00'		#Client hardware address padding
		packet += b'\x00' * 67		#67
		packet += b'\x00' * 125		#125
		packet += b'\x63\x82\x53\x63'	#Magic cookie: DHCP
		packet += b'\x35\x01\x01'	#Option: DHCP Discover
		packet += b'\x3d\x06' + macb	#
		packet += b'\x37\x03\x03\x01\x06'#DHCP Options 53
		packet += b'\xff'		#End Options 
		return packet

class	DHCPRequest:
	def DHCPPacket(self):
		macb = getMacBytes()
		packet = b''
		packet += b'\x01'		#OP
		packet += b'\x01'		#HTYPE
		packet += b'\x06'		#HLEN
		packet += b'\x00'		#HOPS
		packet += b'\x39\x03\xF3\x26'	#XID
		packet += b'\x00\x00'		#SECS
		packet += b'\x00\x00'		#FLAGS
		packet += b'\x00\x00\x00\x00'	#CIADDR(client IP address)
		packet += b'\x00\x00\x00\x00'	#YIADDR(Your IP address)
		packet += b'\xc0\xA8\x01\x01'	#SIADDR(Server IP address)
		packet += b'\x00\x00\x00\x00'	#GIADDR(Gateway IP address)
		packet += macb			#CHADDR(client hardware address)
		packet += b'\x00\x00\x00\x00'	#Client hardware address padding
		packet += b'\x00\x00\x00\x00'	#Client hardware address padding
		packet += b'\x00\x00'		#Client hardware address padding
		packet += b'\x00' * 67		#67
		packet += b'\x00' * 125		#125
		packet += b'\x63\x82\x53\x63'	#Magic cookie: DHCP
		packet += b'\x35\x01\x03'	#Option: DHCP Request
		packet += b'\x3d\x06' + macb	#
		packet += b'\x32\x04\xc0\xa8\x01\x64'#DHCP Options 50
		packet += b'\xff'		#End Options 
		return packet

if __name__ == "__main__":
	input("Press any key to start DHCP client program\n")
	dhcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dhcp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	print("send DISCOVER packet\n")
	requestPacket = DHCPRequest()
	dhcp.sendto(requestPacket.DHCPPacket(), ('<broadcast>', 67))
	print("send DHCPREQUEST packet\n")
	dhcp.close()
	input("Press any key to close DHCP client program\n")
	exit()

