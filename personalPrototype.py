'''
    Contains the personalised simulation information
'''

import Account 
import theBank

MyBank = theBank.Bank()

MyBank.addAccount(Account.Account("Spending", 100))
MyBank.addAccount(Account.Account("Short Term Savings",220.00))
MyBank.addAccount(Account.Account("Secret Account", 65))
MyBank.addAccount(Account.Account("Savings",342))
MyBank.hideAccount("Secret Account")
MyBank.defualtSpending("Spending")


def weeklyTransactions():
    MyBank.transact(400)
    MyBank.transact(5)
    MyBank.transact(-200)
    MyBank.transact(-100)
    MyBank.transfer(10, "Secret Account")
    MyBank.transfer(15, "Short Term Savings")
    MyBank.transfer(40, "Savings")

def monthlyTransactions():
    MyBank.transact(-13)
    MyBank.transact(-43)
