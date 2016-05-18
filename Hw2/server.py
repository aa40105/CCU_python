#This is a Instant Messenger server program
#20160515 by HKK
#github link:https://github.com/aa40105/CCU_python/tree/master/Hw2

import sys, socket, select, string, os

#def fun_login(user,pw)
	
SOCKET_LIST = []
RECV_BUFFER = 1024
name_list = ['server']


#main function
if __name__ == "__main__":
	__author__='HKK'
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('127.0.0.1', 3003))
	server_socket.listen(10)

	SOCKET_LIST.append(server_socket)
	
	print ("Server started !!")
	
	while 1:
		read_sockets, write_sockets,error_sockets = select.select(SOCKET_LIST,[],[],0)
		for sock in read_sockets:
			if(sock == server_socket):
				sc, sockname = server_socket.accept()
				SOCKET_LIST.append(sc)
			else:
				try:
					data = sock.recv(RECV_BUFFER)

					if data:
						dedata = data.decode("utf-8")
						userpwd = dedata.split(' ')
						
						if(userpwd[0] == 'hkk'):
							if(userpwd[1] == 'hkkpw')
								name_list.append('hkk')
								sock.sendall(str.encode("Hello hkk")
						else:
							print("wrong id or wrong passwd")
				except:
					print(" ")


