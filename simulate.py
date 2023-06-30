# import personalPrototype as personal
# Bank =  personalPrototype.MyBank

import personal
Bank = personal.Hayden

week = 1
weeks = 2

while(week <= weeks):
    print("Week", week)

    personal.weeklyTransactions()
    if week %4 == 0:
        personal.monthlyTransactions()

    Bank.updateAccountsHistory()    
    Bank.printBalance()
    week += 1 

Bank.graphBalances(weeks)


