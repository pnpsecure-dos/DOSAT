import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
port = 14620

tc_num = os.path.basename(__file__).split('.')[0]

host = jenkins_node.split(' ')[0]

try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((host,port))
    client_socket.send("hi".encode())
    msg = client_socket.recv(1024)
except Exception as e:
    print(e)

sleep(1)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)
