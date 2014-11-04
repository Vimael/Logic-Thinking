from tkinter import *
import os

ventana = Tk()

def Atras():
    return
def Bucle():
    return
def Aleatorio():
    return
def Adelante():
    return



###############################################################################

bg0 = PhotoImage(file="atras.png")
bg1 = PhotoImage(file="bucle.png")
bg2 = PhotoImage(file="aleatorio.png")
bg3 = PhotoImage(file="adelante.png")

cm = Button(ventana, image=bg0, text="Atrás", command = Atras, width=32, height=32)
cm.grid(row=1, column=0)

cm = Button(ventana, image=bg1, text="Bucle", width=32, height=32)
cm.grid(row=1, column=1)

cm = Button(ventana, image=bg2, text="Aleatorio", width=32, height=32)
cm.grid(row=1, column=2)

cm = Button(ventana, image=bg3, text="Adelante", width=32, height=32)
cm.grid(row=1, column=3)

################################################################################

bg4 = PhotoImage(file="fav.png")

cm = Button(ventana, image=bg4, text="fav", width=32, height=32)
cm.grid(row=2, column=2)






################################################################################

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()

check = Checkbutton(ventana, text="Alegre     ", var=variable1)
check.grid(row=3, column=0)
check = Checkbutton(ventana, text="Triste     ", var=variable2)
check.grid(row=3, column=1)
check = Checkbutton(ventana, text="Meditación ", var=variable3)
check.grid(row=3, column=2)
check = Checkbutton(ventana, text="No pensar  ", var=variable4)
check.grid(row=3, column=3)






################################################################################
ventana.mainloop()
