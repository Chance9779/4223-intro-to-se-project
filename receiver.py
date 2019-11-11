#this is where we're gonna transfer all of our stuff and make sure our hashes match 

import socket 
import sys  

#first we're gonna make a socket
def startListening():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a TCP socket
        print ("Socket successfully created")
    except:
        print("socket creation failed.  Exiting")
        exit()

    #this is gonna be our port.  
    port = 8000

    # Next bind to the port 
    # we have not typed any ip in the ip field 
    # instead we have inputted an empty string 
    # this makes the server listen to requests  
    # coming from other machines on the network 
    s.bind(('', port))         
    print ("socket binded to %s" %(port))

    while True:
        s.listen(5) #listen for others on the network
        c, addr = s.accept() #accept a connection if one is available
        print("accepted connection from", addr)
        
        #receive the information from another machine
        content = c.recv(1023) #max size of the thing
        print(content.decode())
        
        s.close() #close the socket
        return content

startListening()



