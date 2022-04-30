class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, ammount):
        self.balance += ammount

    def withdraw(self, ammount):
        if ammount <= self.balance:
            self.balance -= ammount

    def __str__(self):
        return "Your current balance is {:.2f} euro".format(
            float(self.balance))
