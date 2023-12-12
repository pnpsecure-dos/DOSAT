import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()

def tcp_con(tc_num, port):
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
        result = 0
    else:
        print("fail")
        result = -1

    return result

def tcp_server(port):
    host = jenkins_node.split(' ')[0]

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.settimeout(30)
    server_socket.bind((host,port))
    server_socket.listen()

    try:
        client_socket, client_addr = server_socket.accept()
        msg = client_socket.recv(1024)
        client_socket.sendall("ok".encode())
        client_socket.close()

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except socket.timeout:
        pass

    server_socket.close()