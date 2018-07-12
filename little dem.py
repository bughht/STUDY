#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import re

def add(word):
    return "http://fanyi.youdao.com/translate?&i=%22"+word+"%22&doctype=xml&version"

def translate_surprisingly(input):
    request1 = urllib2.Request(add(input))
    response = urllib2.urlopen(request1)
    passage = response.read()
    print(passage)
    pattern=re.compile(r'trans(?=\w)')
    print pattern.match(passage)

print(translate_surprisingly("fuck"))