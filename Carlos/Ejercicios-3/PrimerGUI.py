def button01_function():
    print("Has escrito: ")
    print('%s' % svalue.get())

def addition():
    w.insert(0,"+")
    w.pack()

def sustract():
    w.insert(0,"-")
    w.pack()

def multiply():
    w.insert(0,"*")
    w.pack()

def divide():
    w.insert(0,"/")
    w.pack()

def result():
    k = 0
    variable = svalue.get()
    for i in range (0,len(variable)):
        if not variable[k].isdigit():
            print("no es un numero")
            
        else:
            print("1")
        k = k+1
    

from tkinter import *


window = Tk(className="Primer GUI")

foo = Label(window,text="Calculadora en Python")
foo.pack()

svalue = StringVar()
w = Entry(window,textvariable=svalue)
w.pack()

foo = Button(window,text="Enter",command= button01_function)
foo.pack()

foo = Button(window,text="+",command= addition)
foo.pack(padx=5,side=LEFT)

foo = Button(window,text="-",command= sustract)
foo.pack(padx=5,side=LEFT)

foo = Button(window,text="*",command= multiply)
foo.pack(padx=5,side=LEFT)

foo = Button(window,text="/",command= divide)
foo.pack(padx=5,side=LEFT)

foo = Button(window,text="=",command= result)
foo.pack(padx=5,side=LEFT)

window.mainloop()

#     len(svalue)
