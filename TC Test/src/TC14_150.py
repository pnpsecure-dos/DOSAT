import os
import platform
from socket import *
from time import sleep
from fac_def import *
from variables import *
from datetime import datetime

os_platform = platform.system()
port = 14150

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]
dt = nowDate()
now_dt = datetime.now()

if os_platform == "Windows" :
    host = "192.168.105.69"
else :
    host = "192.168.105.67"

try:
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)
    server_socket.close()
except Exception as e:
    print(e)

sleep(1)

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