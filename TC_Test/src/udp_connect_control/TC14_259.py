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
host = jenkins_node.split(' ')[0]
port = 14259
tc_num = os.path.basename(__file__).split('.')[0]

send_msg = str.encode("Hello UDP Server")
server_info = (host, port)
bufferSize = 1024

try:
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client_socket.sendto(send_msg, server_info)
    msg_from_server = udp_client_socket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msg_from_server[0])
    print(msg)
except Exception as e:
    print(e)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
else:
    print("fail")
    sys.exit(-1)

sleep(120)

columns=["policy_name"]
tc_list = ["TC14_246", "TC14_247", "TC14_248", "TC14_249", "TC14_250", "TC14_251", "TC14_252",
            "TC14_253", "TC14_254", "TC14_255", "TC14_256", "TC14_257", "TC14_258", "TC14_259"]

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