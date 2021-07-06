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
pfcpath = os.popen('cat /etc/.pfcpath').read().split('=')[1]
pfclog = "tail -1 %s/log/pfclog | awk '{print $15}'" %pfcpath

# SSH
try :
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, port=ssh_port, username=usr, password=pwd)
    sleep(1)
    stdin, stdout, stderr = ssh.exec_command(pfclog)
    log_rtn = stdout.read()
except :
    print("SSH Connect Fail")
    sys.exit(-1)

log_check = log_rtn.decode()
if tc_num in log_check :
    print("true")
else :
    print("fail")
    ssh.close()
    sys.exit(-1)

# FPT
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
    sys.exit(-1)

# Telnet
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
    sys.exit(-1)
    
ssh.close()
