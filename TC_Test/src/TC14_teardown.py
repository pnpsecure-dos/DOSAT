from fac_def import *
from variables import *
import socket as skt

# change policy on/off depending on variables.policy_status
for policy_table in policy_tables:
    dbExecute("dbsafer3","update %s set enabled=0 where name like 'TC%%';"%policy_table)

# send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))