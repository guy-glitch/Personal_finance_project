#WG_CP2 Login
#import helper 
from helper import *
import graphics
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
        graphics.show("file does not exist.")
    except Exception:
        # fallback for unexpected errors
        graphics.show("error reading file")
    return False

def add_user(username: str, hashed: str) -> None:
    #if this recieves a username that already is stored it will overwrite it with the hashed password provided.
    users = json_pull('documents/user.json')
    users[username] = hashed
    json_dump('documents/user.json',users)

#define a function that allows for the creation of the account using the already exists checker to check for the user name already exists if so make them use a diffrent username
def create_account():
    # clear screen here
    clear_screen()

    while True:
        name = graphics.inputs("Choose a username: ").strip()

        if not name:
            graphics.show("Username cannot be blank.")
            continue

        if exists("documents/user.json",name):
            graphics.show("That username is unavailable.")
            continue

        pw = graphics.inputs("Choose a password (12+ chars, upper, lower, digit, special): ")
        add_user(name, hash_pw(pw))
        graphics.show("Account created.")
        break
    
    #get their password
    
    #hash their password and save its value

#A function that reads the whole json

#define a function that edits the account json adding accounts to the user json
    
    #Open the file in append mode
    
    #Use dictwriter to set the field names their username and their hashed password
    
    #write to the file their name password hashed and goal and progress 

#A function to encrypt saved passwords with the hashlib library using a specific encryption  this is in helper library

def login():
    while True:
        users = json_pull('documents/user.json')
        name = graphics.inputs("What is your username? ").strip()
        pw = graphics.inputs("What is your password? ")
        hashed = hash_pw(pw)

        for u in users.keys():

            if u == name and users[u] == hashed:
                graphics.show("Login successful.")
                clear_wait_screen()
                clear_screen()
                return 
        graphics.show("Invalid username or password.")

#A function that gets their goal and saves it
def goal_get():
    goal = graphics.inputs(f"What do you want to set your goal too?").strip()
    return [goal, 0]

def update_goal(user):
    goal_get(user)
    add_user()



#A function that takes in their previous progress towards their goal, and then asks how much more money they have added, and updates the progress.
def new_goal_progress(goal):
    progress = graphics.inputs(f"What progress have you made towards your goal? ").strip()
    new_progress = progress + goal[1]
    return [goal[0], new_progress]
    #Do the thing where you add the progress to the json

#A function that logs them out and takes them back to the main menu without them being logged in.
def logout(): 
    return 

goal_get()