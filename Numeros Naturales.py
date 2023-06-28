numeros = int(input("Ingrese Un Número: "))
suma = 0

for i in range(1, numeros + 1):
    suma += i  
    print("La Suma de los Numeros Naturales hasta", numeros, "es: ", suma)