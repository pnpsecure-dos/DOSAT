import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]

path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("pwd")
	f.close()	

os.system('chmod +x %s'%path)
os.system('chmod u+s %s'%path)

os.system('echo pwd >> %s'%path)

sleep(0.5)

if logCheck(tc_num, 'Posix') == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)

