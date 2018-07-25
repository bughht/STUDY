# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from func_2 import *


if __name__=="__main__":
    filename=raw_input("file name:")
    load_raw(filename)
    printtrans(data_raw,"a")
