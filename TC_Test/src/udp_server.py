import socket
import sys

host = jenkins_node.split(' ')[0]
port = int(sys.argv[1])
bufferSize  = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# 데이터그램 소켓을 생성
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 주소와 IP로 Bind
server_socket.bind((host, port))

print("UDP server up and listening")

# 들어오는 데이터그램 Listen
while(True):
    bytesAddressPair = server_socket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    server_socket.sendto(bytesToSend, address)