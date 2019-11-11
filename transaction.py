from blockchain import *
import datetime
import json

#this is gonna be our transaction class where users will make a transaction

class transaction:
    dateTime = None
    items = [] 
    total = 0
    storeId = None
    transactionId = None 
    def __init__(self, storeId, transactionId):
        self.storeId = storeId
        self.transactionId = transactionId 
        dateTime = datetime.datetime.now()
        self.dateTime = dateTime.strftime("%c")
        self.total = 0
        self.items = []
    
    def setTransaction(self):
        print("please enter the items you wish to add to the transaction")
        print("When you are done type 0")
        userInput = input("") #grab the user Input
        items = []
        while(userInput != "0"):
            items.append(userInput)
            userInput = input("")
        self.items = items #change the item list to this one
        print("\n\n")
        print("Please type the total of the transaction")
        total = input("")
        while (True):
            try:
                total = float(total)
                break
            except:
                print("That is not an float.  Try again\n")
                continue
        self.total = total
        print("\n\n")

    def makeBlock(self):
        dataDict = {"storeId": 0, "transactionId": 0, "total": 0, "items": []}
        dataDict["total"] = self.total
        dataDict["items"] = self.items
        dataDict['storeId'] = self.storeId 
        dataDict['transactionId'] = self.transactionId
        #got the data dictionary
        #now let's get the previous hash
        file = open("blockchain.txt", "r") #open the file
        fileContents = file.read() 
        if not fileContents:
            hashBlock = 0 #this is gonna be our genesis block
        else:
            fileContents = json.loads(fileContents) #turn it into a list of dictionaries
            previousBlock = Block(fileContents[-1]) #make a block class out of the list's last dictionary
            hashBlock = previousBlock.hashThisBlock()
        #now we got the hash, and the data, let's get the date
        datetime = self.dateTime 
        #now let's create a block out of it and return it
        newBlock = createBlock(datetime, dataDict, hashBlock)
        file.close() #close the file
        return newBlock

    




