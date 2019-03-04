import xlrd
from framework.logger import Logger
logeger=Logger(logger="Uti").getlog()
class Uti(object):
    @classmethod
    def read_excel(self,excelPath,sheetName="sheet1"):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        keys=sheet.row_values(0)
        #获取行数
        rowNum=sheet.nrows
        #获取列数
        cloNum=sheet.ncols
