import os, sys, platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    path = "C:\\fac_test_dir\\%s\\%s"%(tc_num,tc_num)
else :
    path = "/home/fac_test_dir/%s/%s"%(tc_num,tc_num)

try:
	f = open(path, 'a')
	f.write("TC14_40_2_write test file")
	f.close()
except Exception as e:
	print(e)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)

