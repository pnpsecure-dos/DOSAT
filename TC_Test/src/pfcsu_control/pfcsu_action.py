import os
import sys
import subprocess
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
from fac_def import *
from variables import *

# file name without py
tc_num = sys.argv[1]
password = "dbsafer00"
useradd_cmd = "sudo useradd %s"%tc_num
userdel_cmd = "sudo userdel -rf %s"%tc_num

subprocess.call('echo {} | sudo -S {}'.format(password, useradd_cmd), shell=True)
sleep(0.5)

try:
    p = subprocess.Popen(["pfc_su", "-", tc_num], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sleep(0.5)
    p.communicate(input="exit".encode('utf-8'))
    sleep(0.5)
except:
    print("pfc_su fail")

subprocess.call('echo {} | sudo -S {}'.format(password, userdel_cmd), shell=True)
