import unittest
import datetime
from mock import Mock
from freezegun import freeze_time
from transaction import Transaction

class TestTransaction(unittest.TestCase):

    @freeze_time("2018-06-06")
    def test(self):
        assert datetime.datetime.now() == datetime.datetime(2018, 6, 6)

    def setUp(self):
        self.bank_account = Mock()
        self.transaction = Transaction()

    def test_transactions_is_empty_at_init(self):
        assert self.transaction.transactions == []

    # def test_credit_stores_the_transaction(self):


if __name__ == '__main__':
    unittest.main()
