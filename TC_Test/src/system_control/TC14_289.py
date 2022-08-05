import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
# file name without py
tc_num = "TC14_288"
posix_shutdown_cmd = ["init 0", "reboot", "shutdown", "poweroff", "halt"]

if os_platform == "Windows" :
    import pyautogui
    # 시작 메뉴에서 재시작 클릭
    pyautogui.click(x=1, y=1)
    sleep(0.5)
    pyautogui.click(x=20, y=1060)
    sleep(0.5)
    pyautogui.click(x=20, y=1020)
    sleep(0.5)
    pyautogui.click(x=20, y=960)
    sleep(0.5)
    pyautogui.click(x=30, y=920)
    sleep(0.5)
    pyautogui.click(x=30, y=920)
    sleep(1)
    pyautogui.click(x=280, y=960)
    sleep(2)

    # 시작 메뉴에서 종료 클릭
    pyautogui.click(x=1, y=1)
    sleep(0.5)
    pyautogui.click(x=20, y=1060)
    sleep(0.5)
    pyautogui.click(x=20, y=1020)
    sleep(0.5)
    pyautogui.click(x=20, y=930)
    sleep(0.5)
    pyautogui.click(x=30, y=920)
    sleep(0.5)
    pyautogui.click(x=30, y=920)
    sleep(1)
    pyautogui.click(x=280, y=960)
    sleep(2)

    os.system("shutdown")

else :
    for cmd in posix_shutdown_cmd:
        try:
            os.system("%s"%cmd)
        except:
            print("%s execute fail"%cmd)
        sleep(0.5)

sleep(0.5)

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)


