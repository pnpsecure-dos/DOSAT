import socket as skt
import os
import platform
import time
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()
dt = nowDate()
log_tables = ["access_file", "etc_acl", "access_process", "bind_control", "setuid_file"]

# change policy on/off depending on variables.policy_status

dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%(tb_fac))
dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%(tb_tcp_ctrl))
dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%(tb_pkill))
dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%(tb_port_bind))
dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%(tb_setuid))
if policy_status == "DENY":
	dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%' and name like '%%allow';"%(tb_fac))
	dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%' and name like '%%allow';"%(tb_tcp_ctrl))
	dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%' and name like '%%allow';"%(tb_pkill))
	dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%' and name like '%%allow';"%(tb_port_bind))
	dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%' and name like '%%allow';"%(tb_setuid))

# delete log tables
for log_table in log_tables:
    try:
        dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"delete from %s_%s;"%(log_table, dt['day']))
    except:
        print("%s doesn't exist"%log_table)


# send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))

ft = ''
count = 0

if os_platform == "Windows" :
    fac_auth_path = "C:\\ProgramData\\PFC\\conf\\fac_auth.rules"
else :
    pfc_path = os.popen('cat /etc/.pfcpath').read().split('=')[1]
    pfc_path = pfc_path.strip('\n')

# check conf file update
while dt['time'] > ft and count < 150:
    if os_platform == "Windows" :
        ft = time.ctime(os.path.getmtime(fac_auth_path)).split()[3]
    else :
        ft = os.popen("ls -al %s/conf/fac_auth.rules | awk '{print $8}'" %pfc_path).read()
    sleep(1)
    count +=1

sleep(5)