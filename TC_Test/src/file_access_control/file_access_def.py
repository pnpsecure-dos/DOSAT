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