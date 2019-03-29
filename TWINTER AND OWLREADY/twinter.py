from practnlptools.tools import Annotator
from nltk.tokenize import sent_tokenize
import re
import os
annotator=Annotator()
from Tkinter import *

window = Tk()

window.title("The Question Answering System")

window.geometry('650x300')

lbl = Label(window, text="")

#lbl.grid(column=0, row=0)
lbl.place(x = 10, y = 90, height = 95, width = 600)
txt=Entry(window,width=10)
def userText(event):
    txt.delete(0,END)
    usercheck=True

txt.insert(0,"ENTER THE QUESTION")
txt.bind("<Button>",userText)
#txt.grid(column=1, row=0)
txt.place(x = 190, y = 20, height = 25, width = 200)
def clicked():
    res =txt.get()
    s = annotator.getAnnotations(res)['srl']
    with open('SENT.txt', 'w') as f:
        f.write("%s" %res)
    st5=" "
    lbl.configure(text="\n")
    with open('SRL.txt', 'w') as f:
        for item in s:
            st = str(item)
            st1 = st.replace("{", "")
            st2 = st1.replace("'", "")
            st3 = st2.replace("}", "")
            st4 = st3.replace(" ", " ")
            st5 = st4.replace(",", "\n")
            f.write("%s" %st5)
            print(st5)
            print("\n")
    cmd = 'python3 next.py'
    os.system(cmd)
    with open("Penalty.txt") as f:
        data = f.read()
    # data = "He sent her a letter. Mary loves him."
    sent = sent_tokenize(data, language='english')
    #print sent
    i = 0
    for data in sent:
     ck = str(data)
     ck1=ck.replace(".",".\n")
     new=lbl.cget("text")+ck1
     lbl.configure(text=new)

btn = Button(window, text="SEARCH", command=clicked)
btn.place(x = 190, y = 50, height = 25, width = 200)

#btn.grid(column=2, row=0)

window.mainloop()
