import os,sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]
path = "C:\\fac_test_dir\\%s"%tc_num

try:
	f = open(path, 'a')
	f.write("TC14_12_2_write test file")
	f.close()
except Exception as e:
	print(e)

sleep(1)

if logCheck(tc_num) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)

