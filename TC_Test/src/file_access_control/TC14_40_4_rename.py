import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s"%(tc_num,tc_num)
else :
    path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s"%(tc_num,tc_num)

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("TC14_40_4_rename test file")
	f.close() 

if os_platform == "Windows" :
    os.system("rename C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s %s_re"%(tc_num,tc_num,tc_num))
    os.system("del C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s_re"%(tc_num,tc_num))
else :
    os.system("mv /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s_re"%(tc_num,tc_num,tc_num,tc_num))

sleep(0.5)
if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)
