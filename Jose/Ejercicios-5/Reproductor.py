from tkinter import *
import os
import random
i_cancion = 0
ventana = Tk()
tabla = ["The_Blasters_Dark_Night.mp3",
         "Stealers_Wheel_Stuck_In_The_Middle_With_You.mp3",
         "Simon_&_Garfunkel_Mrs_Robinson.mp3",
         "Rolling_Stones_Don\'t_Stop.mp3",
         "Nick_Drake_Pink_Moon.mp3",
         "Neil_Young_After_the_Gold_Rush_07_Don\'t_Let_t_Bring_You_Down.mp3",
         "Kula_shaker-fool_that_i_am.mp3",
         "Jet_Get_What_You_Need.mp3",
         "Chuck_Berry_You_Never_Can_Tell.mp3",
         "Chris_Isaak_Baby_did_a_bad_bad_thing.mp3"]

#tabla = ["The_Blasters_Dark_Night.mp3",
#         "Stealers_Wheel_Stuck_In_The_Middle_With_You.mp3",
#         "Simon_&_Garfunkel_Mrs_Robinson.mp3",
#         "Rolling_Stones_Don\'t_Stop.mp3",
#         "Nick_Drake_Pink_Moon.mp3",
#         "Neil_Young_After_the_Gold_Rush_07_Don\'t_Let_t_Bring_You_Down.mp3",
#         "Kula_shaker-fool_that_i_am.mp3",
#         "Jet_Get_What_You_Need.mp3",
#         "Chuck_Berry_You_Never_Can_Tell.mp3",
#         "Chris_Isaak_Baby_did_a_bad_bad_thing.mp3"]

<<<<<<< HEAD
def play():
    os.startfile(tabla[i_cancion])
=======
def uno():
    open('Chris_Isaak_Baby_did_a_bad_bad_thing.mp3')
def dos():
    open('Chuck_Berry_You_Never_Can_Tell.mp3')
def tres():
    open('Jet_Get_What_You_Need.mp3')
def cuatro():
    open('Kula_shaker-fool_that_i_am.mp3')
def cinco():
    open('Neil_Young_After_the_Gold_Rush_07_Don\'t_Let_t_Bring_You_Down.mp3')
def seis():
    open('Nick_Drake_Pink_Moon.mp3')
def siete():
    open('Rolling_Stones_Don\'t_Stop.mp3')
def ocho():
    open('Simon_&_Garfunkel_Mrs_Robinson.mp3')
def nueve():
    open('Stealers_Wheel_Stuck_In_The_Middle_With_You.mp3')
def diez():
    open("The_Blasters_Dark_Night.mp3")

def cambio():
    play = Button(ventana, image=favi, command=uno, width=64, height=64)
    play.grid(row=2, column=2)
>>>>>>> origin/master
    
def atras():
    global i_cancion
    if i_cancion == 0:
        i_cancion = len(tabla)-1
    else:
        i_cancion -= 1
    play()
    
def aleatorio():
    global i_cancion
    i_cancion = random.randint(0, 9)
    play()
    
def siguiente():
    global i_cancion
    if i_cancion >= len(tabla):
        i_cancion = 0
    else:
        i_cancion += 1
    play()

w = Label(ventana, text="BIENVENIDO AL REPRODUCTOR DE JOSE")
w.grid(row=0, column=0, columnspan=4)

<<<<<<< HEAD
bg1=PhotoImage(file="ant.png")
bt1 = Button(ventana, image=bg1, command=atras, width=64, height=64)
bt1.grid(row=1, column=0)
=======
anti = PhotoImage(file="ant.png")
sigi = PhotoImage(file="sig.png")
buci = PhotoImage(file="buc.png")
ali = PhotoImage(file="al.png")
favi = PhotoImage(file="fav.png")
playi = PhotoImage(file="play.png")

ant = Button(ventana, image=anti, text="command=antc", width=64, height=64)
sig = Button(ventana, image=sigi, text="command=sigc", width=64, height=64)
buc = Button(ventana, image=buci, text="command=bucc", width=64, height=64)
al = Button(ventana, image=ali, text="command=alc", width=64, height=64)
fav = Button(ventana, image=favi, text="command=favc", width=64, height=64)
play = Button(ventana, image=playi, command=cambio, width=64, height=64)

ant.grid(row=0, column=0)
buc.grid(row=0, column=1)
al.grid(row=0, column=2)
sig.grid(row=0, column=3)
fav.grid(row=2, column=1)
play.grid(row=2, column=2)
>>>>>>> origin/master

bg2=PhotoImage(file="play.png")
bt2 = Button(ventana, image=bg2, command=play, width=64, height=64)
bt2.grid(row=1, column=1)

bg3=PhotoImage(file="al.png")
bt3 = Button(ventana, image=bg3, command=aleatorio, width=64, height=64)
bt3.grid(row=1, column=2)

bg4=PhotoImage(file="sig.png")
bt4 = Button(ventana, image=bg4, command=siguiente, width=64, height=64)
bt4.grid(row=1, column=3)

ventana.mainloop()
