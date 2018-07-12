#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from Translatorme import *
import pyttsx


speak_engine = pyttsx.init()
rate = speak_engine.getProperty('rate')
speak_engine.setProperty('rate', rate-30)
trans=""

with open("jb4.txt", 'r') as im:
    for line in im:
        trans=requests_for_dst(line)
        print(line)
        print(trans)
        speak_engine.say(line+trans)
        speak_engine.runAndWait()




