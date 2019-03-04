from pageobjects.discuzPage3 import DiscuzPage3
from testsuists.base_testcase import BaseTestCase
from framework.logger import Logger
logger=Logger(logger="Discuz3Page").getlog()
import time
import unittest
class Discuz3TestCase(BaseTestCase):
    def testDiscuz3(self):
        testdiscuz3=DiscuzPage3(self.driver)
        testdiscuz3.get("http://127.0.0.1/forum.php")
        testdiscuz3.login("admin","123456")#管理员账户密码
        time.sleep(1)
        testdiscuz3.select("haotest")#搜索haotest
        time.sleep(2)
        testdiscuz3.intotz()#进入haotest
        time.sleep(1)
        duanYan=testdiscuz3.DuanYan()
        try:
            self.assertEqual(duanYan,"haotest",msg=duanYan)
            logger.info("断言成功：%s"%duanYan)
        except:
            logger.info("断言失败")


if __name__ == '__main__':
    unittest.main()
