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
from checkHash import *

import os

import time

newBlockchain = startListeningForChecks()
#print("got blockchain: ", newBlockchain)
checkOtherMachineBlockchain(newBlockchain)