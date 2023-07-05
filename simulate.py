import personalPrototype as personalInfo
Bank =  personalInfo.MyBank

# import personal as personalInfo
# Bank = personalInfo.Hayden

week = 1
weeks = 25

while(week <= weeks):
    print("Week", week)

    personalInfo.weeklyTransactions()
    if week %4 == 0:
        personalInfo.monthlyTransactions()

    Bank.updateAccountsHistory() 
    Bank.printDefaultBalanceChange()
    # Bank.printBalance()
    week += 1 

Bank.graphBalances(weeks)


