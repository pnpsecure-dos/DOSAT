import os
import sys
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
if os_platform == "Windows":
	sys.exit(0)
	
tc_num = os.path.basename(__file__).split('.')[0]
dt = nowDate()
now_dt = datetime.now()

# cat
os.system("cat /home/fac_test_dir/%s"%tc_num)

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
