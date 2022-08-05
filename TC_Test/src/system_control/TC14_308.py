import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

os_platform = platform.system()
# file name without py
tc_num = "TC14_305"
posix_time_cmd = ["rdate -s time.bora.net", "date -s '10:10:10'", "timedatectl set-time '10:10:10'", "hwclock -s"]
windows_time_cmd = ["date 22-08-03", "time 14:00:00"]

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
            os.system("sudo %s"%cmd)
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
            os.system("%s"%cmd)
        except:
            print("%s execute fail"%cmd)
        sleep(0.5)

sleep(120)

columns=["policy_name"]
tc_list = ["TC14_305"]

dt = nowDate()

dbs = DBCtrl()
ret= dbs.connect()
ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"system_control_%s"%dt['day'], "",columns) 

log_list_tmp = sum(ret, [])
log_list =[]

for log in log_list_tmp:
    index = log.rfind("_")
    log_tmp = log[0:index]
    log_list.append(log_tmp)

for tc in tc_list :
    if tc in log_list :
        print("%s ok"%tc)
        continue
    else :
        print("fail")
        sys.exit(-1)

print("true")
sys.exit(0)