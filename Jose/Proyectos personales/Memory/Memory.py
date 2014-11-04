from tkinter import *
import time

ventana = Tk()

pink = 0
blue = 0
green = 0
counter = 0

def cmai():
    global pink
    ai = Button(ventana, image=aii, width=64, height=64)
    ai.grid(row=0, column=0)
    pink = pink + 1
def cmac():
    global green
    ac = Button(ventana, image=aci, width=64, height=64)
    ac.grid(row=0, column=1)
    green = green + 1
def cmad():
    global blue
    ad = Button(ventana, image=adi, width=64, height=64)
    ad.grid(row=0, column=2)
    blue = blue + 1
def cmdi():
    global green
    di = Button(ventana, image=dii, width=64, height=64)
    di.grid(row=2, column=0)
    green = green + 1
def cmdc():
    global blue
    dc = Button(ventana, image=dci, width=64, height=64)
    dc.grid(row=2, column=1)
    blue = blue + 1
def cmdd():
    global pink
    dd = Button(ventana, image=ddi, width=64, height=64)
    dd.grid(row=2, column=2)
    pink = pink + 1
def reset():
    if not pinkfix:
        ai = Button(ventana, image=white, command=cmai, width=64, height=64)
        dd = Button(ventana, image=white, command=cmdd, width=64, height=64)
        ai.grid(row=0, column=0)
        dd.grid(row=2, column=2)
        pink = 0
    if not greenfix:
        ac = Button(ventana, image=white, command=cmac, width=64, height=64)
        di = Button(ventana, image=white, command=cmdi, width=64, height=64)
        ac.grid(row=0, column=1)
        di.grid(row=2, column=0)
        pink = 0
    if not bluefix:
        ad = Button(ventana, image=white, command=cmad, width=64, height=64)
        dc = Button(ventana, image=white, command=cmdc, width=64, height=64)
        ad.grid(row=0, column=2)
        dc.grid(row=2, column=1)
        pink = 0
def loop():
    global counter
    for i in range(100000000):
        counter = counter + 1
        print(counter)
        time.sleep(1)
        
aii = PhotoImage(file="pink.png")
aci = PhotoImage(file="green.png")
adi = PhotoImage(file="blue.png")
dii = PhotoImage(file="green.png")
dci = PhotoImage(file="blue.png")
ddi = PhotoImage(file="pink.png")
white = PhotoImage(file="white.png")

ai = Button(ventana, image=white, command=cmai, width=64, height=64)
ac = Button(ventana, image=white, command=cmac, width=64, height=64)
ad = Button(ventana, image=white, command=cmad, width=64, height=64)
di = Button(ventana, image=white, command=cmdi, width=64, height=64)
dc = Button(ventana, image=white, command=cmdc, width=64, height=64)
dd = Button(ventana, image=white, command=cmdd, width=64, height=64)

ai.grid(row=0, column=0)
ac.grid(row=0, column=1)
ad.grid(row=0, column=2)
di.grid(row=2, column=0)
dc.grid(row=2, column=1)
dd.grid(row=2, column=2)
#if pink == 1:
#    if pink == 2:
#        pinkfix = True
#    else:
#        reset()
#if blue == 1:
#    if blue == 2:
#        bluefix = True
#    else:
#        reset()
#if green == 1:
#    if green == 2:
#        greenfix = True
#    else:
#        reset()
loop()
