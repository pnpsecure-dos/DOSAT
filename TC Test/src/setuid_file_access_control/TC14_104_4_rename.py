import os
import sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]

path = "/home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("pwd")
	f.close() 

os.system('chmod +x %s'%path)
os.system('chmod u+s %s'%path)

os.system("mv /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/%s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/%s_re"%(tc_num,tc_num))
os.system("mv /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/%s_re /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/%s"%(tc_num,tc_num))

sleep(1)
if logCheck(tc_num, 'Posix') == policy_status :
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)
