#WG_CP2 Login
#import helper 
from helper import *
clear_screen()

#A function to check if something exists
def exists(location, search):
    try:
        with open(location, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                # skip empty lines
                if row and row[0] == search:
                    return True
    except FileNotFoundError:
        print("file does not exist.")
    except Exception:
        # fallback for unexpected errors
        print("error reading file")
    return False

def add_user(username: str, hashed: str) -> None:

    with open("documents/user.json", "a", newline="") as f:
        #bracken put his code in  here
        print()

#define a function that allows for the creation of the account using the already exists checker to check for the user name already exists if so make them use a diffrent username
def create_account():
    # clear screen here
    clear_screen()

    while True:
        name = input("Choose a username: ").strip()

        if not name:
            print("Username cannot be blank.")
            continue

        if exists("documents/user.json",name):
            print("That username is unavailable.")
            continue

        pw = input("Choose a password (12+ chars, upper, lower, digit, special): ")
        add_user(name, hash_pw(pw))
        print("Account created.")
        break
    
    #get their password
    
    #hash their password and save its value

#A function that reads the whole json

#define a function that edits the account json adding accounts to the user json
    
    #Open the file in append mode
    
    #Use dictwriter to set the field names their username and their hashed password
    
    #write to the file their name password hashed and gaol and progress 

#A function to encrypt saved passwords with the hashlib library using a specific encryption  this is in helper library

def login(poker_scores,blackjack_scores,slots_scores):
    users = parse_user()
    name = input("What is your username? ").strip()
    pw = input("What is your password? ")
    hashed = hash_pw(pw)

    for u in users:

        if u["username"] == name and u["password"] == hashed:
            print("Login successful.")
            clear_wait_screen()
            clear_screen()
            menu(name)
            return
    print("Invalid username or password.")

#A function that gets their gaol and saves it
def gaol_get(user):
    gaol = input(f"{user} what do you want to set your gaol too?").strip()
    return gaol

def update_gaol(user):
    gaol_get(user)
    add_user()



#A function that takes in their previous progress towards their gaol, and then asks how much more money they have added, and updates the progress.
def new_gaol_progress(user):
    progress = input(f"What progress have you made towards your gaol? ").strip()
    #Do the thing where you add the progress to the json

#A function that logs them out and takes them back to the main menu without them being logged in.
def logout():
    menu("Not exists")