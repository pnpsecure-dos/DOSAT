import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()

# file name without py
tc_num = sys.argv[1]

os.system("reg add HKEY_LOCAL_MACHINE\SOFTWARE\TC_TEST_KEY /v %s /t REG_SZ /d 'TC_ATUO_TEST' /f"%tc_num)
sleep(1)
os.system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\TC_TEST_KEY /v %s /f"%tc_num)
sleep(0.5)

if logCheck(tc_num, os_platform) == policy_status:
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)


