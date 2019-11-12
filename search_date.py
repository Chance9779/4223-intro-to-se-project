from blockchain import *
from datetime import *
import json
from transaction import *
from searchById import *

# search blockchain by date
# takes in start and end string in the following format:
#   "year-month-day"
def searchByDate(start, end):

    # open blockchain file, grab contents as string
    file = open("blockchain.txt", "r");
    fileContents = file.read()

    # turn it into a python object
    fileContents = json.loads(fileContents)

    # turn start and end dates into datetime objects
    #datetime.strptime(start, "%Y-%m-%d")
    #datetime.strptime(end, "%Y-%m-%d")
    print("start date: ", start, "type: ", type(start))
    print("end date", end, "type: ", type(end))

    # storage for results
    results = []

    # checks to see if the blockchain is empty before searching
    if fileContents:

        # loop through blockchain
        for i in range(len(fileContents)):

            # keep track of current block
            current = fileContents[i]
            currentDatetime = current["datetime"]

            #print("current datetime: ", currentDatetime)
            #change the current date time to a date
            currentDatetime = datetime.datetime.strptime(currentDatetime, '%b %d %Y %I:%M%p')
            #print("GOT HERE: ", currentDatetime)
            #make currentDateTime a date
            currentDatetime = currentDatetime.date()
            # check if the block is between start and end date
            if (currentDatetime >= start and currentDatetime <= end):
                results.append(current)

        return results

    else:
        print("ERROR: There are currently no transactions stored.")
        return None

#get our start and end date values and try to search
def searchByDateInterface():
    #infinite loop
    while(True):
        print("Please enter the dates you wish to search through as listed below.  (press enter to continue or type 0 to leave)")
        check = input("")
        if (check == "0"):
            return None
        print("\n")

        try:
            d1, m1, y1 = [int(x) for x in input("Enter start"
                " date(DD/MM/YYYY) : ").split('/')] 
            start = date(y1, m1, d1)
            print("start: ", start)
    
            # Input for second date 
            d2, m2, y2 = [int(x) for x in input("Enter finish"
                "date(DD/MM/YYYY) : ").split('/')] 

            
            end = date(y2, m2, d2) 
        
            #let's try to search by date
            try:
                results = searchByDate(start, end)
                viewSearch(results)
                return None
            except:
                print("something went wrong.")
                continue
        
        except:
            print("Make sure dates are of the format (Year-Month-Day) and try again")
            print("\n")


