import socket 
import sys  

#gotta send a block of data please
def sendUpdate(block):
        
    # Create the socket
    s = socket.socket()          
    
    # our port number 
    port = 8000              
    
    # connect to the listener
    s.connect(('127.0.0.1', port)) 
    
    # receive data from the server 
    s.send(block.encode())
    print("sent contents. Closing")
    # close the connection 
    s.close()   

block = "SENT THIS"
sendUpdate(block)
