import os
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

os_platform = platform.system()
port = 14153

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    host = "192.168.105.69"
else :
    host = "192.168.105.67"

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen(1)

print("wait...")

serverSocket.close()

sleep(120)

columns=["policy_name"]
tc_list = ["TC14_131", "TC14_132", "TC14_133", "TC14_134", "TC14_135", "TC14_136", "TC14_137", "TC14_138",
            "TC14_139", "TC14_140", "TC14_141", "TC14_142", "TC14_143", "TC14_144", "TC14_145", "TC14_146", 
            "TC14_147", "TC14_150", "TC14_151", "TC14_152", "TC14_153"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"bind_control_%s"%dt['day'], "",columns) 

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