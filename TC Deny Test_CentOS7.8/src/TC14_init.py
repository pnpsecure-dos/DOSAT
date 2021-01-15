import socket as skt
from time import sleep
from fac_def import *
from variables import *

dt = nowDate()

# change policy on/off depending on variables.policy_status
if policy_status == "ALLOW":
	dbExecute("dbsafer3","update %s set enabled=1;"%(tb_fac))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"truncate access_file_%s;"%dt['day'])
elif policy_status == "DENY":
	sql = "update {0} set enabled=0 where name not like '{1}'".format(tb_fac, '%deny')
	print(sql)
	dbExecute("dbsafer3", sql)
	dbExecute("dbsafer3", sql.format(tb_fac, '%deny'))
	dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"truncate access_file_%s;"%dt['day'])

#send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))

ft = ''
count = 0

# check conf file update
while dt['time'] > ft and count < 30:
	ft = os.popen("ls -al /home/pnpsecure/server_agent/addon/pfc/conf/fac_auth.rules | awk '{print $8}'").read()
	sleep(1)
	count +=1


