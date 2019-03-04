from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def sendkeys(self,text,*loc):#输入
        el=self.driver.find_element(*loc)
        el.send_keys(text)
    def clear(self):#清空
        self.driver.clear()
    def back(self):#后退
        self.driver.back()
    def forward(self):#前进
        self.driver.forward()
    def close(self):#关闭
        self.driver.close()
    def click(self,*loc):#点击元素
        el=self.driver.find_element(*loc)
        el.click()
    def find_element(self,*loc):
        WebDriverWait(self.driver,4).until(EC.visibility_of_all_elements_located(loc))
        return self.driver.find_element(*loc)
    def get(self,url):
        self.driver.get(url)
    def jihuo(self):
        self.driver.switch_to.window(self.driver.current_window_handles)
    def jihuo1(self,i):
        self.driver.switch_to.window(self.driver.window_handles[i])
    def switch_to_inframe(self):
        el=self.driver.switch_to.frame(0)
    def get_text(self,*loc):
        dy=self.driver.find_element(*loc)
        return dy.text