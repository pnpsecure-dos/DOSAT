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
svc_path = '"C:\\Program Files\\PNP SECURE\\NODESAFER\\nodesaferwch.exe"'
svc_cmd = ["start", "stop", "delete"]

if os_platform == "Windows" :
    try:
        os.system("sc create %s binpath= %s"%(tc_num, svc_path))
        sleep(0.5)
    except:
        print("svc create fail")

    try:
        for cmd in svc_cmd:
            os.system("sc %s %s"%(cmd, tc_num))
            sleep(0.5)
    except:
        print("svc control fail")
else :
    pass

sleep(0.5)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
else:
    print("fail")
    sys.exit(-1)


sleep(120)

columns=["policy_name"]
tc_list = ["TC14_309", "TC14_310", "TC14_311", "TC14_312", "TC14_313", "TC14_314",
            "TC14_315", "TC14_316", "TC14_317", "TC14_318", "TC14_319", "TC14_320",
            "TC14_321", "TC14_324", "TC14_325", "TC14_326", "TC14_327", "TC14_328", "TC14_329"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"wservice_control_%s"%dt['day'], "",columns) 

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