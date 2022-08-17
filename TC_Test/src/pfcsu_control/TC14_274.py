import os
import sys
import subprocess
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]
password = "dbsafer00"
cmd = "sudo useradd -p %s %s"%(password, tc_num)

subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True)
sleep(0.5)

try:
    p = subprocess.Popen(["pfc_su", "-", tc_num], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sleep(0.5)
    p.communicate(input="exit".encode('utf-8'))
    sleep(0.5)
except:
    print("pfc_su fail")

os.system("sudo userdel %s"%tc_num)

sleep(0.5)

if logCheck(tc_num, 'Posix') == policy_status:
    print("true")
else:
    print("fail")
    sys.exit(-1)

sleep(120)

columns=["policy_name"]
tc_list = ["TC14_260", "TC14_261", "TC14_262", "TC14_263", "TC14_264", "TC14_265", "TC14_266",
            "TC14_267", "TC14_268", "TC14_271", "TC14_272", "TC14_273", "TC14_274"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"su_%s"%dt['day'], "",columns) 

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