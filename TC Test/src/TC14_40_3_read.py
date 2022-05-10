import os
import sys
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    path = "C:\\fac_test_dir\\%s\\%s"%(tc_num,tc_num)
else :
    path = "/home/fac_test_dir/%s/%s"%(tc_num,tc_num)

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
    os.system("type C:\\fac_test_dir\\%s\\%s"%(tc_num,tc_num))
else :
    os.system("cat /home/fac_test_dir/%s/%s"%(tc_num,tc_num))

sleep(1)

if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)