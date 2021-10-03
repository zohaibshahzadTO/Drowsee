import sys
import fileinput

#login
def login():
    #initalize valid users
    users = [["sarah","admin"],["sylvie","buy-standard"],["zohaib","full-standard"]]
    print("Welcome to the Event Ticketing System!")
    username = input("To login, please enter your username: ")
    #Check if username is in the database
    if username in [i[0] for i in users]:
        #if username is valid: 
        print("Welcome " + username)
        #get the index of where they appear in the list
        index = index_2d(users, username)
        #pass arg of valid session types for user
        options(users[index][1])

    #else print error message


#logout
def logout():
    print("Goodbye")

#buy   
def buy():
    print("How many tickets do you want to buy?: ")


#sell
def sell():

    print("")

#session type
def options(x):
    #initialize variables
    userType = x

    #check what type of user they are to determine valid transaction items
    if userType == "admin":
        transactionItems = ["buy", "create", "sell", "addcredit","logout","delete","refund"]
    elif userType == "full-standard":
        transactionItems = ["buy", "sell", "logout"]
    elif userType == "buy-standard":
        transactionItems = ["buy","logout"]
    else:
        transactionItems = ["sell","logout"]
    

    session = input("Enter session type [" + "/".join(transactionItems) + "]: ")

    if session == "buy":
        buy()
    
    elif session == "logout":
        logout()
    else:
        print("Please enter a valid session type or type logout")
        options()


#main
login()


#MISCELLANEOUS FUNCTIONS:

#returns index where user shows up in 2d array
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i
