import os
import sys
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    os.system("taskkill /f /im %s_sleep.exe"%tc_num)
else :
    os.system("killall -9 %s_sleep"%tc_num)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)