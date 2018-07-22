# -*- coding: utf-8 -*-

class test(object):

    """Docstring for test. """

    data=[]

    def out(self):
        print self.value
        print self.data

    def __init__(self,tag):
        """TODO: to be defined1. """
        self.value=tag
        for i in range(tag):
            new=raw_input("Value"+str(i+1))
            self.data.append(new)

list=[]
a=test(3)
a.out()

for i in range(2):
    new=test(i)
    list.append(new)

print list
for i in range(2):
    list[i].out()
