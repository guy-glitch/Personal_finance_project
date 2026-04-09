#main function

#import absolutely everything
import graphics,login,helper

#dict={char:{history:{income:[income values],expenses:[expense values]},categories:{category:value},goal:[goal,progress]}}

#create function main
def main():
    #call retrieve info JSON function(bracken)
    info=helper.json_pull('documents/user_info.json')
    #loop
    while True:
        #get user input for login/create account or exit
        if graphics.Menu(['Login/Create Account','Exit'])=='Exit':
            break
        #if login/create account
        else:
            #call login function(warren)
            login.
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
    helper.json_dump('documents/user_info.json',info)

