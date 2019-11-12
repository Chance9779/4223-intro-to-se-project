from blockchain import *
import datetime
import json
from transaction import *
import datetime


#this will search by storeId and return a list of objects with that storeId

def searchByStoreId(storeId):
    #open the file and grab the contents
    file = open("blockchain.txt", "r")
    fileContents = file.read()
    fileContents = json.loads(fileContents) #now its a python object (list to be exact)
    searchResults = [] #this will hold all of the blocks returned in the search

    #linearly search the wholllleee damn thing.  Unless its empty
    if not fileContents:
        print("I'm sorry.  The blockchain is empty.  Closing")
        file.close()
        return None

    else:
        for x in range(len(fileContents)): #for x in range of the blockchain's length

            currentBlock = fileContents[x] #this is our current Block.  check if its the right one
            #print("currentBlock: ", currentBlock)

            currentBlockData = currentBlock['data'] #this is our current block's data
            #print("currentBlockData: ", currentBlockData)

            if (currentBlockData['storeId'] == storeId):
                #print("appended: ", currentBlock)
                searchResults.append(currentBlock) #add the block if it fits
        file.close()
        return searchResults      

def searchByTransactionId(transactionId):
    #open the file and grab the contents
    file = open("blockchain.txt", "r")
    fileContents = file.read()
    fileContents = json.loads(fileContents) #now its a python object (list to be exact)
    searchResults = [] #this will hold all of the blocks returned in the search

    #linearly search the wholllleee damn thing.  Unless its empty
    if not fileContents:
        print("I'm sorry.  The blockchain is empty.  Closing")
        file.close()
        return None

    else:
        for x in range(len(fileContents)): #for x in range of the blockchain's length

            currentBlock = fileContents[x] #this is our current Block.  check if its the right one
            #print("currentBlock: ", currentBlock)

            currentBlockData = currentBlock['data'] #this is our current block's data
            #print("currentBlockData: ", currentBlockData)

            if (currentBlockData['transactionId'] == transactionId):
                #print("appended: ", currentBlock)
                searchResults.append(currentBlock) #add the block if it fits
        file.close()
        return searchResults  

#this will turn it into a pretty string
def viewSearch(searchResults):
    if not searchResults: #searchResults didn't exist
        print("I'm sorry, there are no transactions matching these parameters.")
        return None
    
    if (searchResults[0] == None):
        print("I'm sorry, we did not find any transactions with those parameters.")
        return None

    for x in range(len(searchResults)): #for all the results
        dateTime = searchResults[x]['datetime']
        currentData = searchResults[x]['data']
        storeId = currentData['storeId']
        transId = currentData['transactionId']
        total = currentData['total']
        items = currentData['items']
        print("Transaction: ", transId)
        print("\ncreated on date: ", dateTime)
        print("\nitems: ")
        for i in range(len(items)):
            print(items[i])
        print("-------------------------------")
        print("total: ", total)
        print("\n\n")

