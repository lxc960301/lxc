from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
logger=Logger(logger="DiscuzPage4").getlog()
import time
class DiscuzPage4(BasePage):
    discuz_input_username_loc = (By.NAME, "username")  # 用户名dw
    discuz_input_password_loc = (By.NAME, "password")  # 密码dw
    discuz_button_login_loc = (By.CSS_SELECTOR, ".fastlg_l em")  # 登陆buttondw
    discuz_button_mrbode_loc = (By.CSS_SELECTOR, "tr:nth-child(4) td:nth-child(2) h2 a")  # 默认板块
    discuz_button_sendtz_loc=(By.ID,"newspecialtmp")#发帖按钮
    discuz_button_sendtp_loc=(By.LINK_TEXT,"发起投票")#发起投票

    discuz_input_tptitle_loc=(By.CSS_SELECTOR,"#subject")#主题
    discuz_input_tpbody1_loc=(By.CSS_SELECTOR,"#pollm_c_1 p:nth-child(1) input")#第一个投票文本框
    discuz_input_tpbody2_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(2) input")  # 第二个投票文本框
    discuz_input_tpbody3_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(3) input")  # 第三个投票文本框
    discuz_button_clicktp_loc=(By.NAME,"topicsubmit")#点击投票按钮
    discuz_button_xz1_loc=(By.CSS_SELECTOR,"#option_1")#选择第一个
    discuz_button_clickxz_loc=(By.CSS_SELECTOR,"#pollsubmit")#点击投票
    discuz_text_getzt_loc=(By.CSS_SELECTOR,"#thread_subject")#获得主题
    discuz_text_getbody1_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(1) > td.pvt")#获取第一个值
    discuz_text_getbody2_loc = (By.CSS_SELECTOR, "#poll > div.pcht > table > tbody > tr:nth-child(3) > td.pvt > label")  # 获取第二个值
    discuz_text_getbody3_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(5) > td.pvt > label")#获取第三个值
    discuz_text_bilv1_loc=(By.CSS_SELECTOR,"#poll > div.pcht > table > tbody > tr:nth-child(2) > td:nth-child(2)")#第一个bilv
    discuz_text_bilv2_loc = (By.CSS_SELECTOR, "#poll > div.pcht > table > tbody > tr:nth-child(4) > td:nth-child(2)")  # 第二个bilv
    discuz_text_bilv3_loc = (By.CSS_SELECTOR, "#poll > div.pcht > table > tbody > tr:nth-child(6) > td:nth-child(2)")  # 第三个bilv




#登录
    def login(self,username,password):
        self.sendkeys(username,*self.discuz_input_username_loc)#用户名
        self.sendkeys(password,*self.discuz_input_password_loc)#密码
        self.click(*self.discuz_button_login_loc)#登陆
        logger.info("登陆")
#默认板块
    def defaultbk(self):
        time.sleep(2)
        self.click(*self.discuz_button_mrbode_loc)#默认板块
        logger.info("默认板块")
#发起投票
    def sendTp(self):
        time.sleep(2)
        self.click(*self.discuz_button_sendtz_loc)#点击发帖按钮
        logger.info("发帖")
        time.sleep(2)
        self.click(*self.discuz_button_sendtp_loc)#点击发表投票
        time.sleep(2)
        logger.info("发起投票")
#进行投票
    def touPiao(self,tptitle,tpbody1,tpbody2,tpbody3):
        self.sendkeys(tptitle,*self.discuz_input_tptitle_loc)#主题
        logger.info("主题")
        self.sendkeys(tpbody1,*self.discuz_input_tpbody1_loc)#第一个投票文本框
        self.sendkeys(tpbody2, *self.discuz_input_tpbody2_loc)# 第二个投票文本框
        self.sendkeys(tpbody3, *self.discuz_input_tpbody3_loc)# 第三个投票文本框
        self.click(*self.discuz_button_clicktp_loc)#点击投票按钮
        logger.info("点击投票")
    def touPiao1(self):
        time.sleep(1)
        self.click(*self.discuz_button_xz1_loc)#选择第一个
        self.click(*self.discuz_button_clickxz_loc)#点击投票按钮
        time.sleep(1)
        a1=self.get_text(*self.discuz_text_getbody1_loc)#获得第一个值
        b1=self.get_text(*self.discuz_text_bilv1_loc)#第一个比率
        a2=self.get_text(*self.discuz_text_getbody2_loc)  # 获得第二个值
        b2=self.get_text(*self.discuz_text_bilv2_loc)#第二个比率
        a3=self.get_text(*self.discuz_text_getbody3_loc)  # 获得第三个值
        b3=self.get_text(*self.discuz_text_bilv3_loc)#第三个比率
        zhuti=self.get_text(*self.discuz_text_getzt_loc)#zhuti
        print("第一个选项：",a1,"比率：",b1)
        logger.info("第一个选项：%s"%a1)
        logger.info("第一个比率：%s"%b1)
        print("第一个选项：", a2, "比率：", b2)
        logger.info("第一个选项：%s" % a2)
        logger.info("第一个比率：%s" % b2)
        print("第一个选项：", a3, "比率：", b3)
        logger.info("第一个选项：%s" % a3)
        logger.info("第一个比率：%s" % b3)
        print("主题：",zhuti)
        logger.info("主题：%s"%zhuti)