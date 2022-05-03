import os, sys, platform
import re
import socket as skt
from time import sleep
from variables import *
from fac_def import *
from datetime import datetime


os_platform = platform.system()

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]

dt = nowDate()
now_dt = datetime.now()

if os_platform == "Windows" :
    tc_sleep_pid=os.popen("tasklist | findstr %s_sleep"%tc_num).read()
    os.system("taskkill /f /pid %s"%tc_sleep_pid.split()[1])
else :
    tc_sleep_pid=os.popen("ps -ef | grep \"%s_sleep\" | grep -v grep | awk '{print $2}'"%tc_num).read()
    os.system("kill -9 %s"%tc_sleep_pid)

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