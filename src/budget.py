#This will contain all the necessary code for the budgeting aspect of this project

#Pseudocode
from helper import *
from datetime import datetime
from graphics import *
#Classes
#income class
class Income():
    #initiate amount and source
    def __init__(self, amount, source, user):
        self.amount = amount
        self.source = source
        self.user = user
    #string
    def add_history(self):
        #take in all the info
        #formate it
        add = f"{self.amount}|{self.source}|{self.time()}"
        #add to user history
        self.user["income history"].append(add)
        return self.user
    
    def update_amount(self):
        for i in self.user["catigories"].keys():
            value = self.user["catigories"][i].get()
            v = value[1]/100
            v_2 = self.amount*v
            self.user["catigories"][i] += v_2
        return self.user
    def time(self):
        now = datetime.now() 
        #formatted time is the time in the correct formate
        formatted_time = now.strftime("%B %d, %Y")
        #return formatted time
        return formatted_time

#expense class
class Expense():
    #initiate amount
    def __init__(self,amount, user):
        self.amount = -1*amount
        self.user = user
    #string
    def add_history(self):
        #take in all the info
        #formate it
        catigori = self.catigory()
        add = f"{self.amount}|{catigori}|{self.time()}"
        #add to user history
        self.update_amount(catigori)
        self.user["expense history"].append(add)
        return self.user
    #time
    def update_amount(self,catigory):
        self.user["catigories"][catigory] -= self.amount
        return self.user
    def time(self):
        now = datetime.now() 
        #formatted time is the time in the correct formate
        formatted_time = now.strftime("%B %d, %Y")
        #return formatted time
        return formatted_time
    #catigory validation
    def catigory(self):
        #go to the user profile and get the catigories
        catigories = self.user["catigories"]
        #start while loop
        while True:
            #show all the catiogories
            choice = list_choice(catigories.keys(), prompt="Choose a catigory you would like to withdraw money from:")
            #ask user to choose one
            #if it is actually a catigory
            if choice in catigories: 
                #return that
                return choice
            #else it isn't
            else:
                print("That was an invalid choice of catigory choose again")
                #restart loop and go again

def float_validation(message):
    while True:
        amount = inputs(question=message)
        try:
            float(amount)
            break
        except ValueError:
            show("That is an invalid input. It must be a number")
    return amount

#income and expense tracking
def income_expense(profile_info):
#parameters:user profile info
    #show the menu of options including view, income, expense, or quit(Braken helper function)
    menu = Menu(["view","income","expense","quit"])
    choice = menu.use()
    #if they choose view
    if choice == "view":
        #get their infomation and input it into the graph function(made by levi)
        #display the graph
        y_line = "Input Instance"
        title = "INCOME AND EXPENSES OVER TIME"
        line_graph = Line(profile_info["income history"],profile_info["expense history"],y_line,title)
        line_graph.show()
    #else if they choose income
    elif choice == "income":
        #ask how much they got
        amount = float_validation("Please input the amount of money you are inputing:")
        #ask for the source
        source = inputs("Please input the source of the money: ")
        #call the income class and formate this info to save
        income_input = Income(amount,source,profile_info)
        #go into budget input that amount and have the money distributed by the percentages of the catigories
        profile_info = income_input.add_history()
        #formate that info and save it to the user profile with the save function(made by Braken)
    #else if they choose expense
    elif choice == "expense":
        #ask how much they spent
        spent = float_validation("Enter the amount of money you spent:")
        #call the expense class
        expense_case = Expense(spent, profile_info)
        #save all that information to the user account
        profile_info = expense_case.add_history()
        #go into the budget info and subtract the amount from the specified catigory
    #else if they choose to quit
    elif choice == "quit":
        #exit the function
        pass

#function to go through all the catigories and get the new percentages for each
def percent_change(user):
    #then tell them what all the catigories are currently and their percentages
            for key in user["catigories"].keys():
                show(f"{key}: {user["catigories"][key]}")
            #go through each of the catigories and ask for the new percentage
            while True:
                sum_total = 0
                for key in user["catigories"].keys():
                    sum_total += user['catigories'][key][0] 
                total = 0
                for key in user["catigories"].keys():
                   show(key.title())
                   new_perc = float_validation("Input the new a percentage for this catigory:") 
                   user["catigories"][key][1] = new_perc
                   total += new_perc
                #make sure they don't go over 100 percent
                if total == 100:
                    break
                else:
                    show("Sorry you went over or under 100% percent please go through it again and allocate the percentages correctly.")

#budgeting function
def budgeting(user):
#parameters:user profile info
    #create a menu that has the option to view, change, or quit
    choice = Menu(["view","change","quit"])
    #if they choose to view
    if choice == "view":
        #get dictionary of user values to use in the graph
        #display the graph with the display function(Levi)
        new_dict = {}
        for key in user["catigories"].keys():
            new_dict[key] = user["catigories"][key][0]
        bar_graph = Bars(new_dict,"Amount of money","BUDGET MONEY ALLOCATION")
    #else if they choose to change
    elif choice == "change":
        #ask if they would like to change the percentages or the catigories
        choice_2 = Menu(["percent","catigory"])
        #if they choose percentages
        if choice_2 == "percent":
            percent_change(user)
        #else if they choose catigories
        elif choice == "catigory":
            #ask if they would like to add or remove a catigory
            choice_3 = Menu(["add","remove"])
            #display all current catigories 
            #if they choose remove 
            if choice_3 == "remove":
                    #ask which they would like to remove 
                    choice_4 = Menu(user["catigories"].keys())
                    #remove it
                    user["catigories"].pop(choice_4)
                    #go through the same process of changing percentages as when changing percentages above
                    percent_change(user)
            #else if they choose to add
            elif choice_4 == "add":
                #ask for the name of the new catigory
                name = inputs("Input the name of the new catigory: ")
                #add it
                user["catigory"][name] = [0,0]
                #go through the same process of changing percentages as when changing percentages above
                #else make them choose again and tell them int was an invalid choice
                percent_change(user)
        #else make them choose again and tell them int was an invalid choice
    #else if they choose to quit
    elif choice == "quit":
        #exit the function
        pass

practice_dict = {"expense history": [],
                 "income history": [],
                 "catigories": {"starter":[0,100]}}
income_expense(practice_dict)




