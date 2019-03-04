from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time
class DiscuzPage3(BasePage):
    discuz_input_username_loc = (By.NAME, "username")  # 用户名dw
    discuz_input_password_loc = (By.NAME, "password")  # 密码dw
    discuz_button_login_loc = (By.CSS_SELECTOR, ".fastlg_l em")  # 登陆buttondw
    discuz_input_tiezi_loc=(By.CSS_SELECTOR,".scbar_txt_td input")#帖子输入
    discuz_button_select_loc=(By.CSS_SELECTOR,".scbar_btn_td button")#帖子按钮
    discuz_button_intotz_loc=(By.CSS_SELECTOR,".xs3 a")#进入帖子
    discuz_select_haotest_loc=(By.CSS_SELECTOR,".ts span")#帖子标题

    #登陆
    def login(self,username,password):
        self.sendkeys(username,*self.discuz_input_username_loc)
        self.sendkeys(password,*self.discuz_input_password_loc)
        self.click(*self.discuz_button_login_loc)
    #搜索
    def select(self,tiezi):
        self.sendkeys(tiezi,*self.discuz_input_tiezi_loc)
        self.click(*self.discuz_button_select_loc)
    #进入帖子
    def intotz(self):
        self.jihuo1(1)
        self.click(*self.discuz_button_intotz_loc)
        time.sleep(1)
        self.jihuo1(2)
    def DuanYan(self):
        duanyan=self.get_text(*self.discuz_select_haotest_loc)
        return duanyan

