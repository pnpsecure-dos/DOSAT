import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

os_platform = platform.system()
port = 14740

tc_num = os.path.basename(__file__).split('.')[0]

host = jenkins_node.split(' ')[0]

try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((host,port))
    client_socket.send("hi".encode())
    msg = client_socket.recv(1024)
except Exception as e:
    print(e)

sleep(0.5)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
else:
    print("fail")
    sys.exit(-1)

sleep(120)

columns=["policy_name"]
tc_list = ["TC14_245", "TC14_61", "TC14_62", "TC14_63", "TC14_64", "TC14_66", "TC14_67",
            "TC14_68", "TC14_69", "TC14_70", "TC14_71", "TC14_72", "TC14_73", "TC14_74"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"etc_acl_%s"%dt['day'], "",columns) 

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