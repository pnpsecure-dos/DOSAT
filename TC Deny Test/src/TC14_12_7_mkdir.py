import os,sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]
path = "/home/fac_test_dir/%s/test"%tc_num

if os.path.isdir(path):
	os.rmdir(path)
try:
	os.mkdir(path)
except Exception as e:
	print(e)

sleep(1)
if logCheck(tc_num) == policy_status :
        print("true")
else :
        print("fail")
        sys.exit(99)

