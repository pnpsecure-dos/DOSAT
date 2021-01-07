import os
import sys
from time import sleep

os.system("/home/jenkins/workspace/DBSAFER\ OS/TC\ Test/test_dir/execute.sh")

sleep(0.5)

log_check = os.popen("tail -2 /home/pnpsecure/server_agent/addon/pfc/log/pfclog | awk '{print $22}'").read()
tc_num = "TC14_12_6"

if tc_num in log_check :
    print("true")
else :
    print("fail")
    sys.exit(99)
