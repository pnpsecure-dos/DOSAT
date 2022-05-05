import os, sys, platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    os.system("start C:\\fac_test_dir\\%s\\%s.exe /t & taskkill /f /im %s.exe"%(tc_num, tc_num))
else :
    os.system("/home/fac_test_dir/%s/%s.sh"%(tc_num, tc_num))

sleep(1)
if logCheck(tc_num, os_platform) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)
