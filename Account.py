class Account:
    def __init__(self, name, startingValue):
        self.balance = startingValue
        self.weeklyBalance = 0
        self.name = name
        self.history = [startingValue]
        # self.log = {}
        

    def transact(self, transactAmount):
        if self.balance + transactAmount < 0:
            raise Exception("Tried to withdraw too much")
        else:
            self.balance += transactAmount
            self.weeklyBalance += transactAmount

        # print(f"{self.name} transacted ${transactAmount}")
        # self.log.update({description,transactAmount})

    def update(self):
        self.history.append(self.balance)
        # print(f"Weekly Change for {self.name}: ${self.weeklyBalance}")
        self.weeklyBalance = 0