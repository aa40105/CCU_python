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
	serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serversocket.bind(('0.0.0.0', 3003))
	serversocket.listen(10)

	SOCKET_LIST.append(serversocket)
	
	print ("Server started !!")

