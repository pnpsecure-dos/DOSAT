import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from variables import *
from fac_def import *
from datetime import datetime
from dbcon import DBCtrl

os_platform = platform.system()

# file name without py
tc_num = "TC14_353"

dt = nowDate()
now_dt = datetime.now()

if os_platform == "Windows" :
    path = "F:\\%s"%tc_num
else :
	pass

sleep(0.5)

if os.path.isfile(path):
	os.remove(path)

try:
	f = open(path, 'w')
	f.write("TC14_355 test file")
	f.close()
	sleep(0.5)
	os.system("type %s"%path)
except Exception as e:
	print(e)

if logCheck(tc_num, os_platform) == policy_status:
        print("true")
else:
        print("fail")
        sys.exit(-1)

sleep(120)

columns=["policy_name"]
tc_list = ["TC14_353"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"rd_control_%s"%dt['day'], "",columns) 

log_list_tmp = sum(ret, [])
log_list =[]

for log in log_list_tmp:
    index = log.rfind("_")
    log_tmp = log[0:index]
    log_list.append(log_tmp)

for tc in tc_list :
    if tc in log_list :
        print("%s ok"%tc)
        continue
    else :
        print("fail")
        sys.exit(-1)

print("true")
sys.exit(0)