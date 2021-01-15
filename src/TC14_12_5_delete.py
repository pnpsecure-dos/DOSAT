import os
import sys
from time import sleep

os.remove("/home/jenkins/workspace/DBSAFER OS/TC Test/test_dir/TC14_12_test_file_rename.txt")

sleep(0.5)

log_check = os.popen("tail -1 /home/pnpsecure/server_agent/addon/pfc/log/pfclog | awk '{print $22}'").read()
tc_num = "TC14_12_5"

if tc_num in log_check :
    print("true")
else :
    print("fail")
    sys.exit(99)
