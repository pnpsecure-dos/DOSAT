import sys
import dbcon
from dbcon import DBCtrl

columns=["policy_name"]
tc_list=["TC14_12_1", "TC14_12_2", "TC14_12_3", "TC14_12_4", "TC14_12_5", "TC14_12_6", "TC14_12_7", "TC14_12_8"]

dbs = DBCtrl()
ret=dbs.connect()
#테이블 데이터 삭제
ret = dbs.select("dbsafer_log_2021_01", "access_file_06", "",columns)  #년도/월/일 자동으로 계산 후 입력 필요
db_pm = sum(ret, [])

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
