import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

# cat
os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num)

sleep(1)

if logCheck(tc_num, 'Posix') == policy_status:
    print("true")
else:
    print("fail")
    sys.exit(-1)


sleep(120)

columns=["policy_name"]
tc_list = ['TC14_100', 'TC14_101', 'TC14_102', 'TC14_103', 'TC14_104_1_create', 'TC14_104_2_write', 'TC14_104_3_read',
            'TC14_104_4_rename', 'TC14_104_5_delete', 'TC14_104_6_execute',
            'TC14_110', 'TC14_111', 'TC14_112', 'TC14_113', 'TC14_114', 'TC14_115', 'TC14_116', 'TC14_119', 'TC14_120',
            'TC14_121', 'TC14_122', 'TC14_123', 'TC14_124']

dt = nowDate()
dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"setuid_file_%s"%dt['day'], "",columns)

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