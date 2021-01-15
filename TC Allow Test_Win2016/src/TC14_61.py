import paramiko
import ftplib
import telnetlib
import os
import sys
from time import sleep

ip = "192.168.105.68"
ssh_port = 22
ftp_port = 21
telnet_port = 23
usr = "root"
pwd = "dbsafer00"
tc_num = os.path.basename(__file__).split('.')[0]
pfclog = "tail -1 /home/pnpsecure/server_agent/addon/pfc/log/pfclog | awk '{print $15}'"

#SSH 접속 
try :
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, port=ssh_port, username=usr, password=pwd)
    sleep(1)
    stdin, stdout, stderr = ssh.exec_command(pfclog)
    log_rtn = stdout.read()
except :
    print("SSH Connect Fail")
    sys.exit(99)
log_rtn.d
log_check = log_rtn.decode()
if tc_num in log_check :
    print("true")
else :
    print("fail")
    ssh.close()
    sys.exit(99)

#FTP 접속
try :
    ftp = ftplib.FTP()
    ftp.connect(ip, ftp_port)
    ftp.login(usr, pwd)
    ftp.quit()
    sleep(1)
    stdin, stdout, stderr = ssh.exec_command(pfclog)
    log_rtn = stdout.read()
except :
    print("FTP Connect Fail")

log_check = log_rtn.decode()
if tc_num in log_check :
    print("true")
else :
    print("fail")
    ssh.close()
    sys.exit(99)

#Telnet 접속
try :
    telnet = telnetlib.Telnet(ip)
    telnet.read_until(b"login: ")
    telnet.write(usr.encode("ascii") + b"\n")
    telnet.read_until(b"Password: ")
    telnet.write(pwd.encode("ascii") + b"\n")
    telnet.write(b"exit\n")
    telnet.close()
    sleep(1)
    stdin, stdout, stderr = ssh.exec_command(pfclog)
    log_rtn = stdout.read()
except :
    print("Telnet Connect Fail")

log_check = log_rtn.decode()
if tc_num in log_check :
    print("true")
else :
    print("fail")
    ssh.close()
    sys.exit(99)
    
ssh.close()