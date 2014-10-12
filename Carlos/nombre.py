import time
nombre = input("Introduzca su nombre: ")
time.sleep(1)
largo = len(nombre)
contador = 0
for contador in range(1, largo):
    print(nombre[:contador])
for contador in range(largo, 0, -1):
    print(nombre[:contador])
