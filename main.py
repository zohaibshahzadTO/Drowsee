import sys
import fileinput


#initalize valid users
users = [["sarah","admin", 1000.00],["sylvie","buy-standard", 2000.00],["zohaib","full-standard", 3000.00]]

#daily transaction file
f = open("dailyfile.txt", "w")
#MISCELLANEOUS FUNCTIONS:

#returns index where user shows up in 2d array
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i

def check_current_user(x):
    if x in [i[0] for i in users]:
        return True
    else:
        return False

def check_valid_accountType(x):
    if x != "admin" or "full-standard" or "buy-standard" or "sell-standard":
        return False

#login
def login():
    print("Welcome to the Event Ticketing System!")

    username = input("To login, please enter your username: ")
    #Check if username is in the database
    if username in [i[0] for i in users]:
        #if username is valid:
        print("Welcome " + username)
        #get the index of where they appear in the list
        index = index_2d(users, username)
        #pass arg of valid session types for user
        options(users[index][1], username)

    #else print error message
    else:
        print("Invalid: User does not exist")
        login()

#logout
def logout():
    print("Goodbye")
    f.close()

# Create a User
def createUser(x, y):
    if x == "admin":
        startingCredit = 100.00
        newUser = input('Please enter the username for this new account: ')

        while(check_current_user(newUser)):
                newUser = input("Please enter a username that isn't already taken: ")
                check_current_user(newUser)

        index = index_2d(users, newUser)

        print("""Choose an option:
        - admin
        - full-standard
        - buy-standard
        - sell-standard
        """)
        accountType = input('Now tell us the type of user for this account (see above for valid user types): ')

        while(check_valid_accountType(accountType)):
            print("""Choose an option:
            - admin
            - full-standard
            - buy-standard
            - sell-standard
            """)
            accountType = input('Please enter a valid account type for this new user (see above for options): ')


        # add user name and user type into users list
        users.append([newUser, accountType, startingCredit])
        print(users)

        # Write to file
        f.write("02" + " " + newUser + " " + accountType + " " + str(float(startingCredit)) + "\n")

        # New user created
        print("New user created successfully!")
        options(x, y)
    else:
        print("Permission Denied")
        options(x, y)

#buy
def buy(x,y):
    #check if transaction is valid for user
    if x == "admin" or x == "buy-standard" or x == "full-standard":
        tickets = input("How many tickets do you want to buy?: ")


#sell
def sell(x,y):
    #check if transaction is valid for user
    if x == "admin" or x == "sell-standard" or x == "full-standard":
        title = input("Please enter event title: ")
        #check if event title is within 25 chars
        while(len(title) > 25):
            print("Error: Event title cannot exceed 25 characters")
            title = input("Please enter event title (25 chars or less): ")

        #check if quantity is not over 100
        quantity = input("Quantity of tickets: ")
        while(not int(quantity) or int(quantity) > 100):
            print("Error: Ticket quantity must be 100 or less.")
            quantity = input("Please enter valid quantity of tickets: ")

        #check if amount per ticket is less than 1000 (need to fix: check if int or float, valid float)
        perTicket = input("How much would you like to charge (per ticket)?: ")
        #while(not float(perTicket) or not int(perTicket)):
            #perTicket = input("Please enter a valid amount (less than 1000): ")

        sellerIndex = index_2d(users, x)
        #write to file
        f.write("03 "+ title + " " + y + " " + quantity + " " + str(users[sellerIndex][2]) + "\n")
        print("Successfully put tickets for sale!")
        options(x,y)

    else:
        print("Permission Denied")
        options(x,y)


#refund
def refund(x,y):
    if x == "admin":
        buyer = input("Enter BUYER'S username: ")
        while(not check_current_user(buyer)):
            buyer = input("Please enter a valid username: ")
            check_current_user(buyer)
        buyerIndex = index_2d(users, buyer)

        seller = input("Enter SELLER'S username: ")
        while(not check_current_user(seller)):
            seller = input("Please enter a valid username: ")
            check_current_user(seller)

        sellerIndex = index_2d(users, seller)

        credit = input("Enter amount of credit to refund: ")
        while (not float(credit)):
            credit = input("Enter a valid amount of credit to refund: ")

        #do the refund
        #new buyer balance
        users[buyerIndex][2] = users[buyerIndex][2] + float(credit)

        #new seller balance
        users[sellerIndex][2] = users[sellerIndex][2] - float(credit)

        #write to file
        f.write("05 "+ users[buyerIndex][0]+ " " + users[sellerIndex][0] + " " + str(float(credit)) +"\n")
        print("Refund successful!")
        options(x,y)
    else:
        print("Permission denied")
        options(x,y)


#add credit
def addCredit(x, y):
    if x == "admin":
        userName = input("Enter username to add credit to: ")
        while(not check_current_user(userName)):
            userName = input("Please enter a valid username to add credit to: ")
            check_current_user(userName)

        index = index_2d(users, userName)

        credit = input("Enter amount of credit to add: ")
        while (not float(credit)):
            credit = input("Enter a valid amount of credit to add: ")

        while (float(credit) > 1000.00):
            print("Amount must not be more than $1000.00")
            credit = input("Enter amount of credit to add: ")

        #add the credit
        users[index][2] = users[index][2] + float(credit)

        #write to file
        f.write("06 " + users[index][0] + " AA " + str(float(credit))+ "\n")

        #success
        print("Credit added successfully!")
        options(x,y)

    elif x == "full-standard":
        credit = input("Enter amount of credit to add: ")
        while (float(credit) > 1000.00):
            print("Amount must not be more than $1000.00")
            credit = input("Enter amount of credit to add: ")

        #add the credit
        index = index_2d(users, y)
        users[index][2] = users[index][2] + float(credit)
        #wrtie to file
        f.write("06 " + y + " FS " + str(float(credit)))
        print("Credit added successfully!")
        options(x,y)
    else:
        print("Permission denied")
        options(x,y)

#session type
def options(x, y):
    #initialize variables
    userType = x
    userName = y
    #check what type of user they are to determine valid transaction items
    if userType == "admin":
        transactionItems = ["buy", "create", "sell", "addcredit","logout","delete","refund"]
    elif userType == "full-standard":
        transactionItems = ["buy", "sell", "addcredit", "logout"]
    elif userType == "buy-standard":
        transactionItems = ["buy","logout"]
    else:
        transactionItems = ["sell","logout"]


    session = input("Enter session type [" + "/".join(transactionItems) + "]: ")

    if session == "buy":
        buy(x,y)

    elif session == "sell":
        sell(x,y)

    elif session == "logout":
        logout()

    elif session == "create":
        createUser(userType, userName)

    elif session == "refund":
        refund(userType)

    elif session == "addcredit":
        addCredit(userType, userName)

    else:
        print("Please enter a valid session type or type logout")
        options(userType)


#main
login()
