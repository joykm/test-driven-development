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

    # test that a string containing no lower case letters returns false
    def test4(self):
        input = "12345678"
        self.assertFalse(check_pwd(input))

    # test that a string containing no upper case lettes returns false
    def test5(self):
        input = "abcdefgh"
        self.assertFalse(check_pwd(input))

if __name__ == '__main__':
    unittest.main()