#This will contain all the necessary code for the budgeting aspect of this project

#Pseudocode

#income and expense tracking
#parameters:user profile info
    #show the menu of options including view, income, expense, or quit(Braken helper function)
    #if they choose view
        #get their infomation and input it into the graph function(made by levi)
        #display the graph
    #else if they choose income
        #ask how much they got
        #ask for the source
        #call the income class and formate this info to save
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


#Classes
#income class
    #initiate amount and source
    #string
        #formate the amount, source and time from the time function
    #time
        #get the time
        #formate it
        #return it

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



