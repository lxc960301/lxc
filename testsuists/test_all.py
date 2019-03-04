import unittest
import HTMLTestRunner
import os
import sys
sys.path.append("E:/04/04python/Discuz")
from testsuists.test_discuz1 import Discuz1TestCase
from testsuists.test_discuz2 import Discuz2TestCase
from testsuists.test_discuz3 import Discuz3TestCase
from testsuists.test_discuz4 import Discuz4TestCase
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"resport")
if not os.path.exists(report_path):
    os.mkdir(report_path)
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Discuz1TestCase))
suite.addTest(unittest.makeSuite(Discuz2TestCase))
suite.addTest(unittest.makeSuite(Discuz3TestCase))
suite.addTest(unittest.makeSuite(Discuz4TestCase))
if __name__=="__main__":
    html_report=report_path + r"\result.html"
    fb=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fb,verbosity=2,
        title="单元测试报告",description="用例执行情况")
    runner.run(suite)