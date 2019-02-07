import unittest
import datetime
from mock import Mock
from freezegun import freeze_time
from statement import Statement

class TestStatement(unittest.TestCase):

    def setUp(self):
        self.statement = Statement()
        self.transaction = Mock()

        self.transaction.transactions = [{'date': datetime.datetime.now().strftime('%d, %m, %Y'),
                                          'credit': 1000,
                                          'debit': None,
                                          'balance': 1000},
                                         {'date': datetime.datetime.now().strftime('%d, %m, %Y'),
                                          'credit': None,
                                          'debit': 500,
                                          'balance': 500}]

    def test_header_format(self):
        assert self.statement.header == " date || credit || debit || balance "

    # def test_display_shows_the_statement_in_right_format(self):
    #     freezer = freeze_time("2012-01-14 12:00:01")
    #     freezer.start()
    #     self.statement.display(self.transaction.transactions)
    #     self.assertEqual(self.transaction.transactions, ' date || credit || debit || balance\n ' + '{}'.format(datetime.datetime.now().strftime("%d, %m, %Y")) + ' ||  || 500.00 || 500.00\n ' + '{}'.format(datetime.datetime.now().strftime("%d, %m, %Y")) + ' || 1000.00 ||  || 1000.00\n ')
    #     freezer.stop()

if __name__ == '__main__':
    unittest.main()
