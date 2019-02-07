import datetime

class Statement:

    def __init__(self):
        self.header = " date || credit || debit || balance "

    # def display(self, transactions):
    #     statement = [i['date'] for i in transactions]
    #     print self.header + str(statement)
