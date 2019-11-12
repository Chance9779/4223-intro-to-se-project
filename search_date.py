from blockchain import *
import datetime
import json
from transaction import *

# search blockchain by date
# takes in start and end string in the following format:
#   "year-month-day"
def search_date(start, end):

    # open blockchain file, grab contents as string
    file = open("blockchain.txt", "r");
    fileContents = file.read()

    # turn it into a python object
    fileContents = json.loads(fileContents)

    # turn start and end dates into datetime objects
    datetime.strptime(start, "%Y-%m-%d")
    datetime.strptime(end, "%Y-%m-%d")

    # storage for results
    results = []

    # checks to see if the blockchain is empty before searching
    if fileContents:

        # loop through blockchain
        for i in range(len(fileContents)):

            # keep track of current block
            current = fileContents[i]
            currentDatetime = current["datetime"]

            # check if the block is between start and end date
            if currentDatetime >= start && currentDatetime <= end:
                results.append(current)

        return results

    else:
        print("ERROR: There are currently no transactions stored.")
        return None
