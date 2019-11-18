import socket 
import sys
import json  

#gotta send a block of data please
def sendUpdate(block):
        
    # Create the socket
    s = socket.socket()          
    
    # our port number 
    port = 8000         
    
    # connect to the listener
    s.connect(('127.0.0.1', port)) 

    #remember, we'll be getting a block.  We need to convert it to json
    block = json.dumps(block)
    # receive data from the server 
    s.send(block.encode())
    print("sent contents. Closing")
    # close the connection 
    s.close()   

def sendCheck(port):
    #someone asked to check our machine.  Send packets of each dict in our blockchain
    file = open("blockchain.txt", "r")
    fileContents = file.read()

        # Create the socket
    s = socket.socket()          
    
    # our port number 
    port = port        
    
    # connect to the listener
    s.connect(('127.0.0.1', port)) 

    #send the file contents
    if fileContents: #the fileContents
        fileContents = json.loads(fileContents)
        #print("fileContents: ", fileContents)
        for x in range(len(fileContents)):
            block = fileContents[x]
            block = json.dumps(block)
            s.send(block.encode())
            print("SENT: ", block)
        #got to the end. send a 0
        block = "0"
        #print("SENT: ", block, "ENDED")
        s.send(block.encode())
    else:
        print("Blockchain is empty. Sending nothing")
        content = "0"
        s.send(content.encode())
    s.close()

