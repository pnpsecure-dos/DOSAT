import socket as skt
import os
from time import sleep
from fac_def import *
from variables import *

dt = nowDate()

# change policy on/off depending on variables.policy_status
if policy_status == "ALLOW":
	dbExecute("dbsafer3","update %s set enabled=1 where name like "TC%";"%(tb_fac))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"truncate access_file_%s;"%dt['day'])
	
	dbExecute("dbsafer3","update %s set enabled=1 where name like "TC%";"%(tb_tcp_ctrl))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"truncate etc_acl_%s;"%dt['day'])

elif policy_status == "DENY":
	sql = "update {0} set enabled=0 where name like '{1}' and name like '{2}'"
	dbExecute("dbsafer3", "update %s set enabled=0;"%tb_fac)
	dbExecute("dbsafer3", sql.format(tb_fac, 'TC%', '%deny'))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"truncate access_file_%s;"%dt['day'])

	dbExecute("dbsafer3", "update %s set enabled=0;"%tb_tcp_ctrl)
	dbExecute("dbsafer3", sql.format(tb_tcp_ctrl, 'TC%', '%deny'))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"truncate etc_acl_%s;"%dt['day'])

#send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))

ft = ''
count = 0
pfcpath = os.popen('cat /etc/.pfcpath').read()

# check conf file update
while dt['time'] > ft and count < 30:
	ft = os.popen("ls -al %s/conf/fac_auth.rules | awk '{print $8}'", pfcpath).read()
	sleep(1)
	count +=1


