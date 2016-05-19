#This is a Instant Messenger server program
#20160515 by HKK
#github link:https://github.com/aa40105/CCU_python/tree/master/Hw2

import sys, socket, select, string, os,time

	
SOCKET_LIST = []
RECV_BUFFER = 1024
name_list = []
hkkfriend = []
cmhfriend = []
rangefriend = []
#0 hkk 1 cmh 2 range
statuslist = ["offline","offline","offline"]
hkkoffline = ''
cmhoffline = ''
rangeoffline =''
hkkonline =''
cmhonline =''
rangeonline = ''


#main function
if __name__ == "__main__":
	__author__='HKK'
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('0.0.0.0', 3003))
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
							if(userpwd[1] =='hkkpw'):
								name_list.append('hkk')
								sock.sendall(str.encode("\nHello hkk "))
								#time.sleep(0.1)
								sock.sendall(str.encode("\n"+hkkoffline))
								statuslist[0] = "online"
								#print(statuslist[0])
							else:
								sock.sendall(str.encode("\nwrong id or passwd "))
								SOCKET_LIST.remove(sock)
								sock.close()
						elif(userpwd[0] == 'cmh'):
							if(userpwd[1] =='cmhpw'):
								name_list.append('cmh')
								sock.sendall(str.encode("\nHello cmh "))
								sock.sendall(str.encode(cmhoffline))
								statuslist[1] = "online"
								#print(statuslist[1])
							else:
								sock.sendall(str.encode("\nwrong id or passwd "))
								SOCKET_LIST.remove(sock)
								sock.close()
						elif(userpwd[0] == 'range'):
							if(userpwd[1] =='rangepw'):
								name_list.append('range')
								sock.sendall(str.encode("\nHello range "))
								#time.sleep(0.1)
								sock.sendall(str.encode(rangeoffline))
								statuslist[2] = "online"
								#print(statuslist[2])
							else:
								sock.sendall(str.encode("\nwrong id or passwd "))
								SOCKET_LIST.remove(sock)
								sock.close()
						#logout
						elif(userpwd[0] =='logout'):
							sock.sendall(str.encode("\n"+userpwd[1]+" is logout"))
							if(userpwd[1] == 'hkk'):
								statuslist[0] = "offline"
							elif(userpwd[1] == 'cmh'):
								statuslist[1] = "offline"
							elif(userpwd[1] == 'range'):
								statuslist[2] = "offline"
							SOCKET_LIST.remove(sock)
							name_list.remove(userpwd[1])
							sock.close()
						#friend list
						elif(userpwd[0] =='friend' and userpwd[1] == 'list'):
							if(userpwd[2] == 'hkk'):
								for x in hkkfriend:
									if(x == 'cmh'):
										sock.sendall(str.encode("\ncmh " + statuslist[1]))
									elif(x == 'range'):												sock.sendall(str.encode("\nrange " + statuslist[2]))
							elif(userpwd[2] == 'cmh'):
								for x in cmhfriend:
									if(x == 'hkk'):
										sock.sendall(str.encode("\nhkk " + statuslist[0]))
									elif(x == 'range'):												sock.sendall(str.encode("\nrange " + statuslist[2]))
							elif(userpwd[2] == 'range'):
								for x in rangefriend:
									if(x == 'hkk'):
										sock.sendall(str.encode("\nhkk " + statuslist[0]))
									elif(x == 'cmh'):												sock.sendall(str.encode("\ncmh " + statuslist[2]))
						#friend add
						elif(userpwd[0] =='friend' and userpwd[1]=='add'):
							#print(userpwd[3])
							if(userpwd[3] == 'hkk'):
								if userpwd[2] not in hkkfriend: 		
									hkkfriend.append(userpwd[2])
									sock.sendall(str.encode("\n"+userpwd[2]+' added into the friend list'))
								else :
									sock.sendall(str.encode("\nfriend is exist")) 
							elif(userpwd[3] == 'cmh'):
								if userpwd[2] not in cmhfriend: 		
									cmhfriend.append(userpwd[2])
									sock.sendall(str.encode("\n"+userpwd[2]+' added into the friend list'))
								else:
									sock.sendall(str.encode("\nfriend is exist")) 
							elif(userpwd[3] == 'range'):
								if userpwd[2] not in rangefriend: 		
									rangefriend.append(userpwd[2])
									sock.sendall(str.encode("\n"+userpwd[2]+' added into the friend list'))
								else:
									sock.sendall(str.encode("\nfriend is exist")) 
						#friend remove
						elif(userpwd[0] =='friend' and userpwd[1]=='rm'):
							if(userpwd[3] == 'hkk'):
								if userpwd[2] in hkkfriend: 		
									hkkfriend.remove(userpwd[2])
									sock.sendall(str.encode("\n"+userpwd[2]+' removed from the friend list'))
								else :
									sock.sendall(str.encode("\nfriend does't exist")) 
							elif(userpwd[3] == 'cmh'):
								if userpwd[2] in cmhfriend: 		
									cmhfriend.remove(userpwd[2])
									sock.sendall(str.encode("\n"+userpwd[2]+' removed from the friend list'))
								else :
									sock.sendall(str.encode("\nfriend does't exist")) 
							elif(userpwd[3] == 'range'):
								if userpwd[2] in rangefriend: 		
									rangefriend.remove(userpwd[2])
									sock.sendall(str.encode("\n"+userpwd[2]+' removed from the friend list'))
								else :
									sock.sendall(str.encode("\nfriend does't exist")) 
						#send to online
						elif(userpwd[0] == 'send'):
							num = len(userpwd) -1
							buff =''
							count = 2;
							
							#print(num)
							buff = buff + userpwd[num] + ' say '
							while(count < num):
								buff = buff + userpwd[count] + ' '
								count += 1
							if(userpwd[1] =='hkk'and statuslist[0] =='online' ):
								for socket in SOCKET_LIST:
									if(socket != server_socket and socket != sock):
										socket.sendall(str.encode("\nreceive from "+ buff))
							elif(userpwd[1] =='hkk'and statuslist[0] =='offline' ):
								hkkoffline = ("receive from " + buff)
								
							elif(userpwd[1] =='cmh'and statuslist[1] =='online' ):
								for socket in SOCKET_LIST:
									if(socket != server_socket and socket != sock):
										socket.send(str.encode("\nreceive from "+ buff))
							elif(userpwd[1] =='cmh'and statuslist[1] =='offline' ):
								cmhoffline = ("receive from " + buff)
							elif(userpwd[1] =='range'and statuslist[2] =='online' ):
								for socket in SOCKET_LIST:
									if(socket != server_socket and socket != sock):
										socket.send(str.encode("\nreceive from "+ buff))
							elif(userpwd[1] =='range'and statuslist[2] =='offline' ):
								rangeoffline = ("receive from " + buff)
						elif(userpwd[0] == 'sendfile'):
							num = len(userpwd) -1
							buff =''
							count = 2;
							buff = buff + userpwd[num] + ' want transmit '
							print(num)
							while(count < num):
								buff = buff + userpwd[count] + ' '
								count += 1
							filename = userpwd[2]
							print(filename)
							print(buff)
							if(userpwd[1] =='hkk'):
								for socket in SOCKET_LIST:
									if(socket != server_socket and socket !=sock):
										socket.send(str.encode("\ntransmit from " + buff + " YES or NO "))
						elif(userpwd[0] == 'YES'):
							print("sucess")
								
				except:
					print('')


