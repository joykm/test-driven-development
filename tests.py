import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    # test that null string returns false
    def test1(self):
        input = ""
        self.assertFalse(check_pwd(input))

    # test that a string under 8 characters long returns false
    def test2(self):
        input = "1234567"
        self.assertFalse(check_pwd(input))

    # test that a string that is too large returns false
    def test3(self):
        input = "123456789012345678901"
        self.assertFalse(check_pwd(input))

if __name__ == '__main__':
    unittest.main()