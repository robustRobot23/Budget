import Account 
 
# Example personal.py module
# Customise this to your own situtation

Spending = Account.Account("Spending", 50)
Savings = Account.Account("Savings",123) 

accounts = [Spending,
            Savings]

def send(amount, receivingAccount, sendingAccount = Spending):
    receivingAccount.transact(amount)
    sendingAccount.transact(-amount)

def weeklyTransactions():
    Spending.transact(300)
    Spending.transact(24)
    Spending.transact(-200)
    Spending.transact(-60)
    send(50, Savings)

def monthlyTransactions():
    Spending.transact(-15)

def findAccountIndex(inputAccount):
    match inputAccount:
        case "Spending":
            return 0
        case "Savings":
            return 1
    raise Exception("Account doesn't exist in accounts list")