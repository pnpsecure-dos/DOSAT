from http import server
import socket
import sys
from variables import *

host = jenkins_node.split(' ')[0]
port = int(sys.argv[1])
bufferSize  = 1024

send_msg = str.encode("Hello UDP Client")
udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket.bind((host, port))
udp_server_socket.settimeout(30)

try:
    msg_from_client = udp_server_socket.recvfrom(bufferSize)
    message = msg_from_client[0]
    address = msg_from_client[1]
    client_msg = "Message from Client:{}".format(message)
    client_ip  = "Client IP Address:{}".format(address)
    print(client_msg)
    print(client_ip)

except KeyboardInterrupt:
    raise KeyboardInterrupt

except socket.timeout:
    pass

udp_server_socket.close()