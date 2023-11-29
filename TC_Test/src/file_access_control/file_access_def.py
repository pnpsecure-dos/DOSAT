import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import platform
from time import sleep
from fac_def import *
from variables import *

os_platform = platform.system()

def file_read(tc_num):
    if os_platform == "Windows" :
        path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
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

    sleep(0.5)

    if logCheck(tc_num, os_platform) == policy_status:
        print("true")
        case1 = 0
    else:
        print("fail")
        case1 = -1

    if os_platform == "Windows" :
        os.system("type C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num)
    else :
        os.system("cat /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num)

    sleep(0.5)

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
        path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    if os.path.isfile(path):
        os.remove(path)

    try:
        f = open(path, 'w')
        f.write("TC14_12_1_create test file")
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
        path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    try:
        f = open(path, 'a')
        f.write("TC14_12_2_write test file")
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
        path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    if os.path.isfile(path) == False:
        f = open(path, 'w')
        f.write("TC14_12_4_rename test file")
        f.close() 

    if os_platform == "Windows" :
        os.system("rename C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s %s_re"%(tc_num,tc_num))
        os.system("rename C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s_re %s"%(tc_num,tc_num))
    else :
        os.system("mv /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s_re"%(tc_num,tc_num))
        os.system("mv /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s_re /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%(tc_num,tc_num))

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
        path = "C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s"%tc_num
    else :
        path = "/home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/%s"%tc_num

    if os.path.isfile(path) == False:
        f = open(path,'w')
        f.write("TC14_12_5_delete test file")
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
        os.system("start C:\\jenkins\\sharedspace\\DBSAFER_OS\\TC_Test\\test_file\\windows\\%s.exe /t & taskkill /f /im %s.exe"%(tc_num, tc_num))
    else :
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



























