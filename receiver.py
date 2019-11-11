#this is where we're gonna transfer all of our stuff and make sure our hashes match 

import socket 
import sys  
import atexit
import json


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
        print("received: ", content.decode())

        content = content.decode() #decode to something we can actually use.
        #Remember, this will be returned as a string
        
        s.close() #close the socket
        return content

#this will update the blockchain txt file whenever a block get's sent
def updateBlockchain(block):
    file = open("blockchain.txt", 'r') #open the txt file
    #grab the json from the file
    fileContents = file.read()
    if fileContents:
        blockList = json.loads(fileContents) #convert the json from string to an object
    else:
        blockList = []
    file.close()
    
    #now we got something useable
    blockList.append(block)
    #we append the block to the blocklist
    #then put the blocklist back
    blockList = json.dumps(blockList)
    file = open("blockchain.txt", "w") #open the file for writing
    file.write(blockList) #write to the file
    #yay, we're done
    file.close()


    