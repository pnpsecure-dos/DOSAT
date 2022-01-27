import os, sys, platform
from time import sleep
from fac_def import *
from variables import *
from glob import glob
from dbcon import DBCtrl


os_platform = platform.system()

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    os.system("type C:\\fac_test_dir\\%s"%tc_num)
else :
    tc_sleep_pid=os.popen("ps -ef | grep \"%s_sleep\" | grep -v grep | awk '{print $2}'"%tc_num).read()
    os.system("kill -9 %s"%tc_sleep_pid)


sleep(60)

#test
columns=["policy_name"]
file_list = sorted(glob("TC14_*"))[:-1]
tc_list = []

for tc in file_list:
	#remove '.py'
	tc_list.append(tc[:-3])	

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"access_process_%s"%dt['day'], "",columns) 

db_pm = sum(ret, [])
#print(db_pm)

result = "false"
tc_result = "true"
for tc_num2 in tc_list :
    for line in db_pm :
        if tc_num2 in line :
#            print("true",tc_num)
            result = "true"
            break
        else :
            result = "false"
    if result == "true" :
        continue
    else :
        print(tc_num2,"fail")
        tc_result = "false"
if tc_result == "false" :
    sys.exit(-1)

