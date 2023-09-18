import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from socket import *
from variables import *

port = int(sys.argv[1])

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