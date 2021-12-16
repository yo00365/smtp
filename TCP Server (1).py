# libraries
from socket import AF_INET, SOCK_STREAM, socket
import uuid
import json 
#tcp connection
if __name__ == '__main__':
   print("Application started")
   s = socket(AF_INET,SOCK_STREAM) # creating socket
   print('TCP socket created')
   s.bind(('127.0.0.1',7777)) # binding socket
   print('socket is bound to %s:%d' % s.getsockname()) # obtaining port address
   backlog = 0 
   s.listen(backlog)
   print('Socket %s:%d is in listening state' % s.getsockname())
   client_socket,client_addr = s.accept() # receiving port
   print('new client connectedfrom %s:%d'% client_addr)
   print ('local end-point socket bound on: %s:%d'%client_socket.getsockname())
   print('Mac address: ',hex(uuid.getnode())) # obtaining mac address
   data = r'{"code":"0","msg":"ok","obj":[{"port":"44139","ip":"113.73.67.60"}],"errno":0,"data":[null]}'
   ip = json.loads(data)['obj'][0]['ip'] # obtaining ip address
   print('IP Address: ',ip)
    
   client_socket.send("220".encode()) # connection is ready
   # the server receives the first command 
   Reply = client_socket.recv(1024).decode("utf-8") # the received data saved in varible 
   if Reply != 'HELO': #server check if the massage received successfully 
       print("HELOcommand not received from the client ") # error massage
   else:
       print(Reply) # print received data
       client_socket.send("250".encode()) # send response code to the client 
       
   # the second command
   R2 = client_socket.recv(1024).decode("utf-8")
   if R2 != 'MAIL FROM:<youssefdihyah@gmail.com>':
       print("mail from command not not received fromm the client ")
   else:
       print(R2)
       client_socket.send("250".encode())
       
    # the third command
   R3 = client_socket.recv(1024).decode("utf-8")
   if R3 != 'RCPT TO:<youssefomar@gmail.com>':
       print("RCPT TO command not not received fromm the client")
   else:
       print(R3)
       client_socket.send("250".encode())
       
   # the forth command
   R4 = client_socket.recv(1024).decode("utf-8")
   if R4 != "DATA":
       print("DATA command not not received fromm the client")
   else:
       print(R4)
       client_socket.send("354".encode())
       
   #  the fifth command  
   R5 = client_socket.recv(1024).decode("utf-8")
   if R5 != "subject:<cw1>":
       print("subject command not not received fromm the client")
   else:
       print(R5)
       client_socket.send("250".encode())
       
    # the sixth command
   R6 = client_socket.recv(1024).decode("utf-8")
   if R6 != "body:<code>":
       print("body command not not received fromm the client")
   else:
        print(R6)
        client_socket.send("250".encode())
        
    # the seventh command    
   R7 = client_socket.recv(1024).decode("utf-8")
   if R7 != "<CRLF>.<CRLF>":
       print("termination command not not received fromm the client")
   else:
        print(R7)   
        client_socket.send("250".encode())
        
   # the eighth command
   R8 = client_socket.recv(1024).decode("utf-8")
   if R8 != "QUIT":
       print("QUIT command not not received fromm the client")
   else:
       print(R8)
       client_socket.send("221".encode())
       
     # closeing the socket 
   input('press enter to terminate...')
   client_socket.close()
   s.close()
   print('closed the client socket')
   print('Terminating...')