import unittest
import os
from time import sleep
#test
class TC_test(unittest.TestCase):

    def setUP(self):
        print("")

    def tearDown(self):
        print("")

    def test_TC14_12_1_create(self):
        rtn = os.system('python ./src/TC14_12_1_create.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_2_write(self):
        rtn = os.system('python ./src/TC14_12_2_write.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_3_read(self):
        rtn = os.system('python ./src/TC14_12_3_read.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_4_rename(self):
        rtn = os.system('python ./src/TC14_12_4_rename.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_5_delete(self):
        rtn = os.system('python ./src/TC14_12_5_delete.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_6_execute(self):
        rtn = os.system('python ./src/TC14_12_6_execute.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_7_mkdir(self):
        rtn = os.system('python ./src/TC14_12_7_mkdir.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_8_rmdir(self):
        rtn = os.system('python ./src/TC14_12_8_rmdir.py')
        self.assertEqual(rtn,0)
