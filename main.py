import personal
Bank =  personal.MyBank
week = 1
weeks = 25

while(week <= weeks):
    print("Week", week)

    personalPrototype.weeklyTransactions()
    if week %4 == 0:
        personalPrototype.monthlyTransactions()
        
    Bank.updateAccountsHistory()    
    Bank.printBalance()
    week += 1 

Bank.graphBalances(weeks)