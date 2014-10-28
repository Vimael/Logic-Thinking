from tkinter import *
r1 = 1
r2 = 1
r3 = 1
r4 = 1
r5 = 1
r6 = 1
r7 = 1
def verificar():
        global r1
        global r2
        global r3
        global r4
        global r5
        global r6
        global r7
        import webbrowser
        if v1.get():
                r1 = 20
        if v2.get():
                r2 = 30
        if v4.get():
                r3 = 10
        if v5.get():
                r4 = -40
        if v5.get():
                r5 = -10
        if v6.get():
                r6 = +10
        if v7.get():
                r7 = -10
        res = r1+r2+r3+r4+r5+r6+r7
        if res >= 50:
                webbrowser.open("")
        if res >= 20 and res < 50:
                webbrowser.open("")
        if res >= 0 and res < 20:
                webbrowser.open("")
        if res < 0 and res >= -20:
                webbrowser.open("")
        if res < -20 and res >= -40:
                webbrowser.open("")
        if res < -40 and res >= -60:
                webbrowser.open("")
        print(res)
  

ventana = Tk()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()

bg = PhotoImage(file="play.png")
ci1 = PhotoImage(file="descojonandose.png")
ci2 = PhotoImage(file="enamorado.png")
ci3 = PhotoImage(file="feliz.png")
ci4 = PhotoImage(file="llorando.png")
ci5 = PhotoImage(file="muriendose.png")
ci6 = PhotoImage(file="sorprendido.png")
ci7 = PhotoImage(file="triste.png")

ch1 = Checkbutton(ventana, image=ci1, text="Me siento eufórico", var=v1)
ch2 = Checkbutton(ventana, image=ci2, text="Me siento triste", var=v2)
ch3 = Checkbutton(ventana, image=ci3, text="Me siento cansado", var=v3)
ch4 = Checkbutton(ventana, image=ci4, text="Me siento eufórico", var=v4)
ch5 = Checkbutton(ventana, image=ci5, text="Me siento triste", var=v5)
ch6 = Checkbutton(ventana, image=ci6, text="Me siento cansado", var=v6)
ch7 = Checkbutton(ventana, image=ci7, text="Me siento cansado", var=v7)
cm = Button(ventana, image=bg, text="Verificar", command=verificar, width=32, height=32)

ch1.grid(row=0, column=0)
ch2.grid(row=1, column=0)
ch3.grid(row=2, column=0)
ch4.grid(row=3, column=0)
ch5.grid(row=4, column=0)
ch6.grid(row=5, column=0)
ch7.grid(row=6, column=0)
cm.grid(row=3, column=1)

ventana.mainloop()
