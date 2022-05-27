import os
import platform
import sys
from socket import *

os_platform = platform.system()
port = int(sys.argv[1])

if os_platform == "Windows" :
    host = "192.168.105.69"
else :
    host = "192.168.105.67"

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