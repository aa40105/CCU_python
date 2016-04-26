#This is a server program about DHCP
#20160420 by HKK

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
class	DHCPAck:

if __name__ == "__main__":
	print ("DHCP server start")
	dhcp = socket.socket.AF_INET, socket, SOCK_DGRAM)
	dhcp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	try:
		dhcps.bind(('',68)) #bind port 68
	except Exception as e:
		print("port 68 in use")
		dhcp.close()
		input('Press any key to quit')
		exit()
	
	
	
	
		
