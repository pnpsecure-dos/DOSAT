import os,sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]
path = "/home/fac_test_dir/%s.sh"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("echo 'TC14_12_6_execute test file'")
	f.close()


os.system("/home/fac_test_dir/%s.sh"%tc_num)

sleep(1)
if logCheck(tc_num) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)
