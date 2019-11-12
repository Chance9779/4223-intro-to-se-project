from blockchain import *
from driver import *
from receiver import *
import datetime
import json
from threading import Thread
from transaction import *
from searchById import *

import os

import time

""" newTransaction = transaction(1)
newTransaction.setTransaction()
newBlock = newTransaction.makeBlock()
print(newBlock)
updateBlockchain(newBlock) """

search = searchByStoreId(1)
viewSearch(search)