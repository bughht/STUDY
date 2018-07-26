# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from CPX import *
import os
import random

def train(times):
    for i in range(times):
        out=listall[random.randint(1,len(listall)-1)]
        raw_input("["+str(i+1)+"] "+out.trans+" ("+str(len(out.words))+")")
        for j in range(len(out.words)):
            print str(j+1)+" "+out.words[j]
        raw_input("Surprise?")


if __name__=="__main__":
    if os.path.exists("HML.txt")==True:
        loadEXCIT("HML.txt")
    print "there are "+str(len(listall))+" types"
    traintime=int(raw_input("How Many Times:"))
    train(traintime)

