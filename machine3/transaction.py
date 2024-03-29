from blockchain import *
import datetime
import json

#find the transaction id by going through the blockchain txt file
def setTransactionId():
    file = open("blockchain.txt", "r")
    fileContents = file.read()
    if not fileContents: #file is empty
        transactionId = 1
        return transactionId
        file.close()
    else:
        blockchain = json.loads(fileContents) #turn it into a usable object
        currentBlock = blockchain[-1] #get the last block
        currentData = currentBlock['data']
        currentTransactionId = currentData['transactionId']
        newTransactionId = currentTransactionId + 1
        file.close()
        return newTransactionId #return the new transaction ID

#this is gonna be our transaction class where users will make a transaction

class transaction:
    dateTime = None
    items = [] 
    total = 0
    storeId = None
    transactionId = None 
    def __init__(self, storeId):
        self.storeId = storeId
        dateTime = datetime.datetime.now()
        self.dateTime = dateTime.strftime('%b %d %Y %I:%M%p')
        self.total = 0
        self.items = []
        self.transactionId = setTransactionId()


    
    def setTransaction(self):
        print("please enter the items you wish to add to the transaction")
        print("When you are done type exit")
        items = []
        while(True):
            userInputString = ""
            userInput = list(map(str,input("").split()))
            #make a string out of the list
            for x in range(len(userInput)):
                userInputString = userInputString + " " + userInput[x]
            #print("user string:", userInputString)
            if(userInputString == " exit"):
                #print("GOT HERE")
                if(len(items) > 0):
                    break
                else:
                    print("must have at least one item.")
                    continue
            else:
                print("added item:", userInputString)
                items.append(userInputString)
                continue
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

    




