# -*- coding: utf-8 -*-


import sys

reload(sys)
sys.setdefaultencoding('utf8')

import re
import urllib2

data_raw = []


def mixurl(input):
    return 'http://fanyi.youdao.com/translate?&i=' + input + '&doctype=xml&version'


def trans(input):
    request = urllib2.urlopen(mixurl(input))
    xml = request.read()
    p = r'[[](.*?)[]]'
    pattern = re.compile(p)
    ans = re.search(pattern, xml)
    output = re.findall(pattern, xml)[1]
    return output[6:]

def load_raw(input):
    with open(input, 'r') as _DATA:
        for line in _DATA:
            if line != "":
                data_raw.append(" ".join(line.split()))
    _DATA.close()

if __name__=="__main__":
    inname=raw_input("File Input:")
    outname=inname+"_PRO"
    load_raw(inname)
    HWL_pro=open(outname,"w")
    for ele in data_raw:
        HWL_pro.write(ele+" "+trans(ele)+"\n")
    HWL_pro.close()
