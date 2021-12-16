#libraries
from socket import AF_INET, SOCK_STREAM, socket 
import uuid
import json
# TCP connection 
if __name__ == '__main__':
   print("Application started")
   s = socket(AF_INET,SOCK_STREAM) # creating socket
   print('TCP socket created')
   server_address =('127.0.0.1',7777)
   s.connect(server_address) # connecting to the server
   print('socket connected to %s:%d' % s.getpeername()) # obtaining port address
   print ('local end-point is bound to %s:%d'%s.getsockname())
   print('Mac address: ',hex(uuid.getnode())) # obtaining mac address
   data = r'{"code":"0","msg":"ok","obj":[{"port":"44139","ip":"113.73.67.60"}],"errno":0,"data":[null]}'
   ip = json.loads(data)['obj'][0]['ip'] # obtaining ip address
   print('IP Address: ',ip)
   
   recv = s.recv(1024).decode("utf-8") # reseiving the respoce code
   if recv[:3] != '220' : # checking the server responce code
    print ('220 reply not received from server.')
   else:
       print (recv)
       heloCommand = 'HELO'
       s.send(heloCommand.encode()) # sending the first command
       
   recv1 = s.recv(1024).decode("utf-8")
   if recv1[:3] != '250' :
       print ('250 reply not received from server.')
   else:
       print (recv1)
       mailfromCommand = 'MAIL FROM:<youssefdihyah@gmail.com>'
       s.send(mailfromCommand.encode()) # sending second command
       
   recv2 = s.recv(1024).decode("utf-8")
   if recv2[:3] != '250' :
       print ('250 reply not received from server.')
   else:
       print (recv2)
       rcptToCommand = 'RCPT TO:<youssefomar@gmail.com>'
       s.send(rcptToCommand.encode())# sending third command 
       
   recv3 = s.recv(1024).decode("utf-8")
   if recv3[:3] != '250' :
       print ('250 reply not received from server.')
   else:
        print (recv3)
        dataCommand = 'DATA'
        s.send(dataCommand.encode()) # sending forth command
        
   recv4 = s.recv(1024).decode("utf-8")
   if recv4[:3] != '354' :
       print ('354 reply not received from server.')
   else:
       print (recv4)
       subject= 'subject:<cw1>'
       s.send(subject.encode()) # sending fifth command 
       
   recv5 = s.recv(1024).decode("utf-8")
   if recv5[:3] != '250' :
       print ('250 reply not received from server.')
   else:
        print (recv5)
        body= 'body:<code>'
        s.send(body.encode()) # sending sixth command
        
   recv6 = s.recv(1024).decode("utf-8")     
   if recv6[:3] != '250' :
       print ('250 reply not received from server.')
   else:
        print (recv6)
        terminationsequenceCommand = "<CRLF>.<CRLF>"
        s.send(terminationsequenceCommand.encode()) # sending seventh command
       
   recv7 = s.recv(1024).decode("utf-8")
   if recv7[:3] != '250' :
       print ('250 reply not received from server.')
   else:
        print (recv7)   
        quitCommand = "QUIT"
        s.send(quitCommand.encode()) # sending eighth command
        
   recv8 = s.recv(1024).decode("utf-8")
   if recv8[:3] != '221' :
       print ('221 reply not received from server.')
   else :
       print (recv8 )
       
   input('Press enter to terminate...  ') # closeing socket 
   s.close()
   print('Terminating...')
   