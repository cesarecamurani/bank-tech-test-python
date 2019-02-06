from statement import Statement
import datetime

class Transaction:

    def __init__(self):
        self.transactions = []

    def credit(self, credit, balance):
        self.transactions.append(('date', datetime.datetime.now(),
                                  'credit', credit,
                                  'debit', None,
                                  'balance', balance))

    def debit(self, debit, balance):
        self.transactions.append(('date', datetime.datetime.now(),
                                  'credit', None,
                                  'debit', debit,
                                  'balance', balance))
