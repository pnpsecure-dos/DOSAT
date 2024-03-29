import socket as skt
import os
import platform
import time
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
dt = nowDate()

# change policy on/off depending on variables.policy_status
for policy_table in policy_tables:
    dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%policy_table)
    if policy_status == "DENY":
        dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%' and name like '%%allow';"%policy_table)
dbExecute("dbsafer3","update policy_file_bypass set enabled=1 where name like 'TC%%';")
print("policy DB change")

# delete log tables
for log_table in log_tables:
    try:
        dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"delete from %s_%s;"%(log_table, dt['day']))
    except:
        print("%s_%s doesn't exist"%(log_table, dt['day']))
print("policy log delete")

# send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))

ft = ''
count = 0

if os_platform == "Windows" :
    win_sa_path = "C:\\Program Files\\PNP SECURE\\NODESAFER\\conf"
else :
    tmp_path = os.popen('cat /etc/.pfcpath').read().split('=')[1]
    remove_path = "/addon/pfc"
    sa_path = tmp_path[:-len(remove_path)].rstrip('/')

# check conf file update
while dt['time'] > ft and count < 150:
    if os_platform == "Windows" :
        ft = time.ctime(os.path.getmtime(win_sa_path)).split()[3]
    else :
        ft = os.popen("ls -al %s/conf/access.rules | awk '{print $8}'" %sa_path).read()
    sleep(1)
    count +=1

sleep(5)