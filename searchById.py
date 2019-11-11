from blockchain import *
import datetime
import json
from transaction import *


#this will search by storeId and return a list of objects with that storeId

def searchById(storeId):
    #open the file and grab the contents
    file = open("blockchain.txt", "r")
    fileContents = file.read()
    fileContents = json.loads(fileContents) #now its a python object (list to be exact)
    searchResults = [] #this will hold all of the blocks returned in the search

    storeId = str(storeId) #change it to a string to compare

    #linearly search the wholllleee damn thing.  Unless its empty
    if not fileContents:
        print("I'm sorry.  The blockchain is empty.  Closing")
        return None

    else:
        for x in range(len(fileContents)): #for x in range of the blockchain's length

            currentBlock = fileContents[x] #this is our current Block.  check if its the right one

            currentBlockData = currentBlock[x]['data'] #this is our current block's data

            if (currentBlockData['storeId'] == storeId):
                searchResults.append(currentBlock)


