def validarcontraseña():
    contraseña = input("Introduzca una contraseña: ")
    if chr(32) in contraseña:
        print("No puede haber espacios en la contraseña. ")
        contraseña = input("Introduzca una nueva contraseña: ")    
    if len(contraseña)<8:
        print("La contraseña debe contener un mínimo de 8 caracteres. ")
        contraseña = input("Introduzca una nueva contraseña: ")
    if contraseña.isalnum()==True:
        print("La contraseña debe contener al menos un caracter no alfanumérico. ")
        contraseña = input("Introduzca una nueva contraseña: ")
    if contraseña.islower()==True:
        print("La contraseña debe contener al menos una mayúscula. ")
        contraseña = input("Introduzca una nueva contraseña: ")
    if contraseña.isupper()==True:
        print("La contraseña debe contener al menos una minúscula. ")
        contraseña = input("Introduzca una nueva contraseña: ")
    if contraseña.isdigit()==True:
        print("La contraseña debe contener letras. ")
        contraseña = input("Introduzca una nueva contraseña: ")
    print("La contraseña es segura")
    return True
validarcontraseña()
