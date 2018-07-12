#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from Functions import *

from Tkinter import *

class Application():

    def __init__(self):

        def searchFunc():
            eng = self.inputVAR.get()
            SpeakEng(eng)
            ch=raw_translate(eng)
            self.LableTVAR.set(eng)
            self.LableBVAR.set(ch)
            raw_input(eng+' '+ch+"\n")
            for line in datalist:
                if eng+' '+ch+"\n" in line:
                    return 0
            Listdata.insert(END,eng+' '+ch+"\n")

        file2data()

        root=Tk()
        root.title("English Review")
        root.geometry()
        #root.attributes("-alpha", 0.6)
        root.resizable(width=False,height=True)

        frmL = Frame(root)
        frmL.pack(side=LEFT)
        frmR=Frame(root)
        frmR.pack(side=RIGHT)
        frmLM=Frame(frmL)
        frmLM.grid(row=1,column=0)

        Head=Label(frmL,text='Input Unknown',font=("Times", "40", "bold italic"))
        Head.grid(row=0,column=0)

        self.inputVAR = StringVar()
        InputEntry = Entry(frmLM,textvariable=self.inputVAR,width=50)
        InputEntry.grid(row=0,column=0)

        SearchButton=Button(frmLM,text='搜索',command=searchFunc,state=ACTIVE)
        SearchButton.focus_set()
        SearchButton.grid(row=0,column=1)

        self.LableTVAR=StringVar()
        OutputT=Label(frmL,textvariable=self.LableTVAR,font=("Arial",30))
        OutputT.grid(row=2,column=0)

        self.LableBVAR=StringVar()
        OutputD=Label(frmL,textvariable=self.LableBVAR,font=("Arial",20))
        OutputD.grid(row=3,column=0)

        self.ListVAR=StringVar()
        self.ListVAR.set(tuple(datalist))
        Listdata=Listbox(frmR,listvariable=self.ListVAR,width=30)


        scrl=Scrollbar(frmR)
        scrl.pack(side=RIGHT,fill=Y)
        Listdata.configure(yscrollcommand=scrl.set)
        scrl['command']=Listdata.yview
        Listdata.pack(side=LEFT, fill=BOTH)

        root.mainloop()



if __name__=="__main__":
    main=Application()