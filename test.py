from blockchain import *
from driver import * 
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

        for i in range(1,10):

            print("I am the daemon thread. I keep on running bg...hehe")

            time.sleep(2)

 

# Main thread

aDaemonThread = DaemonThread()

aDaemonThread.daemon = True

aDaemonThread.start()
for i in range(1,10):
    print("My Daemon will take care")