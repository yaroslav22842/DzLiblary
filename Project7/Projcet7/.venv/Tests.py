import unittest
from Main import *


class My_test(unittest.TestCase):

    def test_Hello(self):
        self.assertEqual(Hello(), "ended")
    def test_Start(self):
        self.assertEqual(Start(), 6)



if __name__ == "__main__":
        unittest.main
