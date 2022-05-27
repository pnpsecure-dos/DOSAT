import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
port = 14138

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    host = "192.168.105.69"
else :
    host = "192.168.105.67"

try:
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind((host,port))
    server_socket.close()
except Exception as e:
    print(e)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)