
from blockchain import *
from receiver import *
from transaction import *
from searchById import *
from search_date import *
from threading import Thread
from checkHash import *

def adminView():
    print("Hello admin!")
    while True:
        print("")
        print("Please type the letter corresponding to your desired function.")
        print("'c' to check another machine's blockchain.")
        print("'x' to exit admin screen.")
        print('================================================================')
        userInput = input("")

        if(userInput == 'x'):
            return
        if(userInput == 'c'):
            while True:
                port = input("Please type the port number of the machine you're trying to check (ports start at 9000 for checks): ")
                try:
                    port = int(port)
                    break
                except:
                    print("that was not an acceptable integer.")
                    continue
            newBlockchain = getBlockchainFromMachine(port, 9020)
            if newBlockchain:
                result = checkOtherMachineBlockchain(newBlockchain)
                if(result == 1):
                    print("Blockchains match.")
                    continue
                else:
                    print("Blockchains do not match.")
                    continue
            else:
                print("something went wrong.")
                continue
        else:
            print("That character was not accepted.  Please try again.")
            input("please press enter to continue")
            print("")
            continue
