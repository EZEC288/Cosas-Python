import random


nombre = input("Escriba su Nombre: ")


print(f"\nHola {nombre}! Bienvenido al juego de adivinanza.")
print("Tenés adivinar un número entre 1 y 100.")
print("Tenés 8 intentos para lograrlo.\n")


numero_adivinar = random.randint(1, 100)


intentos_restantes = 8
adivinado = False


while intentos_restantes > 0:
    print(f"Te quedan: {intentos_restantes} " "Vidas")
    numero_ingresado = input("Ingresa un número: ")

    
    if not numero_ingresado.isdigit():
        print("Errór: Ingresá un número entero.")
        continue

    numero_ingresado = int(numero_ingresado)

    
    if numero_ingresado == numero_adivinar:
        intento_actual = 8 - intentos_restantes + 1
        print(f"\n¡Felicitaciones {nombre}! Has adivinado el número en el intento {intento_actual}.")
        adivinado = True
        break
    elif numero_ingresado < numero_adivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")

    intentos_restantes -= 1


if not adivinado:
    print(f"\nLo siento {nombre}, No te quedan mas Vidas.")
    print(f"El número era: {numero_adivinar}")
