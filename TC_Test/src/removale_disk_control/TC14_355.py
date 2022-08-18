import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from variables import *
from fac_def import *

os_platform = platform.system()

# file name without py
tc_num = "TC14_353"

dt = nowDate()
now_dt = datetime.now()

if os_platform == "Windows" :
    path = "F:\\%s"%tc_num
else :
	pass

sleep(0.5)

if os.path.isfile(path):
	os.remove(path)

try:
	f = open(path, 'w')
	f.write("TC14_354 test file")
	f.close()
	sleep(0.5)
	os.system("type %s"%path)
except Exception as e:
	print(e)

if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        sys.exit(0)
else:
        print("fail")
        sys.exit(-1)