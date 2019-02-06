import unittest
from transaction import Transaction
import datetime
from mock import Mock
from freezegun import freeze_time

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.bank_account = Mock()
        self.transaction = Transaction()

    def test_transactions_is_empty_at_init(self):
        assert self.transaction.transactions == []

    def test_credit_stores_the_transaction_for_deposit(self):
        freezer = freeze_time("2012-01-14 12:00:01")
        freezer.start()
        self.transaction.credit(1000, 2000)
        self.assertEqual(self.transaction.transactions, [('date', datetime.datetime.now(),
                                                          'credit', 1000,
                                                          'debit', None,
                                                          'balance', 2000)])
        freezer.stop()

    def test_debit_stores_the_transaction_for_withdraw(self):
        freezer = freeze_time("2012-01-14 12:00:01")
        freezer.start()
        self.transaction.debit(1000, 1000)
        self.assertEqual(self.transaction.transactions, [('date', datetime.datetime.now(),
                                                          'credit', None,
                                                          'debit', 1000,
                                                          'balance', 1000)])
        freezer.stop()

if __name__ == '__main__':
    unittest.main()
