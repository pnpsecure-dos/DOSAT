from variables import *
import pymysql as py
import paramiko
import re
from time import sleep
import os, sys
from datetime import datetime

def runOnShell(client, cmdlines):
    """command to client server use paramiko 
    Args: 
        client(paramiko.SSHco):
        cmdlines(list):
    Return:
        dict_ret = {
            'cmd':cmdlines, 
            'recv':[]
        }
    Raises:
    """
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

def dbExecute(db,sql):
    """db connect, execute sql and db close
    Args:
        db(str): db what user use
        sql(str): sql command
    Return: X
    Raise:
    
    """
    con = py.connect(host=svr_ip, user= db_usr, password = db_pwd, db=db, charset='utf8')
    cur = con.cursor()
    cur.execute(sql)
    if sql.split(' ')[0] == 'select':
        rows = cur.fetchall()
        con.close()
        return rows
    con.commit()
    con.close()

def nowDate():
    """Now date, time 
    Args: X
    Return :	
        dt_dict ={
            "year":dt[0],
            "month":dt[1],
            "day":dt[2],
            "time":dt[3]
        }
    Reises:
    """
    dt = re.split('[-T]+',datetime.now().isoformat())
    dt_dict ={
        "year":dt[0],
        "month":dt[1],
        "day":dt[2],
        "time":dt[3]
    }
    return dt_dict




def logCheck(tc_num, os_platform):
    """check tc_num in pfclog
        Args:
                tc_num(str): test case num = file name
        Return:
                result(str) : policy status(ALLOW/DENY)
        Raises:

        """
    # ACT:'ALLOW/DENY' PNM:'Policy_Name'

    if os_platform == "Windows" : 
        count = 0
        log_path = r"C:\\ProgramData\\PFC\\data"
        status = False
        pstatus = "N/A"

        while count < 15 :
            log_files = os.listdir(log_path)
            for i in log_files :
                if i.split('.')[1] == "log" :
                    fp = open("C:\\ProgramData\\PFC\\data\\%s"%i, 'r', encoding='utf-16')
                    lines = fp.readlines()
                    for line in lines :
                        print(line)
                        tmp_line = line.split()
                        pname = tmp_line[19].split(':')[1]
                        if tc_num in pname :
                            status = True
                            pstatus = tmp_line[5].split(':')[1]
                            break
                    if status == True :
                        break
                else :
                    fp = open("C:\\ProgramData\\PFC\\data\\%s"%i, 'r', encoding='utf-16')
                    lines = fp.readlines()
                    for line in lines :
                        print(line)
                        tmp_line = line.split()
                        pname = tmp_line[15].split(':')[1]
                        if tc_num in pname :
                            status = True
                            pstatus = tmp_line[5].split(':')[1]
                            break
                    if status == True :
                        break
            if status == True :
                break
            sleep(1)
            count += 1

        return pstatus
        
    else :
        result = ''
        pfcpath = os.popen('cat /etc/.pfcpath').read().split('=')[1]
        pfcpath = pfcpath.strip('\n')

        hf_check = os.popen("tail -1 %s/log/pfclog | awk '{print $5}'"%pfcpath).read()
        udp_check = os.popen("tail -1 %s/log/pfclog | awk '{print $13}'"%pfcpath).read()

        if "HF_ACL" in hf_check:
            if "PRT" in udp_check:
                log_check = os.popen("tail -1 %s/log/pfclog | awk '{print $6, $17}'" %pfcpath).read()
            else:
                log_check = os.popen("tail -1 %s/log/pfclog | awk '{print $6, $16}'" %pfcpath).read()
        else:
            log_check = os.popen("tail -1 %s/log/pfclog | awk '{print $6, $22}'" %pfcpath).read()

        tmp = re.split('[: ]+',log_check)
        print(tmp)	
        pname = tmp[3]
        pstatus = tmp[1]
        if tc_num in pname:
                result = pstatus

        return result

