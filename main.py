import sys
import fileinput

#login
def login():
    print("Welcome to the Event Ticketing System!")
    username = input("To login, please enter your username: ")
    #if username is valid: 
    print("Welcome " + username)
    options()

    #else print error message

#logout
def logout():
    print("Goodbye")

#buy   
def buy():
    print("How many tickets do you want to buy?: ")

#session type
def options():
    session = input("Enter session type: ")
    if session == "buy":
        buy()
    
    elif session == "logout":
        logout()
    else:
        print("Please enter a valid session type or type logout")
        options()


#main
login()
