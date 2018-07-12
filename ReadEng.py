#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pyttsx
import xlrd

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)


data=xlrd.open_workbook('words.xlsx')
table=data.sheets()[0]
print '输入你需要的行数，退出输入q'

while True:
    i=input('你要念第几行？')
    engine.say(table.cell_value(i-1,0))
    engine.runAndWait()

engine.endLoop()


