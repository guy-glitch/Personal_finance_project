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
        #get the time
        #go into budget input that amount and have the money distributed by the percentages of the catigories
        #formate that info and save it to the user profile with the save function(made by Braken)
    #else if they choose expense
        #ask how much they spent
        #ask from which budget catigory they will take from
        #make sure that catigory exists otherwise they have to choose again
        #get the time 
        #save all that information to the user account
        #go into the budget info and subtract the amount from the specified catigory
    #else if they choose to quit
        #exit the function

#budgeting function
#parameters:user profile info
    #create a menu that has the option to view, change, or quit
    #if they choose to view
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



