import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
host = jenkins_node.split(' ')[0]
port = 14249
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
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)
