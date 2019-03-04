from pageobjects.discuzPage2 import DiscuzPage2
from testsuists.base_testcase import BaseTestCase
import time
import unittest
from framework.logger import  Logger
class Discuz2TestCase(BaseTestCase):
    def testDiscuz2(self):
        testdiscuz2=DiscuzPage2(self.driver)
        # testdiscuz2.get("http://127.0.0.1/forum.php")
        testdiscuz2.login("admin","123456")#管理员账户密码
        time.sleep(2)
        testdiscuz2.defaultbk()
        testdiscuz2.deleteTitle()#删除
        testdiscuz2.mangerCent()#中心
        time.sleep(2)
        testdiscuz2.surePwd("123456")
        testdiscuz2.addNewbc()
        testdiscuz2.texit()
        testdiscuz2.login("lxc","lxc960301")
        time.sleep(3)
        testdiscuz2.newBack()
        time.sleep(2)
        testdiscuz2.sendTitle("新板块发帖","帆帆帆帆帆帆帆帆")
        time.sleep(15)
        testdiscuz2.replyTitle("fffffffffffff")
if __name__=="__main__":
    unittest.main()