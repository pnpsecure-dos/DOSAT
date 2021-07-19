import os, sys, platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    path = "C:\\fac_test_dir\\%s"%tc_num
else :
    path = "/home/fac_test_dir/%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("TC14_12_4_rename test file")
	f.close() 

os.system("mv /home/fac_test_dir/%s /home/fac_test_dir/%s_re"%(tc_num,tc_num))
os.system("mv /home/fac_test_dir/%s_re /home/fac_test_dir/%s"%(tc_num,tc_num))

sleep(1)
if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)
