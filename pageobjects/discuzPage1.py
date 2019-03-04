from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger
logger=Logger(logger="DiscuzPage1").getlog()
class DiscuzPage1(BasePage):
    discuz_input_username_loc=(By.NAME,"username")#用户名dw
    discuz_input_password_loc=(By.NAME,"password")#密码dw
    discuz_button_login_loc=(By.CSS_SELECTOR,".fastlg_l em")#登陆buttondw
    discuz_button_mrbode_loc = (By.CSS_SELECTOR, ".fl_tb h2 a") #默认板块
    discuz_input_title_loc = (By.CSS_SELECTOR, ".pbt input")  # 主题
    discuz_input_body_loc = (By.CSS_SELECTOR, ".area .pt")  # 内容
    discuz_button_send_loc = (By.CSS_SELECTOR, ".ptm .pn")  # 点击发表帖子
    discuz_input_reply_loc = (By.CSS_SELECTOR, ".pt")  # 回复内容
    discuz_button_reply_loc = (By.CSS_SELECTOR, ".ptm .pn")  # 发表回复
    discuz_button_exit_loc=(By.LINK_TEXT,"退出")#退出


    #登录
    def login(self,content1,content2):
        self.sendkeys(content1,*self.discuz_input_username_loc)#用户名
        logger.info("输入用户名：")
        self.sendkeys(content2,*self.discuz_input_password_loc)#密码
        self.click(*self.discuz_button_login_loc)#登陆
#默认板块
    def defaultbk(self):
        self.click(*self.discuz_button_mrbode_loc)#默认板块
#发表
    def sendTitle(self,content3,content4):
        self.sendkeys(content3,*self.discuz_input_title_loc)#主题
        self.sendkeys(content4,*self.discuz_input_body_loc)#内容
        self.click(*self.discuz_button_send_loc)#发表帖子
        time.sleep(15)
#回复
    def replyTitle(self,content5):
        self.sendkeys(content5,*self.discuz_input_reply_loc)#回复内容
        self.click(*self.discuz_button_reply_loc)#发表回复
#退出
    def testexit(self):
        self.click(*self.discuz_button_exit_loc)


