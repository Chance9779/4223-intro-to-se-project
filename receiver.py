#this is where we're gonna transfer all of our stuff and make sure our hashes match

import socket
import sys
import atexit
import json
from sender import *


#first we're gonna make a socket
def startListening():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a TCP socket
        #print ("Socket successfully created")
    except:
        #print("socket creation failed.  Exiting")
        exit()

    #this is gonna be our port.
    port = 8000

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other machines on the network
    s.bind(('', port))
    #print ("socket binded to %s" %(port))

    while True:
        s.listen(5) #listen for others on the network
        c, addr = s.accept() #accept a connection if one is available
        #print("accepted connection from", addr)

        #receive the information from another machine
        content = c.recv(1023) #max size of the thing
        #print("received: ", content.decode())

        content = content.decode() #decode to something we can actually use.
        #Remember, this will be returned as a string

        s.close() #close the socket
        return content


def startListeningForChecks():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a TCP socket
        #print ("Socket successfully created")
    except:
        #print("socket creation failed.  Exiting")
        exit()

    #this is gonna be our port.
    # NOTE: this is a different port than the normal listening port
    port = 9000

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other machines on the network
    s.bind(('', port))
    #print ("socket binded to %s" %(port))

    #-----------------------------------------------------------------
    while True:
        s.listen(5) #listen for others on the network
        c, addr = s.accept() #accept a connection if one is available
        #print("accepted connection from", addr)

        #get the port from the other machine
        content = c.recv(1023) #max size of the thing

        newPort = content.decode() #decode it into a port number
        newPort = int(newPort)


        s.close()
        break

    file = open("blockchain.txt", "r")
    fileContents = file.read()

        # Create the socket again
    s = socket.socket()

    # connect to the listener
    s.connect(('127.0.0.1', newPort))

    #send the file contents
    if fileContents: #the fileContents
        fileContents = json.loads(fileContents)
        #print("fileContents: ", fileContents)
        for x in range(len(fileContents)):
            block = fileContents[x]
            block = json.dumps(block)
            s.send(block.encode())
            #print("SENT: ", block)

        #got to the end. send a 0
    block = "\0"
    #print("SENT: ", block, "ENDED")
    #s.send(block.encode())
    s.close()

    print("sent check.")

#first we're gonna make a socket
def startListeningForOverwrites():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a TCP socket
        #print ("Socket successfully created")
    except:
        #print("socket creation failed.  Exiting")
        exit()

    #this is gonna be our port.
    port = 8050

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other machines on the network
    s.bind(('', port))
    #print ("socket binded to %s" %(port))

    while True:
        s.listen(5) #listen for others on the network
        c, addr = s.accept() #accept a connection if one is available
        #print("accepted connection from", addr)

        #receive the information from another machine
        content = c.recv(1023) #max size of the thing
        #print("received: ", content.decode())

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
    #print("BLOCKLIST TYPE: ", type(blockList))
    blockList.append(block)
    #we append the block to the blocklist
    #then put the blocklist back
    blockList = json.dumps(blockList)
    file = open("blockchain.txt", "w") #open the file for writing
    file.write(blockList) #write to the file
    #yay, we're done
    file.close()

#this will overwrite the blockchain txt file whenever an admin sends an overwrite
def overwriteBlockchain(block):
    blockList = []
    blockList.append(block)
    #we append the block to the blocklist
    #then put the blocklist back
    blockList = json.dumps(blockList)
    file = open("blockchain.txt", "w") #open the file for writing
    file.write(blockList) #write to the file
    #yay, we're done
    file.close()
