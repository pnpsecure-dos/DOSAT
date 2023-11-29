import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *
from dbcon import DBCtrl

os_platform = platform.system()

def file_read(tc_num):
    if os_platform == "Windows" :
        if 38 <= tc_num.split('_')[1] <=60:
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s"%(tc_num,tc_num)
        else:
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        if 38 <= tc_num.split('_')[1] <=60:
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s"%(tc_num,tc_num)
        else:
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    if os.path.isfile(path) == False:
        f = open(path, 'w')
        f.write("TC test file")
        f.close()	
        
    try:
        f = open(path, 'r')
        f.read(10)
        f.close()
    except Exception as e:
        print(e)

    sleep(1)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        case1 = 0
    else:
        print("fail")
        case1 = -1

    if os_platform == "Windows" :
        os.system("type %s"%path)
    else :
        os.system("cat %s"%path)

    sleep(1)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        case2 = 0
    else:
        print("fail")
        case2 = -1

    if case1 == 0 and case2 == 0:
        result = 0
    else:
        result = -1

    return result

def file_create(tc_num):
    if os_platform == "Windows" :
        if tc_num.startswith("TC14_40"):
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s"%(tc_num,tc_num)
        else:
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        if tc_num.startswith("TC14_40"):
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s"%(tc_num,tc_num)
        else:
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    if os.path.isfile(path):
        os.remove(path)

    try:
        f = open(path, 'w')
        f.write("TC test file")
        f.close()
    except Exception as e:
        print(e)
        
    sleep(0.5)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        result = 0
    else:
        print("fail")
        result = -1

    return result

def file_write(tc_num):
    if os_platform == "Windows" :
        if tc_num.startswith("TC14_40"):
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s"%(tc_num,tc_num)
        else:
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        if tc_num.startswith("TC14_40"):
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s"%(tc_num,tc_num)
        else:
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    try:
        f = open(path, 'a')
        f.write("TC14 test file")
        f.close()
    except Exception as e:
        print(e)

    sleep(0.5)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        result = 0
    else:
        print("fail")
        result = -1

    return result

def file_rename(tc_num):
    if os_platform == "Windows" :
        if tc_num.startswith("TC14_40"):
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s"%(tc_num,tc_num)
        else:
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        if tc_num.startswith("TC14_40"):
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s"%(tc_num,tc_num)
        else:
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    if os.path.isfile(path) == False:
        f = open(path, 'w')
        f.write("TC14 test file")
        f.close() 

    if os_platform == "Windows" :
        os.system("rename %s %s_re"%(path,tc_num))
        os.system("del %s_re"%path)
    else :
        os.system("mv %s %s_re"%(path,path))

    sleep(0.5)
    
    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        result = 0
    else:
        print("fail")
        result = -1

    return result

def file_delete(tc_num):
    if os_platform == "Windows" :
        if tc_num.startswith("TC14_40"):
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s"%(tc_num,tc_num)
        else:
            path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        if tc_num.startswith("TC14_40"):
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s"%(tc_num,tc_num)
        else:
            path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    if os.path.isfile(path) == False:
        f = open(path,'w')
        f.write("TC14 test file")
        f.close()
    try:
        os.remove(path)
    except Exception as e:
        print(e)
    sleep(0.5)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        result = 0
    else:
        print("fail")
        result = -1

    return result

def file_execute(tc_num):
    if os_platform == "Windows" :
        if tc_num.startswith("TC14_40"):
            os.system("start C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\%s.exe/t & taskkill /f /im %s.exe"%(tc_num, tc_num))
        else:
            os.system("start C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s.exe /t & taskkill /f /im %s.exe"%(tc_num, tc_num))
    else :
        if tc_num.startswith("TC14_40"):
            os.system("/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/%s.sh"%(tc_num, tc_num))
        else:
            os.system("/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s.sh"%tc_num)

    sleep(0.5)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        result = 0
    else:
        print("fail")
        result = -1

    return result

def file_mkdir(tc_num):
    if os_platform == "Windows" :
        path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\test"%tc_num
    else :
        path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/test"%tc_num

    if os.path.isdir(path):
        os.rmdir(path)

    try:
        os.mkdir(path)
    except Exception as e:
        print(e)

    sleep(0.5)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        result = 0
    else:
        print("fail")
        result = -1

    return result

def file_rmdir(tc_num):
    if os_platform == "Windows" :
        path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s\\test"%tc_num
    else :
        path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s/test"%tc_num

    if os.path.isdir(path) == False:
        os.mkdir(path)

    try:
        os.rmdir(path)
    except Exception as e:
        print(e)

    sleep(0.5)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        result = 0
    else:
        print("fail")
        result = -1

    return result

def file_alert(tc_num):
    dt = nowDate()
    now_dt = datetime.now()

    if os_platform == "Windows" :
        os.system("type C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num)
    else :
        os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num)

    sleep(0.5)

    count = 0
    tmp = False
    while count < 30:
        sleep(5)
        
        alert = dbExecute("dbsafer_log_%s_%s"%(dt['year'], dt['month']),"select * from alertlog;")[-1]
        alert_date = datetime.strptime(alert[0], '%Y-%m-%d %H:%M:%S')

        if alert_date >= now_dt:
            tmp = True
            break
        count+=1
    if tmp:
        print('true')
        result = 0
    else:
        print('fail')
        result = -1

    return result

def file_log(tc_num):
    if os_platform == "Windows" :
        os.system("type C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num)
    else :
        os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num)

    sleep(120)

    columns=["policy_name"]
    tc_list = ['TC14_08', 'TC14_09', 'TC14_10', 'TC14_11', 'TC14_12_1_create', 'TC14_12_2_write', 'TC14_12_3_read',
                'TC14_12_4_rename', 'TC14_12_5_delete', 'TC14_12_6_execute', 'TC14_12_7_mkdir', 'TC14_12_8_rmdir',
                'TC14_21', 'TC14_22', 'TC14_23', 'TC14_24', 'TC14_25', 'TC14_26', 'TC14_27', 'TC14_30', 'TC14_31',
                'TC14_32', 'TC14_34', 'TC14_35', 'TC14_36', 'TC14_38', 'TC14_39', 'TC14_49', 'TC14_50', 'TC14_51',
                'TC14_52', 'TC14_53', 'TC14_54', 'TC14_55', 'TC14_58', 'TC14_59', 'TC14_60', 'TC14_40_1_create',
                'TC14_40_2_write', 'TC14_40_3_read', 'TC14_40_4_rename', 'TC14_40_5_delete', 'TC14_40_6_execute', 'TC14_40_7_mkdir', 'TC14_40_8_rmdir']

    dt = nowDate()

    dbs = DBCtrl()
    ret= dbs.connect()
    ret = dbs.select("dbsafer_log_%s_%s"%(dt['year'],dt['month']),"access_file_%s"%dt['day'], "",columns)

    log_list_tmp = sum(ret, [])
    log_list =[]

    for log in log_list_tmp:
        index = log.rfind("_")
        log_tmp = log[0:index]
        log_list.append(log_tmp)

    for tc in tc_list :
        if os_platform == "Windows" :
            tc = tc + "_win"
        if tc in log_list :
            print("%s ok"%tc)
            continue
        else :
            print("fail")
            result = -1

    print("true")
    result = 0

    return result




















