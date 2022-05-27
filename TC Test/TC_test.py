import unittest
import os
import platform
from time import sleep

os_platform = platform.system()

class TC_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.system('python ./src/TC14_init.py')

    @classmethod
    def tearDownClass(cls):
        print("")

    def test_TC14_08(self):
        rtn = os.system('python ./src/file_access_control/TC14_08.py')
        self.assertEqual(rtn,0)

    def test_TC14_09(self):
        rtn = os.system('python ./src/file_access_control/TC14_09.py')
        self.assertEqual(rtn,0)

    def test_TC14_10(self):
        rtn = os.system('python ./src/file_access_control/TC14_10.py')
        self.assertEqual(rtn,0)

    def test_TC14_11(self):
        rtn = os.system('python ./src/file_access_control/TC14_11.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_1_create(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_1_create.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_2_write(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_2_write.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_3_read(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_3_read.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_4_rename(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_4_rename.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_5_delete(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_5_delete.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_6_execute(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_6_execute.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_7_mkdir(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_7_mkdir.py')
        self.assertEqual(rtn,0)

    def test_TC14_12_8_rmdir(self):
        rtn = os.system('python ./src/file_access_control/TC14_12_8_rmdir.py')
        self.assertEqual(rtn,0)

    def test_TC14_21(self):
        rtn = os.system('python ./src/file_access_control/TC14_21.py')
        self.assertEqual(rtn,0)

    def test_TC14_22(self):
        rtn = os.system('python ./src/file_access_control/TC14_22.py')
        self.assertEqual(rtn,0)

    def test_TC14_23(self):
        rtn = os.system('python ./src/file_access_control/TC14_23.py')
        self.assertEqual(rtn,0)

    def test_TC14_24(self):
        rtn = os.system('python ./src/file_access_control/TC14_24.py')
        self.assertEqual(rtn,0)

    def test_TC14_25(self):
        rtn = os.system('python ./src/file_access_control/TC14_25.py')
        self.assertEqual(rtn,0)

    def test_TC14_26(self):
        rtn = os.system('python ./src/file_access_control/TC14_26.py')
        self.assertEqual(rtn,0)

    def test_TC14_27(self):
        rtn = os.system('python ./src/file_access_control/TC14_27.py')
        self.assertEqual(rtn,0)

    def test_TC14_30(self):
        rtn = os.system('python ./src/file_access_control/TC14_30.py')
        self.assertEqual(rtn,0)

    def test_TC14_31(self):
        rtn = os.system('python ./src/file_access_control/TC14_31.py')
        self.assertEqual(rtn,0)

    def test_TC14_32(self):
        rtn = os.system('python ./src/file_access_control/TC14_32.py')
        self.assertEqual(rtn,0)

