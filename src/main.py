#main function

#import absolutely everything
import graphics,login,helper,budget,currency

#dict={char:{history:{income:[income values],expenses:[expense values]},categories:{category:value},goal:[goal,progress]}}

#create function main
def main():
    #call retrieve info JSON function(bracken)
    info=helper.json_pull('documents/user_info.json')
    #loop
    while True:
        #get user input for login/create account or exit
        if graphics.Menu(['Login/Create Account','Exit']).use()=='Exit':
            break
        #if login/create account
        else:
            #call login function(warren)
            if graphics.Menu(['Login','Create Account']).use()=='Login':
                user=login.login()
            else:
                user=login.create_account()
                info[user] = {'income history':[],'expense history':[],'categories':{},'goal':[0,0]}
                helper.json_dump('documents/user_info.json',info)
            #loop
            while True:
                #get user input for manage income/expenses, create savings goal, update savings goal, budget, and log out
                choice=graphics.Menu(['Manage Income/expenses','Create Savings Goal','Show Savings Goal','Update Savings Goal','Budget','Convert Currencies','Logout']).use()
                #if manage incom/expenses
                if choice=='Manage Income/expenses':
                    #call incom/expense tracking function(anna)
                    info[user]=budget.income_expense(info[user])
                #else if create savings goal
                elif choice=='Create Savings Goal':
                    #call set goal function(warren)
                    info[user]['goal']=login.goal_get()
                elif choice=='Show Savings Goal':
                    try:
                        graphics.show(f'Goal: {info[user]['goal'][0]}\nProgress: {info[user]['goal'][1]}\nPercent: {100*info[user]['goal'][1]/info[user]['goal'][0]}%')
                    except:
                        graphics.show('Error: no goal set')
                #else if update savings goal
                elif choice=='Update Savings Goal':
                    #call goal update function(warren)
                    info[user]['goal']=login.new_goal_progress(info[user]['goal'])
                #else if budget
                elif choice=='Budget':
                    #call budgeting function(anna)
                    budget.budgeting(user)
                elif choice=='Convert Currencies':
                    choic=graphics.Menu(['USD to EUR','USD to JPY','USD to GBP','EUR to USD','JPY to USD','GBP to USD']).use()
                    choic=['USD to EUR','USD to JPY','USD to GBP','EUR to USD','JPY to USD','GBP to USD'].index(choic)+1
                    currency.casing(choic)
                #else
                else:
                    #break out of loop
                    break
        #else
            #break out of loop
    #call save to JSON function
    helper.json_dump('documents/user_info.json',info)

main()