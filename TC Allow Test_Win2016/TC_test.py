import unittest
import os
from time import sleep

class TC_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("set")

    @classmethod
    def tearDownClass(cls):
        print("tear")

    def test_TC14_08(self):
        rtn = 0
        self.assertEqual(rtn,0)
  
    def test_TC14_35(self):
        rtn = 0
        self.assertEqual(rtn,0)

    def test_TC14_36(self):
        rtn = 1
        self.assertEqual(rtn,0)
