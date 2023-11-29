import unittest
import os
import platform
from time import sleep
from src import variables
import subprocess
from src.file_access_control.file_access_def import *


os_platform = platform.system()
pfcsu_tc_list = ["TC14_260", "TC14_261", "TC14_262", "TC14_263", "TC14_264", "TC14_265", "TC14_266",
                       "TC14_267", "TC14_268", "TC14_271", "TC14_272", "TC14_273", "TC14_274"]

class TC_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os_platform != 'Windows':
            for tc in pfcsu_tc_list:
                subprocess.call('echo {} | sudo -S {}'.format("dbsafer00", "sudo useradd %s"%tc), shell=True)
            print("useradd finish")
        os.system('python ./src/TC14_setup.py')

    @classmethod
    def tearDownClass(cls):
        if os_platform != 'Windows':
            for tc in pfcsu_tc_list:
                subprocess.call('echo {} | sudo -S {}'.format("dbsafer00", "sudo userdel -rf %s"%tc), shell=True)
            print("userdel finish")
        os.system('python ./src/TC14_teardown.py')

    def test_TC14_08(self):
        rtn = file_read('TC14_08')
        self.assertEqual(rtn,0)
        
    def test_TC14_09(self):
        rtn = file_read('TC14_09')
        self.assertEqual(rtn,0)
 
    def test_TC14_10(self):
        rtn = file_read('TC14_10')
        self.assertEqual(rtn,0)
 
    def test_TC14_11(self):
        rtn = file_read('TC14_11')
        self.assertEqual(rtn,0)
 
    def test_TC14_12_1_create(self):
        rtn = file_create('TC14_12_1_create')
        self.assertEqual(rtn,0)

    def test_TC14_12_2_write(self):
        rtn = file_write('TC14_12_2_write')
        self.assertEqual(rtn,0)

    def test_TC14_12_3_read(self):
        rtn = file_read('TC14_12_3_read')
        self.assertEqual(rtn,0)

    def test_TC14_12_4_rename(self):
        rtn = file_rename('TC14_12_4_rename')
        self.assertEqual(rtn,0)

    def test_TC14_12_5_delete(self):
        rtn = file_delete('TC14_12_5_delete')
        self.assertEqual(rtn,0)

    def test_TC14_12_6_execute(self):
        if os_platform != 'Windows':
            os.system('chmod +x ./test_file/posix/TC14_12_6_execute.sh')
        rtn = file_execute('TC14_12_6_execute')
        self.assertEqual(rtn,0)

    def test_TC14_12_7_mkdir(self):
        rtn = file_mkdir('TC14_12_7_mkdir')
        self.assertEqual(rtn,0)

    def test_TC14_12_8_rmdir(self):
        rtn = file_rmdir('TC14_12_8_rmdir')
        self.assertEqual(rtn,0)

    def test_TC14_21(self):
        rtn = file_read('TC14_21')
        self.assertEqual(rtn,0)
 
    def test_TC14_22(self):
        rtn = file_read('TC14_22')
        self.assertEqual(rtn,0)
 
    def test_TC14_23(self):
        rtn = file_read('TC14_23')
        self.assertEqual(rtn,0)
 
    def test_TC14_24(self):
        rtn = file_read('TC14_24')
        self.assertEqual(rtn,0)
 
    def test_TC14_25(self):
        rtn = file_read('TC14_25')
        self.assertEqual(rtn,0)
 
    def test_TC14_26(self):
        rtn = file_read('TC14_26')
        self.assertEqual(rtn,0)
 
    def test_TC14_27(self):
        rtn = file_read('TC14_27')
        self.assertEqual(rtn,0)
 
    def test_TC14_30(self):
        rtn = file_read('TC14_30')
        self.assertEqual(rtn,0)
 
    def test_TC14_31(self):
        rtn = file_read('TC14_31')
        self.assertEqual(rtn,0)
 
    def test_TC14_32(self):
        rtn = file_read('TC14_32')
        self.assertEqual(rtn,0)

    def test_TC14_34(self):
        rtn = file_read('TC14_34')
        self.assertEqual(rtn,0)

    def test_TC14_35(self):
        rtn = file_read('TC14_35')
        self.assertEqual(rtn,0)

    def test_TC14_36(self):
        rtn = file_read('TC14_36')
        self.assertEqual(rtn,0)

    def test_TC14_38(self):
        rtn = file_read('TC14_38')
        self.assertEqual(rtn,0)

    def test_TC14_39(self):
        rtn = file_read('TC14_39')
        self.assertEqual(rtn,0)

    def test_TC14_40_1_create(self):
        rtn = file_create('TC14_40_1_create')
        self.assertEqual(rtn,0)

    def test_TC14_40_2_write(self):
        rtn = file_write('TC14_40_2_write')
        self.assertEqual(rtn,0)

    def test_TC14_40_3_read(self):
        rtn = file_read('TC14_40_3_read')
        self.assertEqual(rtn,0)

    def test_TC14_40_4_rename(self):
        rtn = file_rename('TC14_40_4_rename')
        self.assertEqual(rtn,0)

    def test_TC14_40_5_delete(self):
        rtn = file_delete('TC14_40_5_delete')
        self.assertEqual(rtn,0)

    def test_TC14_40_6_execute(self):
        if os_platform != 'Windows':
            os.system('chmod +x ./test_file/posix/TC14_40_6_execute.sh')
        rtn = file_execute('TC14_40_6_execute')
        self.assertEqual(rtn,0)

    def test_TC14_40_7_mkdir(self):
        rtn = file_mkdir('TC14_40_7_mkdir')
        self.assertEqual(rtn,0)

    def test_TC14_40_8_rmdir(self):
        rtn = file_rmdir('TC14_40_8_rmdir')
        self.assertEqual(rtn,0)

