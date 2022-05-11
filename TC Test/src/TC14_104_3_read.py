import os
import sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]

path = "/home/fac_test_dir/%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path, 'w')
	f.write("TC14_104_3_read test file")
	f.close()	
	
try:
	f = open(path, 'r')
	f.read(10)
	f.close()
except Exception as e:
	print(e)

sleep(1)

if logCheck(tc_num, 'Posix') == policy_status :
	print("true")
else :
	print("fail")
	sys.exit(-1)


os.system("cat /home/fac_test_dir/%s"%tc_num)

sleep(1)

if logCheck(tc_num, 'Posix') == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)