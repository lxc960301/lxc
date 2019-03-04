from testsuists.base_testcase import BaseTestCase
from pageobjects.discuzPage1 import DiscuzPage1
import unittest,time
class Discuz1TestCase(BaseTestCase):
    def testDiscuz1(self):

        testdiscuz1=DiscuzPage1(self.driver)
        # testdiscuz1.get("http://127.0.0.1/forum.php")
        time.sleep(1)
        testdiscuz1.login("lxc","lxc960301")
        time.sleep(1)
        testdiscuz1.defaultbk()
        testdiscuz1.sendTitle("第一个帖子","不忘初心，方得始终")
        time.sleep(15)
        testdiscuz1.replyTitle("第一个回复帖子")
        time.sleep(1)
        testdiscuz1.testexit()
if __name__ == '__main__':
    unittest.main()
