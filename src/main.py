#main function

#import absolutely everything
import graphics,login,helper,budget

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
            if graphics.Menu(['Login','Create Account'])=='Login':
                user=login.login()
            else:
                user=login.create_account()
                helper.json_dump(info.update({user:{'history':{'income':[],'expenses':[]},'categories':{},'goal':[0,0]}}))
            #loop
            while True:
                #get user input for manage income/expenses, create savings goal, update savings goal, budget, and log out
                choice=graphics.Menu(['Manage Income/expenses','Create Savings Goal','Update Savings Goal','Budget','Logout'])
                #if manage incom/expenses
                if choice=='Manage Income/expenses':
                    #call incom/expense tracking function(anna)
                    info[user]=budget.income_expense(info[user])
                #else if create savings goal
                elif choice=='Create Savings Goal':
                    #call set goal function(warren)
                    info[user]['goal']=login.goal_get()
                #else if update savings goal
                elif choice=='Update Savings Goal':
                    #call goal update function(warren)
                    info[user]['goal']=login.new_goal_progress(info[user]['goal'])
                #else if budget
                elif choice=='Budget':
                    #call budgeting function(anna)
                    pass
                #else
                else:
                    #break out of loop
                    break
        #else
            #break out of loop
    #call save to JSON function
    helper.json_dump('documents/user_info.json',info)

main()