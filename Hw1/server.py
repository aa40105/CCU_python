#This is a server program about DHCP
#20160420 by HKK
#github link:https://github.com/aa40105/CCU_python/tree/master/Hw1

import socket
import struct
from uuid import getnode as get_mac
from random import randint

def getMacBytes():
	mac = str(hex(get_mac()))
	mac = mac[2:]
	while len(mac) < 12 :
		mac = '0' + mac
	macb = b''
	for i in range (0, 12, 2) :
		m = int(mac[i:i + 2], 16)
		macb += struct.pack('!B',m)
	return macb

class	DHCPOffer:
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
		packet += b'\x00\x00\x00\x00'	#CIADDR(Client IP address)
		packet += b'\xC0\xA8\x01\x64'	#YIADDR(Your IP address)
		packet += b'\xC0\xA8\x01\x01'	#SIADDR(Server IP address)
		packet += b'\x00\x00\x00\x00'	#GIADDR(Gateway IP address)
		packet += macb			#CHADDR(Client hardware address)
		packet += b'\x00\x00\x00\x00\x00'#Client hardware address padding
		packet += b'\x00\x00\x00\x00\x00'#
		packet += b'\x00' * 192		#192
		packet += b'\x63\x82\x53\x63'	#Magic cookie: DHCP
		packet += b'\x35\x01\x02'	#Option: DHCP Offer 53
		packet += b'\x3d\x06' + macb	#Client identifier
		packet += b'\x37\x03\x03\x01\x06'#Option 55 Parameter Request list
		packet += b'\xff'		#End Option
		return packet

class	DHCPAck:

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
		packet += b'\x00\x00\x00\x00'	#CIADDR(Client IP address)
		packet += b'\xC0\xa8\x01\x64'	#YIADDR(Your IP address)
		packet += b'\xc0\xa8\x01\x01'	#SIADDR(Server IP address)
		packet += b'\x00\x00\x00\x00'		#GIADDR(Gateway IP address)
		packet += macb			#CHADDR(Client hardware address)
		packet += b'\x00\x00\x00\x00\x00'#Client hardware address padding
		packet += b'\x00\x00\x00\x00\x00'#
		packet += b'\x00' * 192		#192
		packet += b'\x63\x82\x53\x63'	#Magic cookie: DHCP
		packet += b'\x35\x01\x05'	#Option:53 DHCP Ack
		packet += b'\xff'		#End Option
		return packet

if __name__ == "__main__":
	input("Press any key to start DHCP server program\n")
	dhcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dhcp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	try:
		dhcp.bind(('',67)) #bind port 67
	except Exception as e:
		print("port 67 in use")
		dhcp.close()
		input('Press any key to quit')
		exit()
	while True:
		data = dhcp.recv(1024)
		if data == '':
			break
		else:
			break

	offerPacket = DHCPOffer()
	dhcp.sendto(offerPacket.DHCPPacket(), ('<broadcast>', 68))
	while True:
		data = dhcp.recv(1024)
		if data == '':
			break
		else:
			break
	offerAck = DHCPAck()
	dhcp.sendto(offerAck.DHCPPacket(), ('<broadcast>', 68))
	dhcp.close()
	input("Press any key to close DHCP server program\n")
	exit()
