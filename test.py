from blockchain import *
from driver import *
from receiver import *
import datetime
import json
from threading import Thread
from transaction import *
from searchById import *
from search_date import *
from sender import *

import os

import time

newTransaction = transaction(3)
newTransaction.setTransaction()
newBlock = newTransaction.makeBlock()

#now let's send it through the pipeline
sendUpdate(newBlock)