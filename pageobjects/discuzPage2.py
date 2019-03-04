from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger
logger=Logger(logger="DiscuzPage2").getlog()
class DiscuzPage2(BasePage):
    discuz_input_username_loc=(By.NAME,"username")#用户名dw
    discuz_input_password_loc=(By.NAME,"password")#密码dw
    discuz_button_login_loc=(By.CSS_SELECTOR,".fastlg_l em")#登陆buttondw
    discuz_button_mrbode_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")  # 默认板块
    discuz_button_deletgou_loc = (By.CSS_SELECTOR, "tbody:nth-child(2) td:nth-child(2)")  # 删除选择勾
    discuz_button_deletbutton_loc = (By.LINK_TEXT, "删除")  # 删除按钮
    discuz_button_queding_loc = (By.CSS_SELECTOR, ".o .pn")  # 确定按钮
    discuz_button_mgercenter_loc = (By.LINK_TEXT, "管理中心")  # 管理中心
    discuz_input_userpsd_loc = (By.NAME, "admin_password")  # 确认密码
    discuz_button_upadmit_loc = (By.NAME, "submit")  # 提交
    discuz_button_luntan_loc = (By.CSS_SELECTOR, ".nav li:nth-child(7) a")  # 论坛
    discuz_button_addnbk_loc = (By.CSS_SELECTOR, ".lastboard .addtr")  # 添加新板块
    # discuz_clear_addbknum_loc = (By.CSS_SELECTOR, ".tb tbody:nth-child(3) .td25 input")  # 清空数字
    # discuz_clear_addbkinfor_loc = (By.NAME, "newforum[1][]")  # 清空信息
    # discuz_input_addbknum_loc = (By.CSS_SELECTOR, ".tb tbody:nth-child(3) .td25 input")  # 添加数字
    # discuz_input_addbkinfor_loc = (By.NAME, "newforum[1][]")  # 添加信息
    discuz_button_addtj_loc_loc = (By.CSS_SELECTOR,"#submit_editsubmit")
    #新板块

    discuz_button_newbankuai_loc=(By.CSS_SELECTOR,"tr:nth-child(2) td h2 a")
    #退出
    discuz_input_title_loc = (By.CSS_SELECTOR, ".pbt input")  # 主题
    discuz_input_body_loc = (By.CSS_SELECTOR, ".area .pt")  # 内容
    discuz_button_send_loc = (By.CSS_SELECTOR, ".ptm .pn")  # 点击发表帖子
    discuz_input_reply_loc = (By.CSS_SELECTOR, ".pt")  # 回复内容
    discuz_button_reply_loc = (By.CSS_SELECTOR, ".ptm .pn")  # 发表回复
    discuz_button_exit_loc = (By.LINK_TEXT, "退出")
#登陆
    def login(self,content1,content2):
        self.sendkeys(content1,*self.discuz_input_username_loc)#用户名
        self.sendkeys(content2,*self.discuz_input_password_loc)#密码
        self.click(*self.discuz_button_login_loc)#登陆
#默认板块
    def defaultbk(self):
        self.click(*self.discuz_button_mrbode_loc)#默认板块
#删除
    def deleteTitle(self):
        self.click(*self.discuz_button_deletgou_loc)#删除选择勾
        time.sleep(1)
        self.click(*self.discuz_button_deletbutton_loc)#删除
        self.click(*self.discuz_button_queding_loc)#确定按钮
#管理中心
    def mangerCent(self):
        self.click(*self.discuz_button_mgercenter_loc)#管理中心
#添加模块
    def surePwd(self,surepwd):
        time.sleep(2)
        self.jihuo1(1)#激活窗口
        self.sendkeys(surepwd,*self.discuz_input_userpsd_loc)#确认密码
        self.click(*self.discuz_button_upadmit_loc)  # 提交

#论坛
    def addNewbc(self):#编号 名称
        self.jihuo1(1)  # 激活窗口
        self.click(*self.discuz_button_luntan_loc)#论坛
        time.sleep(1)
        self.switch_to_inframe()
        self.click(*self.discuz_button_addnbk_loc)#添加新模块
        # self.sendkeys(adbcnum,*self.discuz_input_addbknum_loc)#添加数字
        # self.sendkeys(adbcinfor,*self.discuz_input_addbkinfor_loc)#添加信息
        self.click(*self.discuz_button_addtj_loc_loc)#提交
        time.sleep(8)
    #退出2
    def texit(self):
        self.jihuo1(1)
        self.click(*self.discuz_button_exit_loc)
        time.sleep(4)
        self.jihuo1(1)
        self.click(*self.discuz_button_exit_loc)
        time.sleep(5)
    #新板块
    def newBack(self):
        self.click(*self.discuz_button_newbankuai_loc)
        logger.info("进入新板块")

    def sendTitle(self, content3, content4):
        self.sendkeys(content3, *self.discuz_input_title_loc)  # 主题
        logger.info("发表主题")
        self.sendkeys(content4, *self.discuz_input_body_loc)  # 内容
        self.click(*self.discuz_button_send_loc)  # 发表帖子
        time.sleep(15)

    # 回复
    def replyTitle(self, content5):
        self.sendkeys(content5, *self.discuz_input_reply_loc)  # 回复内容
        self.click(*self.discuz_button_reply_loc)  # 发表回复


#退出
    def testexit(self):
        self.click(*self.discuz_button_exit_loc)
