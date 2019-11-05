from blockchain import *
from driver import * 
import datetime
import json

#just a test file to see if functions and such are working

block = createBlock(datetime.datetime.now(), "this is our data", "fdfd;aksd202101012e3")

block = Block(block)
hashThing = block.hashThisBlock() 
print(block)
print("HASH: ", hashThing)
