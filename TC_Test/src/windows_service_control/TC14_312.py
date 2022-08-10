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
svc_path = '"C:\\Program Files\\PNP SECURE\\NODESAFER\\nodesaferwch.exe"'
svc_cmd = ["start", "stop", "delete"]

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

if logCheck(tc_num, os_platform) == policy_status:
    print("true")
    sys.exit(0)
else:
    print("fail")
    sys.exit(-1)

