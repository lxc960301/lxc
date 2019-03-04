import logging
import os.path
import time
import os
class Logger(object):
    #初始化logg对象
    def __init__(self,logger):
        #创建一个logger,获取当前的logger对象
        self.logger=logger
        self.logger=logging.getLogger(logger)
        #指定最低的日志级别
        self.logger.setLevel(logging.DEBUG)
        #创建一个handler，用于写入日志文件
        rq=time.strftime('%Y%m%d%H%M',time.localtime((time.time())))
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+rq+".log"
        fh=logging.FileHandler(log_name)

        fh.setLevel(logging.INFO)
        #创建控制台输出
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        #定义haddle输出格式
        formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #给logger添加handdle
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger
