import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *
import winreg

os_platform = platform.system()

# file name without py
tc_num = sys.argv[1]

try:
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\TC_TEST_KEY", 0, winreg.KEY_SET_VALUE)
except FileNotFoundError:
    # 만약 해당 키가 없는 경우 새로운 키를 생성합니다.
    reg_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\TC_TEST_KEY")

# 값을 설정합니다.
winreg.SetValueEx(reg_key, tc_num, 0, winreg.REG_SZ, tc_num)

# 레지스트리 키를 닫습니다.
winreg.CloseKey(reg_key)


# 열려있는 레지스트리 키 핸들을 얻습니다.
try:
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\TC_TEST_KEY", 0, winreg.KEY_SET_VALUE)
    winreg.DeleteValue(reg_key, tc_num)
    winreg.CloseKey(reg_key)
except FileNotFoundError:
    # 만약 해당 키가 없는 경우 작업을 중지합니다.
    print(f"Key not found.")


if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)
