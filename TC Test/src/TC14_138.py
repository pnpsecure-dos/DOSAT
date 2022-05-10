import os
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

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((host,port))

print("wait...")

serverSocket.close()

sleep(1)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)