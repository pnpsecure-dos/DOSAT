import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    os.system("type C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num)
else :
    os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num)

sleep(0.5)

if logCheck(tc_num, os_platform) == policy_status:
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)
