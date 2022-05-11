import os
import sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]

path = "/home/fac_test_dir/%s"%tc_num

if os.path.isfile(path):
	os.remove(path)

try:
	f = open(path, 'w')
	f.write("pwd")
	f.close()
except Exception as e:
	print(e)
	
sleep(1)

if logCheck(tc_num, 'Posix') == policy_status :
	print("true")
	sys.exit(0)
else:
	print("fail")
	sys.exit(-1)
