from testsuists.base_testcase import BaseTestCase
from pageobjects.discuzPage4 import DiscuzPage4
import unittest,time
class Discuz4TestCase(BaseTestCase):
    def testDiscuz1(self):
        testdiscuz4=DiscuzPage4(self.driver)
        testdiscuz4.login("lxc","lxc960301")
        testdiscuz4.defaultbk()
        time.sleep(2)
        testdiscuz4.sendTp()
        testdiscuz4.touPiao("今天出了什么毛病","窗口跳转","ifram定位","log日志")
        testdiscuz4.touPiao1()
if __name__=='__main__':
    unittest.main()