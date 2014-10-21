def button01_function():
    print("Has escrito")
    print("%s" % svalue.get())

def addition():
    w.insert(0,"+")
    w.pack()

def sustract():
    w.insert(0,"-")
    w.pack()

from tkinter import *

window = Tk(className="Mi primer GUI")

foo = Label(window,text="Calculadora en python")
foo.pack()

svalue = stringVar()
w = Entry(window,textvariable=svalue)
w.pack()

foo = Button(window,text="Enter",command= button01_function)
foo.pack()

foo = Button(window,text="+",command= addition)
foo.pack(side=LEFT)

window.mainloop()
