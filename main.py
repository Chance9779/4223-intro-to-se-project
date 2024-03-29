
from blockchain import *
from receiver import *
from transaction import *
from searchById import *
from search_date import *
from threading import Thread
from checkHash import *
from admin import *


# class defining Daemon Thread

class listeningForUpdatesThread(Thread):



    # Daemon Thread constructor

    def __init__(self):

        Thread.__init__(self)

    # Daemon Thread run method

    def run(self):
        #this is an inherent function.  It will be called
        #when start() is called on the daemon thread.
        #listen for another machine
        while True:
            try:
                update = startListening()
                update = json.loads(update) #gotta make it into something useful
                updateBlockchain(update)
                continue #continue this infinitely
            except:
                print("Something went wrong receiving for updating. Closing")
                exit()

class listeningForChecksThread(Thread):



    # Daemon Thread constructor

    def __init__(self):

        Thread.__init__(self)

    # Daemon Thread run method

    def run(self):
        #this is an inherent function.  It will be called
        #when start() is called on the daemon thread.
        #listen for another machine
        while True:
            try:
                update = startListeningForChecks()
                continue #continue this infinitely
            except:
                print("Something went wrong receiving for checking. Closing")
                exit()

class listeningForOverwritesThread(Thread):

    # Thread constructor
    def __init__(self):
        Thread.__init__(self)

    # Thread run method
    def run(self):
        # another inherent function, also called when start() is called on the
        # daemon thread.
        # listen for any overwrite messages from other machines (by admins)
        while True:
            try:
                overwrite = startListeningForOverwrites()
                overwrite = json.loads(overwrite)
                overwriteBlockchain(overwrite)
                continue # continue infinitely
            except:
                print("Something went wrong trying to overwrite the blockchain. Closing")
                exit()


# Main thread

#listen for updates
listeningforUpdatesThread = listeningForUpdatesThread()

listeningforUpdatesThread.daemon = True
#starts the background listening
listeningforUpdatesThread.start()

#now listen for checks
listeningforChecksThread = listeningForChecksThread()

listeningforChecksThread.daemon = True
#starts the background listening
listeningforChecksThread.start()

# listen for overwrite messages from admins
listeningForOverwritesThread = listeningForOverwritesThread()

listeningForOverwritesThread.daemon = True
# start in the background
listeningForOverwritesThread.start()

#MAIN
#------------------------------------------------------
print("Welcome to our transaction system!")
print("")
while(True):
    print("please type in the password below and hit enter or type 0 to exit")
    userInput = input("")
    if(userInput == "0"):
        exit()
    #check the password
    elif(userInput == "admin"):
        #admin stuff
        adminView()
        continue
    elif(userInput == "12345"):
        break
    else:
        print("that was the wrong password.  Please try again.")
        continue

#we got past the password checker

while(True):
    print("please type out the character that represents your desired function.")
    print("----------------------------------------------------------------------")
    print("'t'    to create a transaction")
    print("'s'    to search through transactions")
    print("'x'    to exit")
    #  t is to create a transaction
    #
    # s to search
    #
    # x to exit
    #
    # ignore anything else
    #
    userInput = input("")
    if(userInput == 'x'):
        exit()
    #create a transaction and update the blockchain
    #
    #
    #************************TODO****************************
    # this must be updated or put into a function so that it can
    # send updated blocks to the other machine's in the
    elif(userInput == 't'):
        newTransaction = transaction(1) #our store number is 1
        newTransaction.setTransaction()
        newBlock = newTransaction.makeBlock()
        updateBlockchain(newBlock)
        updateOtherBlockchains(newBlock)
        continue
    #*********************************************************
    elif(userInput == 's'):
        #this is the search tree.  This will continue until the user backs out of it
        while(True):
            print("Type 'd' to search by date, 's' to search by store ID, or 't' to search by transaction id. (type 0 to return to main screen)")
            check = input("")
            if(check == 'd'):
                searchByDateInterface()
                continue
            #store id search tree
            elif(check == 's'):
                print("please type the store ID you wish to search for: ")
                storeId = input("")
                try:
                    storeId = int(storeId)
                    results = searchByStoreId(storeId)
                    viewSearch(results)
                    continue
                except:
                    print("Something went wrong.  Make sure you enter an integer value")
                    continue
            #transaction id search tree
            elif(check == 't'):
                print("please type the transaction ID you wish to search for: ")
                transId = input("")
                #try to search by transaction id
                try:
                    transId = int(transId)
                    results = searchByTransactionId(transId)
                    viewSearch(results)
                    continue
                except:
                    print("Something went wrong.  Make sure you enter an integer value")
                    continue
            elif(check == "0"):
                break
            #wasn't a valid character. ignore it
            else:
                print("that character was not accepted.")
                continue
    #wasn't a valid character. ignore it
    else:
        print("that character was not accepted.")
        continue
