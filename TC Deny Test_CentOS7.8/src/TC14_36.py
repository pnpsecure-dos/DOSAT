import sys

from fac_def import *
from dbcon import DBCtrl

#test
columns=["policy_name"]
tc_list=["TC14_12_1", "TC14_12_2", "TC14_12_3", "TC14_12_4", "TC14_12_5", "TC14_12_6", "TC14_12_7", "TC14_12_8"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"access_file_%s"%dt['day'], "",columns) 

db_pm = sum(ret, [])
print(db_pm)

"""
result = "false"
tc_result = "true"
for tc_num in tc_list :
    for line in db_pm :
        if tc_num in line :
#            print("true",tc_num)
            result = "true"
            break
        else :
            result = "false"
    if result == "true" :
        continue
    else :
        print(tc_num,"fail")
        tc_result = "false"
if tc_result == "false" :
    sys.exit(99)
"""
