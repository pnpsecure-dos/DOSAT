import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

# file name without py
tc_num = sys.argv[1]
columns=["policy_name"]

dt = nowDate()

dbs = DBCtrl()
ret = dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"su_%s"%dt['day'], "",columns) 

log_list_tmp = sum(ret, [])
log_list =[]

for log in log_list_tmp:
    index = log.rfind("_")
    log_tmp = log[0:index]
    log_list.append(log_tmp)

if tc_num in log_list :
    print("%s ok"%tc_num)
else :
    print("fail")
    sys.exit(-1)

print("true")
sys.exit(0)