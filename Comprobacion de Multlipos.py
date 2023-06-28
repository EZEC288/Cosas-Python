numero = int(input("Ingrese un Número "))

if numero % 2 == 0  and  numero % 3 == 0:
    print("Su Número es Multiplo de 2 y de 3")
elif numero % 2 == 0:
    print("Su Número es Multiplo de 2 pero no de 3")
elif numero % 3 == 0:
    print("Su Número es Multipo de 3 y no de 2")
else:
    print("No es Multiplo de 2 ni de 3")