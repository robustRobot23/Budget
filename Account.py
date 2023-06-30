class Account:
    def __init__(self, name, startingValue):
        self.balance = startingValue
        self.name = name
        self.history = [startingValue]
        # self.log = {}
        

    def transact(self, transactAmount):
        if self.balance + transactAmount < 0:
            raise Exception("Tried to withdraw too much")
        else:
            self.balance += transactAmount

        print(f"{self.name} transacted ${transactAmount}")
        # self.log.update({description,transactAmount})

    def update(self):
        self.history.append(self.balance)