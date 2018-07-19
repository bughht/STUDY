# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def mixurl(input):
    return 'http://fanyi.youdao.com/translate?&i=' + input + '&doctype=xml&version'

import urllib2
import re

def trans(input):
    request = urllib2.urlopen(mixurl(input))
    xml = request.read()
    p = r'[[](.*?)[]]'
    pattern = re.compile(p)
    ans = re.search(pattern, xml)
    output = re.findall(pattern, xml)[1]
    return output[6:]

if __name__=="__main__":
    inword=""
    while inword!="q":
        inword=raw_input("Translate into Chinese:")
        print trans(inword)
