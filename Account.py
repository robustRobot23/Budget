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
            self.weeklyBalance = round(self.weeklyBalance, 2)

        # print(f"{self.name} transacted ${transactAmount}")
        # self.log.update({description,transactAmount})

    def update(self):
        self.history.append(round(self.balance,2))
        self.weeklyBalance = 0

    def difference(self):
        if len(self.history) >= 2:
            print(f"Weekly Change for {self.name}: ${round(self.history[-1] - self.history[-2],2)}")
        else: 
            print("Not enough history yet")
