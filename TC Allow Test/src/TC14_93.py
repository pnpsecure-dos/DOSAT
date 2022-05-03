import os, sys, platform
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl


os_platform = platform.system()

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    tc_sleep_pid=os.popen("tasklist | findstr %s_sleep"%tc_num).read()
    os.system("taskkill /f /pid %s"%tc_sleep_pid.split()[1])
else :
    tc_sleep_pid=os.popen("ps -ef | grep \"%s_sleep\" | grep -v grep | awk '{print $2}'"%tc_num).read()
    os.system("kill -9 %s"%tc_sleep_pid)


sleep(120)

columns=["policy_name"]
tc_list = ["TC14_75", "TC14_76", "TC14_77", "TC14_78", "TC14_79", "TC14_80", "TC14_81", "TC14_82", "TC14_83", "TC14_84", "TC14_85", "TC14_88", "TC14_89", "TC14_90", "TC14_91", "TC14_92", "TC14_93"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"access_process_%s"%dt['day'], "",columns) 

log_list_tmp = sum(ret, [])
log_list =[]

for log in log_list_tmp:
    index = log.rfind("_")
    log_tmp = log[0:index]
    log_list.append(log_tmp)

for tc in tc_list :
    if tc in log_list :
        continue
    else :
        print("fail")
        sys.exit(-1)

print("true")
sys.exit(0)