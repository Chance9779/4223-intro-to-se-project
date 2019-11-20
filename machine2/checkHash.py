import json
import datetime
from blockchain import *
from transaction import *
import socket 
import sys  


'''
Check hash

1.  check hash takes in a block from the main blockchain and a block from the
new blockchain and calculates each block's hashes.  If they are not the same, throw an error

updateBlockchain()

1.  this function is going to go through all machines listening and update their blockchains

                main  2nd   3rd
machine ports: [8000, 8001, 8002]

this function is going to take in a block to update every other machine on the system


'''

#this function will take in a fully complete block
def updateOtherBlockchains(block):
    #these are our machines on the network by port number
    machines = [8000, 8002] #this is the main machine, it won't send an update to itself.
    #this list will change depending on what machine you're looking at the code in  
           
    #remember, we'll be getting a block.  We need to convert it to json
    block = json.dumps(block)
    
    # our port number 
    for x in range(len(machines)):
            # Create the socket
        s = socket.socket() 
        port = machines[x]         
    
        # connect to the listener
        s.connect(('127.0.0.1', port)) 
        # receive data from the server 
        s.send(block.encode())
        #print("sent contents to machine: ", x, " Closing")
    # close the connection 
        s.close()   

#each machine will be listening on port 900(whatever number they are)
#this port is different than the updateBlockchain port. Remember
def checkOtherMachineBlockchain(otherBlockchain):
    #grab our own blockchain
    file = open("blockchain.txt", "r")
    fileContents = file.read()
    fileContents = json.loads(fileContents)
    perfect = 0 #this is just to see if we had 0 errors

    if (len(fileContents) != len(otherBlockchain)):
        print("blockchains are not of the same length.")
        return

    #we have the other blockchain, so let's compare with their blocks
    for x in range(len(fileContents)):
        check = checkHash(fileContents[x], otherBlockchain[x])
        #print("RESULT: ", check)
        if (check != 1):
            print("ERROR CODE: ", check)
            perfect = 1
    if(perfect == 0):
        return 1 #no errors at all





#this will take a blockchain of a system and check the hashes to make sure they're correct
def checkHash(mainBlock, newBlock):
    #first initialize the blocks
    mainBlock = Block(mainBlock)
    newBlock = Block(newBlock)

    #now get the hashes
    mainBlockHash = mainBlock.hashThisBlock()
    newBlockHash = newBlock.hashThisBlock()

    if (mainBlockHash != newBlockHash):
        print("Error: block hashes do not match on transaction: ", mainBlock.data['transactionId'])
        print("mainHash: ", mainBlockHash)
        print("newHash: ", newBlockHash)
        return 0
    else:
        return 1
    