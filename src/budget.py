#This will contain all the necessary code for the budgeting aspect of this project

#Pseudocode
from helper import *
from datetime import datetime
#Classes
#income class
class Income():
    #initiate amount and source
    def __init__(self, amount, source, user):
        self.amount = amount
        self.source = source
        self.user = user
    #string
    def __str__(self):
        #formate the amount, source and time from the time function
        return f"""Income Input:
        Amount: {self.amount}
Source: {self.source}
Time:{self.time()}"""
    #add to user history
    def add_history(self):
        #take in all the info
        #formate it
        add = f"{self.amount}|{self.source}|{self.time()}"
        #add to user history
    #update budget
        #get the current bugdet of the user
        #add the amount to the total
        #the budget will divide it amoung the sections
    def time(self):
        now = datetime.now() 
        #formatted time is the time in the correct formate
        formatted_time = now.strftime("%B %d, %Y at %I:%M %p")
        #return formatted time
        return formatted_time

#expense class
    #initiate amount
    #string
        #formate this info to print
    #formate
        #formate the info to input into the user profile
    #time
        #get the time
        #formate it
        #return it
    #catigory validation
        #go to the user profile and get the catigories
        #start while loop
            #show all the catiogories
            #ask user to choose one
            #if it is actually a catigory 
                #return that
            #else it isn't
                #restart loop and go again

#income and expense tracking
def income_expense(profile_info):
#parameters:user profile info
    #show the menu of options including view, income, expense, or quit(Braken helper function)
    choice = list_choice(["view", "income","expense","quit"], prompt="Choose one of the following actions to complete:")
    #if they choose view
    if choice == "view":
        #get their infomation and input it into the graph function(made by levi)
        #display the graph
        pass
    #else if they choose income
    elif choice == "income":
        #ask how much they got
        amount = int_input(prompt="Please enter the amount of money you are inputing: ")
        #ask for the source
        source = input("Please input the source of the money: ")
        #call the income class and formate this info to save
        income_input = Income(amount,source,profile_info)
        #go into budget input that amount and have the money distributed by the percentages of the catigories
        #formate that info and save it to the user profile with the save function(made by Braken)
    #else if they choose expense
        #ask how much they spent
        #call the expense class
        #save all that information to the user account
        #go into the budget info and subtract the amount from the specified catigory
    #else if they choose to quit
        #exit the function

#budgeting function
#parameters:user profile info
    #create a menu that has the option to view, change, or quit
    #if they choose to view
        #get dictionary of user values to use in the graph
        #display the graph with the display function(Levi)
    #else if they choose to change
        #ask if they would like to change the percentages or the catigories
        #if they choose percentages
            #then tell them what all the catigories are currently and their percentages
            #go through each of the catigories and ask for the new percentage
            #make sure they don't go over 100 percent
        #else if they choose catigories
            #ask if they would like to add or remove a catigory
                #display all current catigories 
                #if they choose remove 
                    #ask which they would like to remove 
                    #remove it
                    #go through the same process of changing percentages as when changing percentages above
                #else if they choose to add
                    #ask for the name of the new catigory
                    #add it
                    #go through the same process of changing percentages as when changing percentages above
                #else make them choose again and tell them int was an invalid choice
        #else make them choose again and tell them int was an invalid choice
    #else if they choose to quit
        #exit the function
    #else make them choose again and tell them int was an invalid choice






