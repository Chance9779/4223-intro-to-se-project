import socket 
import sys
import json  

#gotta send a block of data please
def sendUpdate(block):
        
    # Create the socket
    s = socket.socket()          
    
    # our port number 
    port = 8000         
    
    # connect to the listener
    s.connect(('127.0.0.1', port)) 

    #remember, we'll be getting a block.  We need to convert it to json
    block = json.dumps(block)
    # receive data from the server 
    s.send(block.encode())
    print("sent contents. Closing")
    # close the connection 
    s.close()   


#this port will only be used when getting the blockchain
#this port will be 902(whatever)
def getBlockchainFromMachine(port, me):
    try:
        # Create the socket
        s = socket.socket()          
        
        # our port number 
        port = port

        #port we want the machine to send the stuff to
        ourMachinesPort = me        
        
        # connect to the listener
        try:
            s.connect(('127.0.0.1', port))
        except:
            print("That port is not running currently.")
            return None 

        #send the ack that you wanna check it
        content = ourMachinesPort
        content = str(content) #send it as a string.  The other
        #machine will grab it as a string and decode it
        s.send(content.encode())

        s.close()

        # Create the socket again on our port number to listen
        s = socket.socket()          

        #port we want the machine to send the stuff to
        port = ourMachinesPort     
        
        while True:
            print("TRYING ON: ", port)
            # connect to the listener
            try:
                s.bind(('', ourMachinesPort)) #bind the socket to the port
                break
            except:
                continue

        newBlockchain = [] #this is a buffer to store the receiving dicts in

        #the other machine will send multiple dictionaries until it sends an
        #end which will be the string "0"

        while True:
            s.listen(5) #listen for others on the network
            c, addr = s.accept() #accept a connection from the machine
            
            #receive the information from another machine
            while True:
                content = c.recv(1023) #max size of the thing
                #print("received: ", content.decode())

                content = content.decode() #decode to something we can actually use.
                #Remember, this will be returned as a string
                #print("GOT: ", content)
                if(not content):
                    #we got to the end. break
                    #print("GOT EVERYTHING.  Leaving")
                    break
                
                #this will be a json object, throw it into the newBlockchain
                #print("CONTENT: ", content)
                content = json.loads(content)
                newBlockchain.append(content) 

            
            s.close() #close the socket
            return newBlockchain #will return the whole blockchain
    except:
        print("something went wrong. please try again.")
        return []