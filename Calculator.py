
# coding: utf-8


from tkinter import *
from tkinter import font as tkfont
from math import *

win= Tk()
win.configure(bg="black")
win.title("Calculator")

history= Entry(win,width=40,borderwidth=2,justify="right",bg="#1a1a1a",fg="white")
history.grid(row=0,column=0,columnspan=3,ipady=5)

his= Label(win,text="<--History",bg="black",fg="white")
his.grid(row=0,column=3)

e= Entry(win,width=40,borderwidth=2,justify="right",bg="#1a1a1a",fg="white")
e.grid(row=1,column=0,columnspan=3,ipady=10)

# functions

def his(numbe):
    if numbe=="pm":
        g=history.get()
        history.delete(0,END)
        try:
            history.insert(0,-int(g))
        except:
            history.insert(0,-float(g))
    elif numbe=="pt":
        g=history.get()
        history.delete(0,END)
        if g=="":
            history.insert(0,g)
        else:
            try:
                history.insert(0,sqrt(int(g)))
            except:
                history.insert(0,sqrt(float(g)))
    elif numbe=="pr":
        g=history.get()
        history.delete(0,END)
        if g=="":
            history.insert(0,g)
        else:
            try:
                history.insert(0,pow(int(g)),2)
            except:
                history.insert(0,pow(float(g),2))

    else:
        current=history.get()
        history.delete(0,END)
        history.insert(0,str(current)+str(numbe))


def squa():
    hist="on"
    curreny= e.get()
    global k
    k="no"
    e.delete(0,END)
    if curreny=="":
        e.insert(0,curreny)
    else:
        try:
            a=int(curreny)
            e.insert(0,pow(a,2))
        except:
            a=float(curreny)
            e.insert(0,pow(a,2))
        
def c():
    first_number=''
    e.delete(0,END)
    history.delete(0,END)
    
def pm():
    curreny= e.get()
    global a
    e.delete(0,END)
    if curreny=="":
        e.insert(0,curreny)
    else:
        try:
            a=-int(curreny)
            e.insert(0,(a))
        except:
            a=-float(curreny)
            e.insert(0,(a))
        
def rot():
    ab=e.get()
    e.delete(0,END)
    global k
    k="no"
    if ab=="":
        e.insert(0,ab)
    else:    
        try:
            ac=int(ab)
            e.insert(0,sqrt(ac))
        except:
            ad=float(ab)
            e.insert(0,sqrt(ad))

global k
k="ok"        
def click(number):
    global k
    if k=="no":
        c()
        k="ok"
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))
    else:
        k="ok"
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))
        

def clear():
    e.delete(0,END)

def add():
    global first_number
    global math
    global k
    k="ok"
    math= "addition"
    first_number=e.get()
    e.delete(0,END)
    
def sub():
    global first_number
    global math
    global k
    k="ok"
    math= "subtraction"
    first_number=e.get()
    e.delete(0,END)
    
def multiply():
    global first_number
    global math
    global k
    k="ok"
    math= "multiply"
    first_number=e.get()
    e.delete(0,END)
    
def divide():
    global first_number
    global math
    global k
    k="ok"
    math= "divide"
    first_number=e.get()
    e.delete(0,END)
    
def equal():
    second_num= e.get()
    e.delete(0,END)
    global k
    k="no"
    global hist
    try:
        if math=="addition":
            try:
                e.insert(0,int(first_number)+int(second_num))
            except:
                e.insert(0,float(first_number)+float(second_num))

        elif math=="subtraction":
            try:
                e.insert(0,int(first_number)-int(second_num))
            except:
                e.insert(0,float(first_number)-float(second_num))

        elif math=="multiply":
            try:
                e.insert(0,int(first_number)*int(second_num))
            except:
                e.insert(0,float(first_number)*float(second_num))

        elif math=="divide":
            try:
                try:
                    e.insert(0,int(first_number)/int(second_num))
                except:
                    e.insert(0,float(first_number)/float(second_num))
            except:
                e.insert(0,"You cannot divide by zero!")
    except:
        e.delete(0,END)
        

        
