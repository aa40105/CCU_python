#This is a Instant Messenger client program
#20160515 by HKK
#github linuk:https//github.com/aa40105/CCU_python/tree/master/Hw2

import sys, socket, select, string, os

#hide passwd
def hide_passwd():
	os.system("stty -echo")
	hidenpass = input ('passwd:')
	os.system("stty echo")
	return hidenpass

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
		sys.exit()

	print ("Connect to server success!\n")
	user = input("user:")
	#print (user)
	passwd = hide_passwd()
	userpwd = user + ' ' + passwd
	client_socket.send(str.encode(userpwd))
	while 1:
		socket_list = [sys.stdin, client_socket]
		read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

		for sock in read_sockets:
			if sock == client_socket:
				data = sock.recv(1024)
				if not data:
					print("Disconneted from chat server\n")
					sys.exit()
				else:
					print(data.decode('utf-8'))
			else:
				msg = input('>')
				if(msg == 'logout'):
					client_socket.send(str.encode(msg + ' ' + user))
