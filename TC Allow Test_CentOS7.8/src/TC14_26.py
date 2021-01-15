import os, sys
from time import sleep
from fac_def import * 
from variables import *

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

os.system("cat /home/fac_test_dir/%s"%tc_num)
sleep(1)

if logCheck(tc_num) == policy_status:
	print("true")
else:
	print("fail")
	sys.exit(99)