# Buttons

root=Button(win,text="√x",width=10,height=3,activebackground="grey",bg="black",fg="white",command=lambda:[rot(),his("pt")])
root.grid(row=2,column=0)

sq= Button(win,text="x²",width=10,height=3,activebackground="grey",bg="black",fg="white",command=lambda:[squa(),his("pr")])
sq.grid(row=2,column=1)

C= Button(win,text="C",width=10,height=3,activebackground="grey",bg="black",fg="white",command=c)
C.grid(row=2,column=2)

divi=Button(win,text="÷",width=10,height=3,activebackground="grey",command=lambda:[divide(),his('/')],bg="black",fg="white")
divi.grid(row=2,column=3)

seven= Button(win,text="7",width=10,height=3,activebackground="grey",command=lambda:[click(7),his(7)],bg="black",fg="white")
seven.grid(row=3,column=0)

eight= Button(win,text="8",width=10,height=3,activebackground="grey",command=lambda: [click(8),his(8)],bg="black",fg="white")
eight.grid(row=3,column=1)

nine= Button(win,text="9",width=10,height=3,activebackground="grey",command=lambda: [click(9),his(9)],bg="black",fg="white")
nine.grid(row=3,column=2)

multi= Button(win,text="×",width=10,height=3,activebackground="grey",command=lambda:[multiply(),his('×')],bg="black",fg="white")
multi.grid(row=3,column=3)

four=Button(win,text="4",width=10,height=3,activebackground="grey",command=lambda: [click(4),his(4)],bg="black",fg="white")
four.grid(row=4,column=0)

five=Button(win,text="5",width=10,height=3,activebackground="grey",command=lambda: [click(5),his(5)],bg="black",fg="white")
five.grid(row=4,column=1)

six=Button(win,text="6",width=10,height=3,activebackground="grey",command=lambda: [click(6),his(6)],bg="black",fg="white")
six.grid(row=4,column=2)

minus=Button(win,text="-",width=10,height=3,activebackground="grey",command= lambda:[sub(),his('-')],bg="black",fg="white")
minus.grid(row=4,column=3)

one=Button(win,text="1",width=10,height=3,activebackground="grey",command=lambda: [click(1),his(1)],bg="black",fg="white")
one.grid(row=5,column=0)

two=Button(win,text="2",width=10,height=3,activebackground="grey",command=lambda: [click(2),his(2)],bg="black",fg="white")
two.grid(row=5,column=1)

three=Button(win,text="3",width=10,height=3,activebackground="grey",command=lambda: [click(3),his(3)],bg="black",fg="white")
three.grid(row=5,column=2)

plus=Button(win,text="+",width=10,height=3,activebackground="grey",command=lambda:[add(),his('+')],bg="black",fg="white")
plus.grid(row=5,column=3)

plusmin=Button(win,text="+/-",width=10,height=3,activebackground="grey",bg="black",fg="white",command=lambda:[pm(),his("pm")])
plusmin.grid(row=6,column=0)

zero=Button(win,text="0",width=10,height=3,activebackground="grey",command=lambda:[click(0), his(0)],bg="black",fg="white")
zero.grid(row=6,column=1)

dot=Button(win,text=".",width=10,height=3,activebackground="grey",command=lambda:[click("."),his('.')],bg="black",fg="white")
dot.grid(row=6,column=2)


equal=Button(win,text="=",width=10,height=3,activebackground="black",activeforeground="white",command=equal,bg="grey",fg="white")
equal.grid(row=6,column=3)

clear=Button(win,text="Clear",width=10,height=2,activebackground="grey",command=clear,bg="black",fg="white")
clear.grid(row=1,column=3)


win.mainloop()


