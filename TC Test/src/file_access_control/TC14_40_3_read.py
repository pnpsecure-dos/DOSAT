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
	f.write("TC14_40_3_read test file")
	f.close()	
	
try:
	f = open(path, 'r')
	f.read(10)
	f.close()
except Exception as e:
	print(e)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status :
	print("true")
else :
	print("fail")
	sys.exit(-1)


if os_platform == "Windows" :
    os.system("type C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s"%(tc_num,tc_num))
else :
    os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s"%(tc_num,tc_num))

sleep(1)

if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)