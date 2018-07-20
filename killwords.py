# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from func_2 import *

kill_count={}

def cutfile(input,filename):
    with open(filename,'r') as r:
        lines=r.readlines()

def cuttrain(train_time):
    for time in range(1,train_time):
        out = data_sel[random.randint(0, len(data_sel) - 1)]
        raw_input(trans(out))
        result=raw_input(out+"\n"+"[y/n]:")
        if result=="y":
            data_sel.remove(out)
        else:
            if kill_count.has_key(out)==True:
                kill_count[out]=kill_count[out]+1
            else:
                kill_count[out]=1
                continue

def KILL_RESULT():
    for d,x in kill_count.items():
        print d+" "+str(x)

if __name__ == "__main__":
    cut_file=raw_input("Input Cut file:")
    load_raw(cut_file)
    letter_sel=raw_input("Head:")
    select(letter_sel)
    print "there are "+str(countsel())+" letters to kill"
    train_time=0
    train_time=int(raw_input("Times?:"))
    cuttrain(train_time)
    print ""
    KILL_RESULT()
