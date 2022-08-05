import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
# file name without py
tc_num = os.path.basename(__file__).split('.')[0]
posix_time_cmd = ["rdate -s time.bora.net", "date -s '10:10:10'", "timedatectl set-time '10:10:10'", "hwclock -s"]
windows_time_cmd = ["date 22-08-03", "time 14:00:00"]

dt = nowDate()
now_dt = datetime.now()

if os_platform == "Windows" :
    import pyautogui
    os.system("timedate.cpl")
    sleep(0.5)
    pyautogui.hotkey("altleft", "d")
    sleep(0.5)
    fw = pyautogui.getActiveWindow()
    sleep(1)

    pyautogui.click(fw.left+355, fw.top+250)
    sleep(0.5)
    pyautogui.click(fw.left+280, fw.top+370)
    sleep(0.5)
    pyautogui.hotkey("ESC")

    for cmd in windows_time_cmd:
        try:
            os.system("%s"%cmd)
        except:
            print("%s execute fail"%cmd)
        sleep(0.5)

    ''' ms-settings:dateandtime 으로 테스트 확인 ("자동으로 시간 설정" 해제하는 방법 찾아야 함)
    os.system('"c:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run.lnk"')
    sleep(0.5)
    pyautogui.write("ms-settings:dateandtime")
    sleep(0.5)
    pyautogui.hotkey("ENTER")
    sleep(0.5)
    fw2 = pyautogui.getActiveWindow()
    sleep(1)
    '''

else :
    for cmd in posix_time_cmd:
        try:
            os.system("sudo %s"%cmd)
        except:
            print("%s execute fail"%cmd)
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