import os
import sys
import platform
from glob import glob
from fac_def import *
from dbcon import DBCtrl

os_platform = platform.system()
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    os.system("type C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC Test\\test_file\\windows\\%s"%tc_num)
else :
    os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/%s"%tc_num)

sleep(120)

columns=["policy_name"]
tc_list = ['TC14_08', 'TC14_09', 'TC14_10', 'TC14_11', 'TC14_12_1_create', 'TC14_12_2_write', 'TC14_12_3_read',
            'TC14_12_4_rename', 'TC14_12_5_delete', 'TC14_12_6_execute', 'TC14_12_7_mkdir', 'TC14_12_8_rmdir',
            'TC14_21', 'TC14_22', 'TC14_23', 'TC14_24', 'TC14_25', 'TC14_26', 'TC14_27', 'TC14_30', 'TC14_31',
            'TC14_32', 'TC14_34', 'TC14_35', 'TC14_36', 'TC14_38', 'TC14_39', 'TC14_49', 'TC14_50', 'TC14_51',
            'TC14_52', 'TC14_53', 'TC14_54', 'TC14_55', 'TC14_58', 'TC14_59', 'TC14_60', 'TC14_40_1_create',
            'TC14_40_2_write', 'TC14_40_3_read', 'TC14_40_4_rename', 'TC14_40_5_delete', 'TC14_40_6_execute', 'TC14_40_7_mkdir', 'TC14_40_8_rmdir']

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