""" /*
This is a blockchain.  Blocks in a blockchain hold a datetime stamp, the data in question, and a hash
of the PREVIOUS block's datetime + data

We're gonna hold our blockchain in a txt file on the machine.  This is gonna be a list of dictionaries 
that's converted to a JSON string to hold it.  When we need it, we'll just pull it out of JSON format from the txt file.

Storing it in a txt file allows us to hold the txt file on seperate machines.  Each machine will have its own
txt file and every time a block is added from one machine, it will send the new dictionary to the other
machines txt files.

In terms of security, we will define a function that checks the hashes of all blocks and makes sure
that there hasn't been any tampering with the blockchain in any way.

*/
 """

class Blockchain:
    blockchain = []
    