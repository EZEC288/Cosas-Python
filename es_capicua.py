def es_capicua(numero):
    numero_str = str(numero)
    numero_invertido = numero_str[::-1]
    if numero_str == numero_invertido:
       return True
    else:
        return False

if es_capicua(12345):
    print("el numero es capicua")
else:
    print("el numero no es capicua")  