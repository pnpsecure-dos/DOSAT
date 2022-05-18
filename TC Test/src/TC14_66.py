import os
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
port = 14660

tc_num = os.path.basename(__file__).split('.')[0]

if os_platform == "Windows" :
    host = "192.168.105.69"
else :
    host = "192.168.105.67"

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
