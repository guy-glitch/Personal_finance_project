#main function

#import absolutely everything

#create function main
    #loop
        #get user input for login/create account or exit
        #if login/create account
            #call retrieve info JSON function(bracken)
            #call login function(warren)
            #loop
                #get user input for manage income/expenses, create savings goal, update savings goal, budget, and log out
                #if manage incom/expenses
                    #call incom/expense tracking function(anna)
                #else if create savings goal
                    #call set goal function(warren)
                #else if update savings goal
                    #call goal update function(warren)
                #else if budget
                    #call budgeting function(anna)
                #else
                    #break out of loop
        #else
            #break out of loop
    #call save to JSON function