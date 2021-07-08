import os,sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]
path = "C:\\fac_test_dir\\%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("TC14_12_4_rename test file")
	f.close() 

os.system("rename C:\\fac_test_dir\\%s C:\\fac_test_dir\\%s_re"%(tc_num,tc_num))
os.system("rename C:\\fac_test_dir\\%s_re C:\\fac_test_dir\\%s"%(tc_num,tc_num))

sleep(1)
if logCheck(tc_num) == policy_status :
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)
