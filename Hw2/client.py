#This is a Instant Messenger client program
#20160515 by HKK
#github linuk:https//github.com/aa40105/CCU_python/tree/master/Hw2

import sys, socket, select, string, os

#hide passwd
def hide_passwd():
	os.system("stty -echo")
	hidenpass = input ("passwd:")
	os.system("stty echo")
	return hidepass

#main function

if __name__ == "__main__":
	
	host = '127.0.0.1'
	port = 3003
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.settimeout(2)

	# connect to server
	try:
		client_socket.connect((host, port))
	except :
		print ("Unable to connect to Server")
		print (host)
		sys.exit()

	print ("Connect to server success!")
	user = input ("user: ")
	passwd = hide_passwd()

	while 1:
		socket_list = [sys.stdin, client_socket]
		read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
		for sock in read_sockets:
			if sock == s:
				data = sock.recv[1024]
				if not data:
					print("Disconneted from chat server\n")
					sys.exit()
				else:
					tmp = data.decode('utf-8')
					temp = tmp.split()
					print(data.decode('utf-8'))
			
