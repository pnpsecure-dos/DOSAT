import socket
import sys
from variables import *

host = jenkins_node.split(' ')[0]
port = int(sys.argv[1])
bufferSize  = 1024

send_msg = str.encode("Hello UDP Client")
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_socket.bind((host, port))
server_socket.settimeout(10)

print("UDP server up")

try:
    msg_from_client = server_socket.recvfrom(bufferSize)
    message = msg_from_client[0]
    address = msg_from_client[1]
    client_msg = "Message from Client:{}".format(message)
    client_ip  = "Client IP Address:{}".format(address)
    print(client_msg)
    print(client_ip)
except socket.timeout:
    print("time out")
    pass