#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import re

def mix(input):
    return 'http://fanyi.youdao.com/translate?&i='+input+'&doctype=xml&version'

def trans(input):
    request=urllib2.urlopen(mix(input))
    xml=request.read()
    p=r'[[](.*?)[]]'
    pattern=re.compile(p)
    ans=re.search(pattern,xml)
    output=re.findall(pattern,xml)[1]
    return output[6:]


if __name__=="__main__":
    print trans('debug')