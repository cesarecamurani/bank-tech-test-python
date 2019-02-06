from transaction import Transaction

class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, transaction, amount):
        transaction.credit()
        self.balance += amount

    def withdraw(self, transaction, amount):
        self.__noCredit(amount)
        transaction.debit()
        self.balance -= amount

    def __noCredit(self, amount):
        if amount > self.balance:
            raise Exception('Not enough credit!')
