from framework.browser_engine import BrowserEngine
import unittest
import time
browser=BrowserEngine()
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # self.driver=browser.open_browser()
        self.driver=browser.open_browser()
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(2)
    def tearDown(self):
        time.sleep(2)
        # self.driver=browser.exit_browser()
        self.driver=browser.quit_browser()

