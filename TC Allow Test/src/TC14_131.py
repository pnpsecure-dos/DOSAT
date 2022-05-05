import os, platform
from socket import *
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
port = 14131

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

sleep(1)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)