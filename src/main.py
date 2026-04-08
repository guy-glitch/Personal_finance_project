#main function

#import absolutely everything
import graphics,login

#create function main
def main():
    #loop
    while True:
        #get user input for login/create account or exit
        if graphics.Menu(['Login/Create Account','Exit']).use()=='Exit':
            break
        #if login/create account
        else:
            #call retrieve info JSON function(bracken)
            #call login function(warren)
            if graphics.Menu(['Login','Create Account']).use()=='Login':
                user=login.login()
            else:
                user=login.create_account()
            #loop
            while True:
                #get user input for manage income/expenses, create savings goal, update savings goal, budget, and log out
                choice=graphics.Menu(['Manage Income/Expenses','Create Savings Goal','Update Savings Goal','Budget','Logout']).use()
                #if manage incom/expenses
                if choice=='Manage Income/Expenses':
                    #call incom/expense tracking function(anna)
                #else if create savings goal
                elif choice=='Create Savings Goal':
                    #call set goal function(warren)
                #else if update savings goal
                elif choice=='Update Savings Goal'
                    #call goal update function(warren)
                #else if budget
                elif choice=='Budget':
                    #call budgeting function(anna)
                #else
                else:
                    #break out of loop
                    break
        #else
            #break out of loop
    #call save to JSON function