"""
    def test_TC14_49(self):
        rtn = os.system('python ./src/file_access_control/TC14_49.py')
        self.assertEqual(rtn,0)

    def test_TC14_50(self):
        rtn = os.system('python ./src/file_access_control/TC14_50.py')
        self.assertEqual(rtn,0)

    def test_TC14_51(self):
        rtn = os.system('python ./src/file_access_control/TC14_51.py')
        self.assertEqual(rtn,0)

    def test_TC14_52(self):
        rtn = os.system('python ./src/file_access_control/TC14_52.py')
        self.assertEqual(rtn,0)

    def test_TC14_53(self):
        rtn = os.system('python ./src/file_access_control/TC14_53.py')
        self.assertEqual(rtn,0)

    def test_TC14_54(self):
        rtn = os.system('python ./src/file_access_control/TC14_54.py')
        self.assertEqual(rtn,0)

    def test_TC14_55(self):
        rtn = os.system('python ./src/file_access_control/TC14_55.py')
        self.assertEqual(rtn,0)

    def test_TC14_58(self):
        rtn = os.system('python ./src/file_access_control/TC14_58.py')
        self.assertEqual(rtn,0)

    def test_TC14_59(self):
        rtn = os.system('python ./src/file_access_control/TC14_59.py')
        self.assertEqual(rtn,0)

    def test_TC14_60(self):
        rtn = os.system('python ./src/file_access_control/TC14_60.py')
        self.assertEqual(rtn,0)

    def test_TC14_60_36(self):
        sleep(10)
        rtn = os.system('python ./src/file_access_control/TC14_36.py')
        self.assertEqual(rtn,0)
    
    # 파일 접근 통제 - bypass 정책
    def test_TC14_359(self):
        rtn = os.system('python ./src/file_access_control/TC14_359.py')
        self.assertEqual(rtn,0)

    def test_TC14_360(self):
        rtn = os.system('python ./src/file_access_control/TC14_360.py')
        self.assertEqual(rtn,0)

    def test_TC14_361(self):
        rtn = os.system('python ./src/file_access_control/TC14_361.py')
        self.assertEqual(rtn,0)

    def test_TC14_362(self):
        rtn = os.system('python ./src/file_access_control/TC14_362.py')
        self.assertEqual(rtn,0)

    def test_TC14_363(self):
        rtn = os.system('python ./src/file_access_control/TC14_363.py')
        self.assertEqual(rtn,0)

    def test_TC14_364(self):
        rtn = os.system('python ./src/file_access_control/TC14_364.py')
        self.assertEqual(rtn,0)

    def test_TC14_365(self):
        rtn = os.system('python ./src/file_access_control/TC14_365.py')
        self.assertEqual(rtn,0)

    def test_TC14_366(self):
        rtn = os.system('python ./src/file_access_control/TC14_366.py')
        self.assertEqual(rtn,0)

    def test_TC14_367(self):
        rtn = os.system('python ./src/file_access_control/TC14_367.py')
        self.assertEqual(rtn,0)

    def test_TC14_368(self):
        rtn = os.system('python ./src/file_access_control/TC14_368.py')
        self.assertEqual(rtn,0)

    def test_TC14_369(self):
        rtn = os.system('python ./src/file_access_control/TC14_369.py')
        self.assertEqual(rtn,0)

    def test_TC14_372(self):
        rtn = os.system('python ./src/file_access_control/TC14_372.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_1_create(self):
        rtn = os.system('python ./src/file_access_control/TC14_373_1_create.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_2_write(self):
        rtn = os.system('python ./src/file_access_control/TC14_373_2_write.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_3_read(self):
        rtn = os.system('python ./src/file_access_control/TC14_373_3_read.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_4_rename(self):
        rtn = os.system('python ./src/file_access_control/TC14_373_4_rename.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_5_delete(self):
        rtn = os.system('python ./src/file_access_control/TC14_373_5_delete.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_6_execute(self):
        if os_platform != 'Windows':
            os.system('chmod +x ./test_file/posix/TC14_373_6_execute.sh')
        rtn = os.system('python ./src/file_access_control/TC14_373_6_execute.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_7_mkdir(self):
        rtn = os.system('python ./src/file_access_control/TC14_373_7_mkdir.py')
        self.assertEqual(rtn,0)

    def test_TC14_373_8_rmdir(self):
        rtn = os.system('python ./src/file_access_control/TC14_373_8_rmdir.py')
        self.assertEqual(rtn,0)
		
    def test_TC14_381(self):
        rtn = os.system('python ./src/file_access_control/TC14_381.py')
        self.assertEqual(rtn,0)

    def test_TC14_382(self):
        rtn = os.system('python ./src/file_access_control/TC14_382.py')
        self.assertEqual(rtn,0)

    def test_TC14_385(self):
        rtn = os.system('python ./src/file_access_control/TC14_385.py')
        self.assertEqual(rtn,0)
  
    def test_TC14_386(self):
        rtn = os.system('python ./src/file_access_control/TC14_386.py')
        self.assertEqual(rtn,0)
		
    def test_TC14_386_383(self):
        sleep(10)
        rtn = os.system('python ./src/file_access_control/TC14_383.py')
        self.assertEqual(rtn,0)

    # TCP 제어
    def test_TC14_61(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14610')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14610 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_61.py')
        self.assertEqual(rtn,0)

    def test_TC14_62(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14620')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14620 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_62.py')
        self.assertEqual(rtn,0)

    def test_TC14_63(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14630')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14630 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_63.py')
        self.assertEqual(rtn,0)

    def test_TC14_245(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14245')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14245 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_245.py')
        self.assertEqual(rtn,0)

    def test_TC14_64(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14640')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14640 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_64.py')
        self.assertEqual(rtn,0)

    def test_TC14_66(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14660')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14660 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_66.py')
        self.assertEqual(rtn,0)

    def test_TC14_67(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14670')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14670 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_67.py')
        self.assertEqual(rtn,0)

    def test_TC14_68(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14680')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14680 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_68.py')
        self.assertEqual(rtn,0)

    def test_TC14_69(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14690')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14690 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_69.py')
        self.assertEqual(rtn,0)

    def test_TC14_70(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14700')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14700 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_70.py')
        self.assertEqual(rtn,0)

    def test_TC14_71(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14710')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14710 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_71.py')
        self.assertEqual(rtn,0)

    def test_TC14_72(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14720')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14720 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_72.py')
        self.assertEqual(rtn,0)

    def test_TC14_73(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14730')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14730 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_73.py')
        self.assertEqual(rtn,0)

    def test_TC14_74(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_connect_control\\tcp_server.py 14740')
        else:
            os.system('python ./src/tcp_connect_control/tcp_server.py 14740 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_74.py')
        self.assertEqual(rtn,0)

    # 프로세스 킬
    def test_TC14_75(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_75_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_75_sleep')
            os.system('./test_process/posix/TC14_75_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_75.py')
        self.assertEqual(rtn,0)

    def test_TC14_76(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_76_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_76_sleep')
            os.system('./test_process/posix/TC14_76_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_76.py')
        self.assertEqual(rtn,0)

    def test_TC14_77(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_77_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_77_sleep')
            os.system('./test_process/posix/TC14_77_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_77.py')
        self.assertEqual(rtn,0)

    def test_TC14_78(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_78_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_78_sleep')
            os.system('./test_process/posix/TC14_78_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_78.py')
        self.assertEqual(rtn,0)

    def test_TC14_79(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_79_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_79_sleep')
            os.system('./test_process/posix/TC14_79_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_79.py')
        self.assertEqual(rtn,0)

    def test_TC14_80(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_80_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_80_sleep')
            os.system('./test_process/posix/TC14_80_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_80.py')
        self.assertEqual(rtn,0)

    def test_TC14_81(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_81_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_81_sleep')
            os.system('./test_process/posix/TC14_81_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_81.py')
        self.assertEqual(rtn,0)

    def test_TC14_82(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_82_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_82_sleep')
            os.system('./test_process/posix/TC14_82_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_82.py')
        self.assertEqual(rtn,0)

    def test_TC14_83(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_83_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_83_sleep')
            os.system('./test_process/posix/TC14_83_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_83.py')
        self.assertEqual(rtn,0)

    def test_TC14_84(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_84_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_84_sleep')
            os.system('./test_process/posix/TC14_84_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_84.py')
        self.assertEqual(rtn,0)

    def test_TC14_85(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_85_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_85_sleep')
            os.system('./test_process/posix/TC14_85_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_85.py')
        self.assertEqual(rtn,0)

    def test_TC14_88(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_88_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_88_sleep')
            os.system('./test_process/posix/TC14_88_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_88.py')
        self.assertEqual(rtn,0)

    def test_TC14_89(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_89_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_89_sleep')
            os.system('./test_process/posix/TC14_89_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_89.py')
        self.assertEqual(rtn,0)

    def test_TC14_90(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_90_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_90_sleep')
            os.system('./test_process/posix/TC14_90_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_90.py')
        self.assertEqual(rtn,0)

    def test_TC14_91(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_91_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_91_sleep')
            os.system('./test_process/posix/TC14_91_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_91.py')
        self.assertEqual(rtn,0)

    def test_TC14_92(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_92_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_92_sleep')
            os.system('./test_process/posix/TC14_92_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_92.py')
        self.assertEqual(rtn,0)

    def test_TC14_93(self):
        if os_platform == "Windows":
            os.system('start test_process\\windows\\TC14_93_sleep.exe')
        else:
            os.system('chmod +x ./test_process/posix/TC14_93_sleep')
            os.system('./test_process/posix/TC14_93_sleep &')
        rtn = os.system('python ./src/process_kill_control/TC14_93.py')
        self.assertEqual(rtn,0)
    
    # 권한상승 파일 통제
    def test_TC14_100(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_100')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_100.py')
            self.assertEqual(rtn,0)

    def test_TC14_101(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_101')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_101.py')
            self.assertEqual(rtn,0)

    def test_TC14_102(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_102')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_102.py')
            self.assertEqual(rtn,0)

    def test_TC14_103(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_103')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_103.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_1_create(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_104_1_create')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_1_create.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_2_write(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_104_2_write')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_2_write.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_3_read(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_104_3_read')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_3_read.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_4_rename(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_104_4_rename')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_4_rename.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_5_delete(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_104_5_delete')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_5_delete.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_6_execute(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_104_6_execute.sh')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_6_execute.py')
            self.assertEqual(rtn,0)

    def test_TC14_110(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_110')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_110.py')
            self.assertEqual(rtn,0)

    def test_TC14_111(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_111')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_111.py')
            self.assertEqual(rtn,0)

    def test_TC14_112(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_112')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_112.py')
            self.assertEqual(rtn,0)

    def test_TC14_113(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_113')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_113.py')
            self.assertEqual(rtn,0)

    def test_TC14_114(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_114')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_114.py')
            self.assertEqual(rtn,0)

    def test_TC14_115(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_115')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_115.py')
            self.assertEqual(rtn,0)

    def test_TC14_116(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_116')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_116.py')
            self.assertEqual(rtn,0)

    def test_TC14_119(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_119')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_119.py')
            self.assertEqual(rtn,0)

    def test_TC14_120(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_120')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_120.py')
            self.assertEqual(rtn,0)

    def test_TC14_121(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_121')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_121.py')
            self.assertEqual(rtn,0)

    def test_TC14_122(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_122')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_122.py')
            self.assertEqual(rtn,0)

    def test_TC14_123(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_123')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_123.py')
            self.assertEqual(rtn,0)

    def test_TC14_124(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+xs /home/jenkins/sharedspace/DBSAFER_OS/TC_Test/test_file/posix/TC14_124')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_124.py')
            self.assertEqual(rtn,0)

    # 포트 바인드
    def test_TC14_131(self):
        rtn = os.system('python ./src/port_bind_control/TC14_131.py')
        self.assertEqual(rtn,0)

    def test_TC14_132(self):
        rtn = os.system('python ./src/port_bind_control/TC14_132.py')
        self.assertEqual(rtn,0)

    def test_TC14_133(self):
        rtn = os.system('python ./src/port_bind_control/TC14_133.py')
        self.assertEqual(rtn,0)

    def test_TC14_134(self):
        rtn = os.system('python ./src/port_bind_control/TC14_134.py')
        self.assertEqual(rtn,0)

    def test_TC14_135(self):
        rtn = os.system('python ./src/port_bind_control/TC14_135.py')
        self.assertEqual(rtn,0)

    def test_TC14_136(self):
        rtn = os.system('python ./src/port_bind_control/TC14_136.py')
        self.assertEqual(rtn,0)

    def test_TC14_137(self):
        rtn = os.system('python ./src/port_bind_control/TC14_137.py')
        self.assertEqual(rtn,0)

    def test_TC14_138(self):
        rtn = os.system('python ./src/port_bind_control/TC14_138.py')
        self.assertEqual(rtn,0)

    def test_TC14_139(self):
        rtn = os.system('python ./src/port_bind_control/TC14_139.py')
        self.assertEqual(rtn,0)

    def test_TC14_140(self):
        rtn = os.system('python ./src/port_bind_control/TC14_140.py')
        self.assertEqual(rtn,0)

    def test_TC14_141(self):
        rtn = os.system('python ./src/port_bind_control/TC14_141.py')
        self.assertEqual(rtn,0)

    def test_TC14_142(self):
        rtn = os.system('python ./src/port_bind_control/TC14_142.py')
        self.assertEqual(rtn,0)

    def test_TC14_143(self):
        rtn = os.system('python ./src/port_bind_control/TC14_143.py')
        self.assertEqual(rtn,0)

    def test_TC14_144(self):
        rtn = os.system('python ./src/port_bind_control/TC14_144.py')
        self.assertEqual(rtn,0)

    def test_TC14_145(self):
        rtn = os.system('python ./src/port_bind_control/TC14_145.py')
        self.assertEqual(rtn,0)

    def test_TC14_146(self):
        rtn = os.system('python ./src/port_bind_control/TC14_146.py')
        self.assertEqual(rtn,0)

    def test_TC14_147(self):
        rtn = os.system('python ./src/port_bind_control/TC14_147.py')
        self.assertEqual(rtn,0)

    def test_TC14_150(self):
        rtn = os.system('python ./src/port_bind_control/TC14_150.py')
        self.assertEqual(rtn,0)

    def test_TC14_151(self):
        rtn = os.system('python ./src/port_bind_control/TC14_151.py')
        self.assertEqual(rtn,0)

    def test_TC14_152(self):
        rtn = os.system('python ./src/port_bind_control/TC14_152.py')
        self.assertEqual(rtn,0)

    def test_TC14_153(self):
        rtn = os.system('python ./src/port_bind_control/TC14_153.py')
        self.assertEqual(rtn,0)

    # udp 제어
    def test_TC14_246(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14246')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14246 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_246.py')
        self.assertEqual(rtn,0)

    def test_TC14_247(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14247')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14247 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_247.py')
        self.assertEqual(rtn,0)

    def test_TC14_248(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14248')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14248 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_248.py')
        self.assertEqual(rtn,0)

    def test_TC14_249(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14249')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14249 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_249.py')
        self.assertEqual(rtn,0)

    def test_TC14_250(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14250')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14250 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_250.py')
        self.assertEqual(rtn,0)
    '''
    UDP 제어에서 프로세스 명을 획득하지 못해서 주석 처리
    프로세스 명 획득 가능하도록 개선 후 활성화 필요
    def test_TC14_251(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14251')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14251 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_251.py')
        self.assertEqual(rtn,0)

    def test_TC14_252(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14252')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14252 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_252.py')
        self.assertEqual(rtn,0)
    '''
    def test_TC14_253(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14253')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14253 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_253.py')
        self.assertEqual(rtn,0)

    def test_TC14_254(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14254')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14254 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_254.py')
        self.assertEqual(rtn,0)

    def test_TC14_255(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14255')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14255 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_255.py')
        self.assertEqual(rtn,0)

    def test_TC14_256(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14256')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14256 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_256.py')
        self.assertEqual(rtn,0)

    def test_TC14_257(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14257')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14257 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_257.py')
        self.assertEqual(rtn,0)

    def test_TC14_258(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14258')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14258 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_258.py')
        self.assertEqual(rtn,0)

    def test_TC14_259(self):
        if os_platform == "Windows":
            os.system('start python src\\udp_connect_control\\udp_server.py 14259')
        else:
            os.system('python ./src/udp_connect_control/udp_server.py 14259 &')
        rtn = os.system('python ./src/udp_connect_control/TC14_259.py')
        self.assertEqual(rtn,0)
    
    
    '''
    계정 변경 - 실행할 때마다 정상실행 되는 정책이 있고 아닌 경우도 있음.. 원인 파악 필요
    def test_TC14_260(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            for tc in pfcsu_tc_list:
                os.system('python ./src/pfcsu_control/pfcsu_action.py %s'%tc)
                sleep(5)
                print("%s pass"%tc)
            sleep(120)

            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_260')
            self.assertEqual(rtn,0)

    def test_TC14_261(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_261')
            self.assertEqual(rtn,0)

    def test_TC14_262(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_262')
            self.assertEqual(rtn,0)
            
    def test_TC14_263(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_263')
            self.assertEqual(rtn,0)
            
    def test_TC14_264(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_264')
            self.assertEqual(rtn,0)
            
    def test_TC14_265(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_265')
            self.assertEqual(rtn,0)
            
    def test_TC14_266(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_266')
            self.assertEqual(rtn,0)
            
    def test_TC14_267(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_267')
            self.assertEqual(rtn,0)
            
    def test_TC14_268(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_268')
            self.assertEqual(rtn,0)
            
    def test_TC14_271(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_271')
            self.assertEqual(rtn,0)
            
    def test_TC14_272(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_272')
            self.assertEqual(rtn,0)
            
    def test_TC14_273(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_273')
            self.assertEqual(rtn,0)
            
    def test_TC14_274(self):
        if os_platform == "Windows" or variables.policy_status == "DENY":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/pfcsu_control/pfcsu_log_check.py TC14_274')
            self.assertEqual(rtn,0)
    '''
    # 시스템 제어
    def test_TC14_288(self):
        if variables.policy_status == "ALLOW":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/system_control/TC14_288.py')
        self.assertEqual(rtn,0)

    def test_TC14_289(self):
        if variables.policy_status == "ALLOW":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/system_control/TC14_289.py')
        self.assertEqual(rtn,0)
        
    def test_TC14_291(self):
        if variables.policy_status == "ALLOW":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/system_control/TC14_291.py')
        self.assertEqual(rtn,0)
        
    def test_TC14_305(self):
        if variables.policy_status == "ALLOW":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/system_control/TC14_305.py')
        self.assertEqual(rtn,0)
        
    def test_TC14_306(self):
        if variables.policy_status == "ALLOW":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/system_control/TC14_306.py')
        self.assertEqual(rtn,0)
        
    def test_TC14_308(self):
        if variables.policy_status == "ALLOW":
            self.skipTest("skip")
        else:
            rtn = os.system('python ./src/system_control/TC14_308.py')
        self.assertEqual(rtn,0)

    # 윈도우 서비스 제어
    
    def test_TC14_309(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_309.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_310(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_310.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_311(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_311.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_312(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_312.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_313(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_313.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_314(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_314.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_315(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_315.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_316(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_316.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_317(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_317.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_318(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_318.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_319(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_319.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_320(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_320.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_321(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_321.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_324(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_324.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_325(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_325.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_326(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_326.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_327(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_327.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_328(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_328.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_329(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/windows_service_control/TC14_329.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    # 이동식 디스크 제어
    def test_TC14_353(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/removale_disk_control/TC14_353.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_355(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/removale_disk_control/TC14_355.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
        
    def test_TC14_357(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/removale_disk_control/TC14_357.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
    
    #레지스트리 제어
    def test_TC14_387(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_387')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_388(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_388')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_389(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_key_add_delete.py TC14_389')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_390(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_key_add_delete.py TC14_390')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_391(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_391')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_392(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_392')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_393(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_key_add_delete.py TC14_393')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_394(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_key_add_delete.py TC14_394')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_395(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_395')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_396(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_396')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_397(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_397')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_398(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_398')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_399(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_399')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_400(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_400')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_401(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_401')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_402(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_402')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_403(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_403')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_406(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_406')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_407(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_407')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_408(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/TC14_408.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_409(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_409')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_410(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/registry_value_add_delete.py TC14_410')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)

    def test_TC14_411(self):
        if os_platform == "Windows":
            rtn = os.system('python ./src/registry_control/TC14_411.py')
        else:
            self.skipTest("skip")
        self.assertEqual(rtn,0)
"""