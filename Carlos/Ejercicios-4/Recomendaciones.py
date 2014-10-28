import random
import webbrowser
from tkinter import *

urlgay = "https://www.youtube.com/watch?v=XVE8DSeoX9U"



def verificar():
    global variable1
    global variable2 
    global variable3
    global variable4 
    global variable5
    global variable6 
    global variable7
    global variable8 
    global variable9

    if variable9.get() == 1:
        print("GAAAAAAY")
        webbrowser.open(urlgay)
        
    
    if variable1.get() == 1:
        variable1 = random.randint(150, 200)
        
    if variable2.get() == 1:
        variable2 = random.randint(100, 175)
        
    if variable3.get() == 1:
        variable3 = random.randint(50, 125)
        
    if variable4.get() == 1:
        variable4 = random.randint(0, 75)
        
    if variable5.get() == 1:
        variable5 = random.randint(-50, 25)

    if variable6.get() == 1:
        variable6 = random.randint(-100, -25)

    if variable7.get() == 1:
        variable7 = random.randint(-150, -75)

    if variable8.get() == 1:
        variable8 = random.randint(-200, -125)

    resultado = variable1+variable2+variable3+variable4+variable5+variable6+variable7+variable8

    
        


ventana = Tk()

bg = PhotoImage(file="play.png")

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()

check1 = Checkbutton(ventana, text="Me gusta el heavy metal   ", var=variable1)
check2 = Checkbutton(ventana, text="Me gusta el punk          ", var=variable2)
check3 = Checkbutton(ventana, text="Me gusta el rock urbano   ", var=variable3)
check4 = Checkbutton(ventana, text="Me gusta el rock clásico  ", var=variable4)
check5 = Checkbutton(ventana, text="Me me gusta el ska        ", var=variable5)
check6 = Checkbutton(ventana, text="Me gusta el blues         ", var=variable6)
check7 = Checkbutton(ventana, text="Me gusta el jazz          ", var=variable7)
check8 = Checkbutton(ventana, text="Me gusta la música clásica", var=variable8)
check9 = Checkbutton(ventana, text="Me gusta Abraham Mateo    ", var=variable9)

check1.grid(row=0, column=0)
check2.grid(row=1, column=0)
check3.grid(row=2, column=0)
check4.grid(row=3, column=0)
check5.grid(row=4, column=0)
check6.grid(row=5, column=0)
check7.grid(row=6, column=0)
check8.grid(row=7, column=0)
check9.grid(row=8, column=0)

cm = Button(ventana, image=bg, text="Verificar", command=verificar, width=32, height=32)
cm.grid(row=9, column=0)

ventana.mainloop()
