#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from Translatorme import *
import pyttsx


datalist = []
speak_engine = pyttsx.init()
rate = speak_engine.getProperty('rate')
speak_engine.setProperty('rate', rate-80)

def file2data():
    with open("DATA.data",'r') as _DATA:
        for line in _DATA:
            if line != "":
                datalist.append(line)
    _DATA.close()


def add2file(result):
    _DATA=open("DATA.data",'a')
    _DATA.write(result)
    _DATA.close()

def raw_translate(eng):
    return(requests_for_dst(eng))

def translate(eng):
    ch = requests_for_dst(eng)
    return eng+' '+ch+"\n"


def checkindata(eng):
    result=translate(eng)
    print result
    for line in datalist:
        if eng in line:
            print line
            return True
    return result


def input(eng):
    SpeakEng(eng)
    ans=checkindata(eng)
    if ans == True:
        print 'exsisted'
    else:
        add2file(ans)

def raw_input(all):
    for line in datalist:
        if all in line:
            print line
            return 0
    add2file(all)

def SpeakEng(eng):
    speak_engine.say(eng)
    speak_engine.runAndWait()


def listall():
    with open("DATA.data",'r') as _DATA:
        for line in _DATA:
            print line


if __name__ == "__main__":
    print 'helloworld'
    file2data()
    input("developer")
    listall()