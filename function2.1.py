# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import pyttsx3
import re
import urllib2
import random

data_sel = []
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


def speak(input):
    speak_engine = pyttsx3.init()
    rate = speak_engine.getProperty('rate')
    speak_engine.setProperty('rate', rate - 50)
    speak_engine.say(input)
    speak_engine.runAndWait()
    speak_engine.stop()


def load_raw(input):
    with open(input, 'r') as _DATA:
        for line in _DATA:
            if line != "":
                data_raw.append(" ".join(line.split()))
    _DATA.close()


def select(heads):
    for ele in data_raw:
        if ele=='':
            continue
        if ele[0] in heads + fnn(heads):
            data_sel.append(ele)


def printtrans(IN_list,method):
    if method=="a":
        for ele in IN_list:
            print ele + ' ' + trans(ele)
    if method=="b":
        IN_list.sort()
        for ele in IN_list:
            print ele + ' ' + trans(ele)

 
    
def fnn(input):
    def fn(x):
        if x.islower():
            return x.upper()
        elif x.isupper():
            return x.lower()
        else:
            return x

    return ''.join([fn(r) for r in list(input)])


def train(times):
    for i in range(1, times):
        out = data_sel[random.randint(0, len(data_sel) - 1)]
        raw_input(trans(out))
        raw_input(out)

if __name__=="__main__":
    filename=raw_input("import your file name:")
    method=raw_input("how to translate")
    load_raw(filename+".txt")
    #printtrans(data_raw,method)
    #select('v')
    #printtrans(data_sel)
    #train(50)
    speak("hello")
