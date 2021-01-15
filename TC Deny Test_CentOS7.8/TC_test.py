import unittest
import os
from time import sleep

class TC_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.system('python ./src/TC14_init.py')

    @classmethod
    def tearDownClass(cls):
        print("")

    def test_TC14_08(self):
        rtn = os.system('python ./src/TC14_08.py')
        self.assertEqual(rtn,0)

    def test_TC14_09(self):
        rtn = os.system('python ./src/TC14_09.py')
        self.assertEqual(rtn,0)

    def test_TC14_10(self):
        rtn = os.system('python ./src/TC14_10.py')
        self.assertEqual(rtn,0)

    def test_TC14_11(self):
        rtn = os.system('python ./src/TC14_11.py')
        self.assertEqual(rtn,0)

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

    def test_TC14_21(self):
        rtn = os.system('python ./src/TC14_21.py')
        self.assertEqual(rtn,0)

    def test_TC14_22(self):
        rtn = os.system('python ./src/TC14_22.py')
        self.assertEqual(rtn,0)

    def test_TC14_23(self):
        rtn = os.system('python ./src/TC14_23.py')
        self.assertEqual(rtn,0)

    def test_TC14_24(self):
        rtn = os.system('python ./src/TC14_24.py')
        self.assertEqual(rtn,0)

    def test_TC14_25(self):
        rtn = os.system('python ./src/TC14_25.py')
        self.assertEqual(rtn,0)

    def test_TC14_26(self):
        rtn = os.system('python ./src/TC14_26.py')
        self.assertEqual(rtn,0)

    def test_TC14_27(self):
        rtn = os.system('python ./src/TC14_27.py')
        self.assertEqual(rtn,0)

#    def test_TC14_28(self):
#        rtn = os.system('python ./src/TC14_28.py')
#        self.assertEqual(rtn,0)

#    def test_TC14_29(self):
#        rtn = os.system('python ./src/TC14_29.py')
#        self.assertEqual(rtn,0)

    def test_TC14_30(self):
        rtn = os.system('python ./src/TC14_30.py')
        self.assertEqual(rtn,0)

    def test_TC14_31(self):
        rtn = os.system('python ./src/TC14_31.py')
        self.assertEqual(rtn,0)

    def test_TC14_32(self):
        rtn = os.system('python ./src/TC14_32.py')
        self.assertEqual(rtn,0)

    def test_TC14_33(self):
        rtn = os.system('python ./src/TC14_33.py')
        self.assertEqual(rtn,0)
  
    def test_TC14_34(self):
        rtn = os.system('python ./src/TC14_34.py')
        self.assertEqual(rtn,0)
  
    def test_TC14_35(self):
        rtn = os.system('python ./src/TC14_35.py')
        self.assertEqual(rtn,0)

    def test_TC14_36(self):
        sleep(10)
        rtn = os.system('python ./src/TC14_36.py')
        self.assertEqual(rtn,0)
