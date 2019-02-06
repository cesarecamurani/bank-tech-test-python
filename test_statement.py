import unittest
from statement import Statement

class TestStatement(unittest.TestCase):

    def setUp(self):
        self.statement = Statement()

    def test_header_format(self):
        assert self.statement.header == " date || credit || debit || balance "

if __name__ == '__main__':
    unittest.main()
