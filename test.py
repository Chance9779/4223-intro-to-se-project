from blockchain import *
from driver import * 
from receiver import *
import datetime
import json
from threading import Thread

import os

import time

 

# class defining Daemon Thread

class DaemonThread(Thread):

 

    # Daemon Thread constructor

    def __init__(self):

        Thread.__init__(self)

 

    # Daemon Thread run method

    def run(self):

        #listen for another machine
        while True:
            try:
                update = startListening()
                updateBlockchain(update)
                continue #continue this infinitely
            except:
                print("Something went wrong receiving. Closing")
                exit()
 

# Main thread

aDaemonThread = DaemonThread()

aDaemonThread.daemon = True

aDaemonThread.start()
for i in range(1,2):
    print("My Daemon will take care")
    time.sleep(10) 


