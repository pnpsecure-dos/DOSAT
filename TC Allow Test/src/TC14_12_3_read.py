import os,sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]
path = "/home/fac_test_dir/%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("TC14_12_3_read test file")
	f.close()	

try:
	f = open(path, 'r')
	f.read(10)
	f.close()
except Exception as e:
	print(e)
        sys.exit(-1)
sleep(1)

if logCheck(tc_num) == policy_status :
        print("true")
        sys.exit(0)
else :
        print("fail")
        sys.exit(-1)
