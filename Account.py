names = set()

class Account:
    def __init__(self, name, startingValue):
        self.balance = startingValue
        self.name = name
        names.add(name)

    def transact(self, transactAmount):
        if self.balance + transactAmount < 0:
            raise Exception("Tried to withdraw too much")
        else:
            self.balance += transactAmount
