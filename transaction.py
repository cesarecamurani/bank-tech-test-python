from statement import Statement
import datetime

class Transaction:

    def __init__(self):
        self.transactions = []

    def credit(self, credit, debit, balance):
        self.transactions.append(('date', datetime.datetime.now(),
                                  'credit', credit,
                                  'debit', None,
                                  'balance', balance))
