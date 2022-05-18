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
    sys.exit(0)
else :
    os.system("cat /home/fac_test_dir/%s"%tc_num)

sleep(0.5)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)
