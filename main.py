import Account
import personal

   
def requestDeposits():
    print("Transactions:")
    done = False
    doneInput = input("Finished for the week? y/n ")
    done = doneInput == "y"
    while (not done):

        inputAccount = ""
        transactionAmount = 0
        account = input("Enter Account to Transact to: ")
        if account in Account.names:
            currentAccount = personal.accounts[personal.findAccountIndex(inputAccount)]
            transactionAmount = float(input("Enter Amount"))
            if (transactionAmount != 0):
                currentAccount.transact(transactionAmount)
        else:
            print("Account name not found")
        
        doneInput = input("Finished for the week? y/n ")
        done = doneInput == "y"
        

        
def printBalance():
    for account in personal.accounts:
        print(f"    {account.name:<25} ${account.balance:.2f}")

def init():
    mode = input("Choose Mode: Update, Free Run  ")
    weeks = int(input("Choose Weeks: "))
    if mode == "Update":
        return True, weeks
    return False, weeks

def run():
    week = 1
    weeks = 25
    updateTransaction = False
    # updateTransaction, weeks = init()
    
    while(week <= weeks):

        print("Week", week)

        personal.weeklyTransactions()
        if week %4 == 0:
            personal.monthlyTransactions()

        if updateTransaction:
            print("Starting Balance:")
            printBalance()
            requestDeposits()
        
        print("Finishing Balance:")
        printBalance()
        print()

        week += 1   

run()