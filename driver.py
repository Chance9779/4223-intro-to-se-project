"""
this is our driver file.

this will be used to grab the blockchain and all of its blocks
from the blockchain.txt file.  

"""

import json

#open our file
file = open("blockchain.txt", 'r')

#grab the json from the file
fileContents = file.read()

#this converts the blockchain from JSON
def fromJSON():
    blockList = json.loads(fileContents)
    return blockList

#this converts whatever to JSON
def toJSON(content):
    content = json.dumps(content)
    return content

#close the file
file.close()
