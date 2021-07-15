import socket as skt
from fac_def import *

dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%';"%(tb_fac))
dbExecute("dbsafer3", "update %s set enabled=0 where name like 'TC%%';"%(tb_tcp_ctrl))

#send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))
