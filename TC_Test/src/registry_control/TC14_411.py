import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

os_platform = platform.system()

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

os.system("reg add HKEY_LOCAL_MACHINE\SOFTWARE\TC_TEST_KEY /v %s /t REG_SZ /d 'TC_ATUO_TEST' /f"%tc_num)
sleep(1)
os.system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\TC_TEST_KEY /v %s /f"%tc_num)

sleep(120)

columns=["policy_name"]
tc_list = ['TC14_387', 'TC14_388', 'TC14_389', 'TC14_390', 'TC14_391', 'TC14_392', 'TC14_393',
           'TC14_394', 'TC14_395', 'TC14_396', 'TC14_397', 'TC14_398', 'TC14_399', 'TC14_400',
           'TC14_401', 'TC14_402', 'TC14_403', 'TC14_406', 'TC14_407', 'TC14_408', 'TC14_409',
           'TC14_410', 'TC14_411']

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"registry_control_%s"%dt['day'], "",columns)

log_list_tmp = sum(ret, [])
log_list =[]

for log in log_list_tmp:
    index = log.rfind("_")
    log_tmp = log[0:index]
    log_list.append(log_tmp)

for tc in tc_list :
    if os_platform == "Windows" :
        tc = tc + "_win"
    if tc in log_list :
        print("%s ok"%tc)
        continue
    else :
        print("fail")
        sys.exit(-1)

print("true")
sys.exit(0)