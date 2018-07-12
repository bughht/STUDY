#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from Functions import *

def listener():
    while True:
        code=raw_input('>:')
        if code[0]=='q':
            sys.exit()
        if code[0]=='a':
            input(code[2:])
        if code[0]=='l':
            listall()
#        if code[0]=='i':


if __name__ == "__main__":
    file2data()
    listener()

