import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *
import re
from datetime import datetime

os_platform = platform.system()
# file name without py
tc_num = os.path.basename(__file__).split('.')[0]
svc_path = '"C:\\Program Files\\PNP SECURE\\NODESAFER\\nodesaferwch.exe"'
svc_cmd = ["start", "stop", "delete"]

dt = nowDate()
now_dt = datetime.now()

if os_platform == "Windows" :
    try:
        os.system("sc create %s binpath= %s"%(tc_num, svc_path))
        sleep(0.5)
    except:
        print("svc create fail")

    try:
        for cmd in svc_cmd:
            os.system("sc %s %s"%(cmd, tc_num))
            sleep(0.5)
    except:
        print("svc control fail")
else :
    pass

sleep(0.5)
    
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