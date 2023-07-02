import matplotlib.pyplot as plt

class Bank:
    def __init__(self):
        self.accountNames = set()
        self.showAccounts = set()
        self.accounts = []
        self.defualtSpendingAccount = None
    
    def addAccount(self, account):
        self.accounts.append(account)
        self.accountNames.add(account.name)
        self.showAccounts.add(account.name)

    def findAccount(self, accountName):
        for account in self.accounts:
            if account.name == accountName:
                return account
        raise Exception("Account doesn't exist in accounts list")

    def hideAccount(self, accountName):
        self.showAccounts.remove(accountName)

    def defualtSpending(self, accountName):
        account = self.findAccount(accountName)
        self.defualtSpendingAccount = account

    def checkDefualtExists(self):
        if self.defualtSpendingAccount == None:
            raise Exception("No defualt Account set, please specify")
        
    def findTotalBalance(self):
        sum = 0
        for account in self.accounts:
            sum += account.balance
        return sum
    
    def transact(self, amount, sendingAccountName = None):
        if sendingAccountName == None:
            self.checkDefualtExists()
            account = self.defualtSpendingAccount
        else:
            account = self.findAccount(sendingAccountName)
        try:
            account.transact(amount)
        except:
            raise Exception("Unable to transact from account")

    def transfer(self, amount, receivingAccountName, sendingAccountName = None):
        startingBalance = self.findTotalBalance()
        if sendingAccountName == None:
            self.checkDefualtExists()
            sendingAccount = self.defualtSpendingAccount
        else:
            sendingAccount = self.findAccount(sendingAccountName)

        try:
            sendingAccount.transact(-amount)
        except:
            raise Exception("Unable to transfer to sending account, account may not exist")


        receivingAccount = self.findAccount(receivingAccountName)
        try:
            receivingAccount.transact(amount)
        except:
            raise Exception("Unable to transfer to recieving account, account may not exist")
        
        # print(f"Sending ${amount} to {receivingAccount.name} from {sendingAccount.name}")

        finishingBalance = self.findTotalBalance()
        if startingBalance < finishingBalance -0.5 or startingBalance > finishingBalance + 0.5:
            raise Exception("Starting Balance doesn't equal finishing Balance after transfer")

    def updateAccountsHistory(self):
        for account in self.accounts:
            account.update()

    def printBalance(self):
        print("Finishing Balance:")
        for account in self.accounts:
            if account.name in self.showAccounts:
                print(f"    {account.name:<25} ${account.balance:.2f}")   
        print()
    

    def graphBalances(self, weeks):
        for account in self.accounts:
            if account.name in self.showAccounts:
                plt.plot(account.history, label = account.name)

        plt.title(f"Balance projection over {weeks} weeks")
        plt.xlabel("Weeks")
        plt.ylabel("$")
        plt.legend()
        plt.show()
