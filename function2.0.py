# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import pyttsx
import re
import urllib2
import random
import os
from cmd import Cmd


class Client(Cmd):
    prompt = 'STUDY>'
    intro = 'Demo Beta 0.1'
    data_raw = []
    data_sel = []

    def __init__(self):
        Cmd.__init__(self)

    def do_import(self, input):
        self.load_raw(input)
        print len(self.data_raw)

    def do_select(self, input):
        self.select(input)

    def do_list(self, heads):
        self.printtrans(self.data_raw)

    def do_train(self, input):
        self.train(input)

    def do_exit(self, arg):
        print 'Bye!'
        return True  # 返回True，直接输入exit命令将会退出

    def default(self, line):
        print 'There\'s something wrong'

    def emptyline(self):
        print 'please input command!'

    def mixurl(self, input):
        return 'http://fanyi.youdao.com/translate?&i=' + input + '&doctype=xml&version'

    def trans(self, input):
        request = urllib2.urlopen(self.mixurl(input))
        xml = request.read()
        p = r'[[](.*?)[]]'
        pattern = re.compile(p)
        ans = re.search(pattern, xml)
        output = re.findall(pattern, xml)[1]
        return output[6:]

    def speak(self, input):
        speak_engine = pyttsx.init()
        rate = speak_engine.getProperty('rate')
        speak_engine.setProperty('rate', rate - 50)
        speak_engine.say(input)
        speak_engine.runAndWait()
        speak_engine.stop()

    def load_raw(self, input):
        with open(input, 'r') as _DATA:
            for line in _DATA:
                if line != "":
                    self.data_raw.append(" ".join(line.split()))
        self.data_raw.sort()
        _DATA.close()

    def select(self, heads):
        for ele in self.data_raw:
            if ele == '':
                continue
            if ele[0] in heads + self.fnn(heads):
                self.data_sel.append(ele)

    def printtrans(self, IN_list):
        for ele in IN_list:
            sys.stdout.write(ele + ' ' + self.trans(ele)+'\n')

    def fnn(self, input):
        def fn(x):
            if x.islower():
                return x.upper()
            elif x.isupper():
                return x.lower()
            else:
                return x

        return ''.join([fn(r) for r in list(input)])

    def train(self, times):
        for i in range(1, times):
            out = self.data_sel[random.randint(0, len(self.data_sel) - 1)]
            sys.stdin.write(self.trans(out)+"\n")
            sys.stdin.write(out+"\n")


if __name__ == "__main__":
    try:
        os.system('cls')
        client = Client()
        client.cmdloop()
    except:
        exit()
