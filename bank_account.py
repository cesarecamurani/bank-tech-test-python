from transaction import Transaction

class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, transaction, amount):
        self.balance += amount
        transaction.credit(amount, self.balance)

    def withdraw(self, transaction, amount):
        self.__noCredit(amount)
        self.balance -= amount
        transaction.debit(amount, self.balance)

    def __noCredit(self, amount):
        if amount > self.balance:
            raise Exception('Not enough credit!')
