import pymysql as py
import paramiko
import time
import re
import socket as skt
import os, sys

db_usr = 'safeusr'
db_pwd = 'caNbPFvrYZDYIlRrQQEGTvEW7FbXZPTQ3NnOw0lv'
svr_ip = '192.168.105.65'
svr_usr = 'root'
svr_pwd = 'dbsafer00'
svr_port = 7795
cnt_ip = '192.168.105.118'
cnt_usr = 'root'
cnt_pwd = 'dbsafer00'
cnt_port = 22

on=1
off=0

tb_fac = "policy_file_auth"
tb_pkill = "policy_process_kill_auth"
tb_monitor = "policy_watch_process_list"
tb_setuid = "policy_setuid_auth"
tb_integrity = "policy_file_integrity"
tb_port_bind = "policy_pb_auth"
tb_tcp_ctrl = "policy_hf_auth"

def runonshell(client, cmdlines):
    sh = client.invoke_shell()    
    dict_ret = {'cmd':cmdlines, 'recv':[]}
    for cmd in cmdlines:
        ret = sh.send(cmd+"\n")
        time.sleep(0.5)
        buf=''
        while sh.recv_ready():
            buf = sh.recv(4096)
            dict_ret['recv'].append(re.split('[\r\n]+', buf.decode('utf-8'))[3:-1])
    sh.close()
    return dict_ret

def db_con(sql):
    con = py.connect(host=svr_ip, user= db_usr, password = db_pwd,
                 db='dbsafer3', charset='utf8')
    cur = con.cursor()
    cur.execute(sql)
    con.close()

def db_select(sql):
    con = py.connect(host=svr_ip, user= db_usr, password = db_pwd,
                 db='dbsafer3', charset='utf8')
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchone()
    con.close()
    return rows
    
    
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cli.connect(cnt_ip, port=cnt_port, username=cnt_usr, password=cnt_pwd)

before = runonshell(cli, ['cat /home/hgjeong/test01/test'])

#db update 0->1, 1->0
policy_name = 'jenkins_TC14_8_deny'

status = db_select("select enabled from %s where name='jenkins_TC14_8_deny'"%(tb_fac))

if status[0] == on:
    db_con("update %s set enabled=%d where name='jenkins_TC14_8_deny'"%(tb_fac, on))
elif status[0] == off:
    db_con("update %s set enabled=%d where name='jenkins_TC14_8_deny'"%(tb_fac, off))


#send to server_manager
usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), (svr_ip,21114))

time.sleep(20)
after = runonshell(cli, ['cat /home/hgjeong/test01/test'])

print(before['cmd'][0], " ", before['recv'][0][1])
print(after['cmd'][0], " ", after['recv'][0][1])


log_check = os.popen("tail -1 /home/pnpsecure/server_agent/addon/pfc/log/pfclog | awk '{print $22}'").read()
tc_num = "TC14_8"

if tc_num in log_check :
    print("true")
else :
    print("fail")
    sys.exit(99)
