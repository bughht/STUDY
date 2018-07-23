# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import re
import pickle
import os

listall=[]

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

class EXCIT(object):
    def output(self,place):
        print "["+str(place+1)+"] "+self.trans
        for i in range(0,self.count):
            print(str(i+1)+" "+self.words[i])

    def change(self,col,word):
        self.words[col]=word
        self.trans=trans(self.words[0])

    def __init__(self):
        self.trans=""
        self.words=[]
        self.count=int(raw_input("How Many? "))
        for i in range(0,self.count):
            new = ""
            new = raw_input(str(i+1)+":")
            self.words.append(new)
        self.trans=trans(self.words[0])

def inEXCIT():
    time=int(raw_input("HOW MANY KINDS?!:"))
    for i in range(0,time):
        new=EXCIT()
        listall.append(new)

def outEXCIT():
    for i in range(0,len(listall)):
        listall[i].output(i)

def saveEXCIT():
    with open ("HML.txt","w") as f:
        pickle.dump(listall,f)

def loadEXCIT(filename):
    with open (filename,"r") as f:
        newlist=pickle.load(f)
    for classes in newlist:
        listall.append(classes)

def debugEXCIT():
    check=int(raw_input("Times"))
    for i in range(check):
        row=int(raw_input("Which Line? "))
        col=int(raw_input("Which One? "))
        word=raw_input("Change TO? ")
        listall[row-1].change(col-1,word)

if __name__=="__main__":
    if os.path.exists("HML.txt")==True:
        loadEXCIT("HML.txt")
    outEXCIT()
    inEXCIT()
    outEXCIT()
    debugEXCIT()
    outEXCIT()
    saveEXCIT()
