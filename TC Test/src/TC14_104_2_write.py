import os
import sys
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
if os_platform == "Windows":
	sys.exit(0)

tc_num = os.path.basename(__file__).split('.')[0]
path = "/home/fac_test_dir/%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("pwd")
	f.close()	

os.system('chmod +x %s'%path)
os.system('chmod u+s %s'%path)

os.system('echo pwd >> %s'%path)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)

