import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
import socket
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
host = jenkins_node.split(' ')[0]
port = 14256
tc_num = os.path.basename(__file__).split('.')[0]
dt = nowDate()
now_dt = datetime.now()

send_msg = str.encode("Hello UDP Server")
server_info = (host, port)
bufferSize = 1024

try:
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client_socket.sendto(send_msg, server_info)
except Exception as e:
    print(e)

udp_client_socket.close()

sleep(0.5)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
else:
    print("fail")
    sys.exit(-1)

count = 0
tmp = False

while count < 30:
	sleep(5)
	
	# last alertlog in dbsafer_log db 
	alert = dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"select * from alertlog;")[-1]
	alert_date = datetime.strptime(alert[0], '%Y-%m-%d %H:%M:%S')

	# compare logtime with file access time
	# if 'logtime > file access time' tmp = True
	if alert_date >= now_dt:
		result = re.split('[\r\n]+',alert[2])
#		print(result[3],result[5],result[7])
		tmp = True
		break
	count+=1
if tmp:
	print('true')
	sys.exit(0)
else:
	print('fail')
	sys.exit(-1)
