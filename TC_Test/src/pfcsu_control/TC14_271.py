import os
import sys
import subprocess
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *

# file name without py
tc_num = os.path.basename(__file__).split('.')[0]
password = "dbsafer00"
cmd = "sudo useradd -p %s %s"%(password, tc_num)

dt = nowDate()
now_dt = datetime.now()

subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True)
sleep(0.5)

try:
    p = subprocess.Popen(["pfc_su", "-", tc_num], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sleep(0.5)
    p.communicate(input="exit".encode('utf-8'))
    sleep(0.5)
except:
    print("pfc_su fail")

os.system("sudo userdel %s"%tc_num)

sleep(0.5)

if logCheck(tc_num, 'Posix') == policy_status:
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
