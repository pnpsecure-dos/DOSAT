import socket as skt
import os
from time import sleep
from fac_def import *
from variables import *

dt = nowDate()

# change policy on/off depending on variables.policy_status
if policy_status == "ALLOW":
	dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%(tb_fac))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"delete from access_file_%s;"%dt['day'])
	
	dbExecute("dbsafer3","update %s set enabled=1 where name like 'TC%%';"%(tb_tcp_ctrl))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"delete from etc_acl_%s;"%dt['day'])

elif policy_status == "DENY":
	dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%';"%(tb_fac))
	dbExecute("dbsafer3", "update %s set enabled=1 where name like 'TC%%' and name like '%%deny';"%(tb_fac))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"delete from access_file_%s;"%dt['day'])

	dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%';"%(tb_tcp_ctrl))
	dbExecute("dbsafer3", "update %s set enabled=1 where name like 'TC%%' and name like '%%deny';"%(tb_tcp_ctrl))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"delete from etc_acl_%s;"%dt['day'])

#send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))

ft = ''
count = 0
pfcpath = os.popen('cat /etc/.pfcpath').read().split('=')[1]
pfcpath = pfcpath.strip('\n')

# check conf file update
while dt['time'] > ft and count < 150:
	ft = os.popen("ls -al %s/conf/fac_auth.rules | awk '{print $8}'" %pfcpath).read()
	sleep(1)
	count +=1

sleep(5)
