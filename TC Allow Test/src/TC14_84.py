import os, sys, platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    tc_sleep_pid=os.popen("tasklist | findstr %s_sleep"%tc_num).read()
    os.system("taskkill /f /pid %s"%tc_sleep_pid.split()[1])
else :
    tc_sleep_pid=os.popen("ps -ef | grep \"%s_sleep\" | grep -v grep | awk '{print $2}'"%tc_num).read()
    os.system("kill -9 %s"%tc_sleep_pid)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)