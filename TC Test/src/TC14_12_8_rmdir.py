import os
import sys
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    path = "C:\\fac_test_dir\\%s\\test"%tc_num
else :
    path = "/home/fac_test_dir/%s/test"%tc_num

if os.path.isdir(path) == False:
	os.mkdir(path)

try:
	os.rmdir(path)
except Exception as e:
	print(e)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else :
        print("fail")
        sys.exit(-1)

