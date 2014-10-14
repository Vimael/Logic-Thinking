def validarcontraseña():
    contraseña = input("Introduzca una contraseña: ")
    if chr(32) in contraseña:
        print("La contraseña elegida no es segura.\nDebe tener un mínimo de 8 caracteres.\nDebe incluir al menos una mayúscula, minúscula, número y carácter alfanumérico. ")
        contraseña = input("Introduzca una nueva contraseña: ")

    while len(contraseña)<8 or contraseña.isalnum()==True or contraseña.islower()==True or contraseña.isupper()==True or contraseña.isdigit()==True:
        print("La contraseña elegida no es segura.\nDebe tener un mínimo de 8 caracteres.\nDebe incluir al menos una mayúscula, minúscula, número y carácter alfanumérico. ")
        contraseña = input("Introduzca una nueva contraseña: ")
    print("La contraseña es segura")
    return True
