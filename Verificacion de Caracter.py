def verificar_caracter(caracter):
    if caracter.issuper():
        print("Tu Contenido tiene alguna Mayúscula")
    elif caracter.islower():
        print("Tu Contenido tiene alguna Minúscula")
     
    elif caracter.isdigit():
        print("Tu Contenido tiene algún Número")

    else:
        print("No Contiene caraceteres Especiales")

        caracter_ingresado = input("Ingrese un Caracter:")
        verificar_caracter(caracter_ingresado)