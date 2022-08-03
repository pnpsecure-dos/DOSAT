import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

# cat
os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num)

sleep(1)

if logCheck(tc_num, 'Posix') == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)