#예외 정책 테스트는 TC14_38 ~ TC14_60 으로 대체
#    def test_TC14_33(self):
#        rtn = os.system('python ./src/file_access_control/TC14_33.py')
#        self.assertEqual(rtn,0)
  
    def test_TC14_34(self):
        rtn = os.system('python ./src/file_access_control/TC14_34.py')
        self.assertEqual(rtn,0)
  
    def test_TC14_35(self):
        rtn = os.system('python ./src/file_access_control/TC14_35.py')
        self.assertEqual(rtn,0)

    def test_TC14_38(self):
        rtn = os.system('python ./src/file_access_control/TC14_38.py')
        self.assertEqual(rtn,0)

    def test_TC14_39(self):
        rtn = os.system('python ./src/file_access_control/TC14_39.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_1_create(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_1_create.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_2_write(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_2_write.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_3_read(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_3_read.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_4_rename(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_4_rename.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_5_delete(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_5_delete.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_6_execute(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_6_execute.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_7_mkdir(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_7_mkdir.py')
        self.assertEqual(rtn,0)

    def test_TC14_40_8_rmdir(self):
        rtn = os.system('python ./src/file_access_control/TC14_40_8_rmdir.py')
        self.assertEqual(rtn,0)

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

    def test_TC14_61(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14610')
        else:
            os.system('python ./src/tcp_server.py 14610 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_61.py')
        self.assertEqual(rtn,0)

    def test_TC14_62(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14620')
        else:
            os.system('python ./src/tcp_server.py 14620 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_62.py')
        self.assertEqual(rtn,0)

    def test_TC14_63(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14630')
        else:
            os.system('python ./src/tcp_server.py 14630 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_63.py')
        self.assertEqual(rtn,0)

    def test_TC14_245(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14245')
        else:
            os.system('python ./src/tcp_server.py 14245 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_245.py')
        self.assertEqual(rtn,0)

    def test_TC14_64(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14640')
        else:
            os.system('python ./src/tcp_server.py 14640 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_64.py')
        self.assertEqual(rtn,0)

    def test_TC14_66(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14660')
        else:
            os.system('python ./src/tcp_server.py 14660 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_66.py')
        self.assertEqual(rtn,0)

    def test_TC14_67(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14670')
        else:
            os.system('python ./src/tcp_server.py 14670 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_67.py')
        self.assertEqual(rtn,0)

    def test_TC14_68(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14680')
        else:
            os.system('python ./src/tcp_server.py 14680 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_68.py')
        self.assertEqual(rtn,0)

    def test_TC14_69(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14690')
        else:
            os.system('python ./src/tcp_server.py 14690 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_69.py')
        self.assertEqual(rtn,0)

    def test_TC14_70(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14700')
        else:
            os.system('python ./src/tcp_server.py 14700 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_70.py')
        self.assertEqual(rtn,0)

    def test_TC14_71(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14710')
        else:
            os.system('python ./src/tcp_server.py 14710 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_71.py')
        self.assertEqual(rtn,0)

    def test_TC14_72(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14720')
        else:
            os.system('python ./src/tcp_server.py 14720 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_72.py')
        self.assertEqual(rtn,0)

    def test_TC14_73(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14730')
        else:
            os.system('python ./src/tcp_server.py 14730 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_73.py')
        self.assertEqual(rtn,0)

    def test_TC14_74(self):
        if os_platform == "Windows":
            os.system('start python src\\tcp_server.py 14740')
        else:
            os.system('python ./src/tcp_server.py 14740 &')
        rtn = os.system('python ./src/tcp_connect_control/TC14_74.py')
        self.assertEqual(rtn,0)

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
    
    def test_TC14_100(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_100')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_100.py')
            self.assertEqual(rtn,0)

    def test_TC14_101(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_101')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_101.py')
            self.assertEqual(rtn,0)

    def test_TC14_102(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_102')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_102.py')
            self.assertEqual(rtn,0)

    def test_TC14_103(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_103')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_103.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_1_create(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_104_1_create')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_1_create.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_2_write(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_104_2_write')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_2_write.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_3_read(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_104_3_read')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_3_read.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_4_rename(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_104_4_rename')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_4_rename.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_5_delete(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_104_5_delete')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_5_delete.py')
            self.assertEqual(rtn,0)

    def test_TC14_104_6_execute(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_104_6_execute.sh')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_104_6_execute.py')
            self.assertEqual(rtn,0)

    def test_TC14_110(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_110')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_110.py')
            self.assertEqual(rtn,0)

    def test_TC14_111(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_111')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_111.py')
            self.assertEqual(rtn,0)

    def test_TC14_112(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_112')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_112.py')
            self.assertEqual(rtn,0)

    def test_TC14_113(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_113')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_113.py')
            self.assertEqual(rtn,0)

    def test_TC14_114(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_114')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_114.py')
            self.assertEqual(rtn,0)

    def test_TC14_115(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_115')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_115.py')
            self.assertEqual(rtn,0)

    def test_TC14_116(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_116')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_116.py')
            self.assertEqual(rtn,0)

    def test_TC14_119(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_119')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_119.py')
            self.assertEqual(rtn,0)

    def test_TC14_120(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_120')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_120.py')
            self.assertEqual(rtn,0)

    def test_TC14_121(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_121')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_121.py')
            self.assertEqual(rtn,0)

    def test_TC14_122(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_122')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_122.py')
            self.assertEqual(rtn,0)

    def test_TC14_123(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_123')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_123.py')
            self.assertEqual(rtn,0)

    def test_TC14_124(self):
        if os_platform == "Windows":
            self.skipTest("skip")
        else:
            os.system('chmod u+s /home/jenkins/sharedspace/DBSAFER_OS/TC Test/test_file/posix/TC14_124')
            rtn = os.system('python ./src/setuid_file_access_control/TC14_124.py')
            self.assertEqual(rtn,0)

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

