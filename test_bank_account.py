import unittest
from mock import Mock
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount()
        self.transaction = Mock()

    def test_balance_at_init_is_zero(self):
        assert self.bank_account.balance == 0

    def test_deposit_adds_money_into_the_account(self):
        self.bank_account.deposit(500)
        assert self.bank_account.balance == 500

    def test_withdraw_takes_money_from_the_account(self):
        self.bank_account.deposit(1000)
        self.bank_account.withdraw(500)
        assert self.bank_account.balance == 500

    def test_trying_to_withdraw_with_no_credit_raises_error(self):
        with self.assertRaisesRegexp(Exception, 'Not enough credit!'):
            self.bank_account.withdraw(1000)



if __name__ == '__main__':
    unittest.main()
