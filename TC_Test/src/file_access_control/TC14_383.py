import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from glob import glob
from fac_def import *
from dbcon import DBCtrl

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    os.system("type C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num)
else :
    os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num)

sleep(120)

columns=["policy_name"]
tc_list = ['TC14_359', 'TC14_360', 'TC14_361', 'TC14_362', 'TC14_373_1_create', 'TC14_373_2_write', 'TC14_373_3_read',
            'TC14_373_4_rename', 'TC14_373_5_delete', 'TC14_373_6_execute', 'TC14_373_7_mkdir', 'TC14_373_8_rmdir',
            'TC14_363', 'TC14_364', 'TC14_365', 'TC14_366', 'TC14_367', 'TC14_368', 'TC14_369', 'TC14_372', 'TC14_381',
            'TC14_382', 'TC14_383', 'TC14_385', 'TC14_386']

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"access_file_%s"%dt['day'], "",columns)

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