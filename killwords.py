# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from func_2 import *

def cutfile(input,filename):
    with open(filename,'r') as r:
        lines=r.readlines()
    with open(filename,'w') as w:
        for l == lines:
            if input not in l:
                w.write(l)

if __name__=="__main__":
    cut_file=raw_input("Input Cut file:")
    load_file(cut_file)
    letter_sel=raw_input("Head:")
    select(letter_sel)
    print "there are "+str(countsel())+" letters to kill"
    train_time=0
    train_time=int(raw_input("Times?:"))
    train(train_time)
