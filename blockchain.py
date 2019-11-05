""" /*
This is a blockchain.  Blocks in a blockchain hold a datetime stamp, the data in question, and a hash
of the PREVIOUS block's datetime + data

We're gonna hold our blockchain in a txt file on the machine.  This is gonna be a list of dictionaries 
that's converted to a JSON string to hold it.  When we need it, we'll just pull it out of JSON format from the txt file.

Storing it in a txt file allows us to hold the txt file on seperate machines.  Each machine will have its own
txt file and every time a block is added from one machine, it will send the new dictionary to the other
machines txt files.

In terms of security, we will define a function that checks the hashes of all blocks and makes sure
that there hasn't been any tampering with the blockchain in any way.

*/
 """
from driver import *
import datetime
import hashlib

#blockchain class
class Blockchain:
    #this will hold the blockchain as it is
    blockchain = []
    
    #constructor
    def __init__(self):
        self.blockchain = fromJSON() #this loads our blockchain from the blockchain.txt file

    #just an easy way of converting the blockchain to a string
    def __str__(self):
        blockchain = toJSON(self.blockchain)
        return blockchain

#this will hold the contents inside our 
class Block:
    block = {} #block is a dictionary
    datetime = None #datetime
    data = None #data - a dictionary usually.  This will be changed to JSON for hash and storing
    hashBlock = None #hash
    #constructor
    def __init__(self, block):
        self.block = block #grab our block dictionary
        self.datetime = block.get("datetime")
        self.data = block.get("data")
        self.hashBlock = block.get("hashBlock")

    #just a way of getting a quick and easy string
    def __str__(self):
        return str(self.block)

    #this is for getting the hash of THIS block.
    #this will only be used by SUBSEQUENT blocks to get the hash that they will carry. 
    def hashThisBlock():
        #first, we'll concatenate the datetime and data together
        data = toJSON(self.data) #convert the data to JSON 
        datetime = self.datetime.strftime("%c") #this converts datetime to a readable string
        contents = data + datetime 
        hashBlock = hashlib.md5(contents) #hash the stuff 
        return hashBlock #spit it out 

def createBlock(datetime, data, hashBlock):
#global base dictionary for a block
    block = {
        "datetime": None,
        "data": None,
        "hashBlock": None
    }
    block['datetime'] = datetime.strftime("%c")
    block['data'] = data
    block['hashBlock'] = hashBlock 
    return block

        