import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]

path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

if os.path.isfile(path):
	os.remove(path)

try:
	f=os.open(path, os.O_CREAT, 3577)
	os.close
except Exception as e:
	print(e)
	
sleep(1)

if logCheck(tc_num, 'Posix') == policy_status :
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)
