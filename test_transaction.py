import unittest
from mock import Mock
from transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.bank_account = Mock()
        self.transaction = Transaction()

    def test_transactions_is_empty_at_init(self):
        assert self.transaction.transactions == []

if __name__ == '__main__':
    unittest.main()
