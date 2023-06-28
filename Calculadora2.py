operacion = int(input("Ingrese la operación a realizar (1-Suma, 2-Resta, 3-Multiplicación, 4-División): ")) 

num1 = float(input("Indique el Primer Número: "))
num2 = float(input("Indique el Segundo Número: "))

if operacion == 1:
    resultado = num1 + num2
    print("El Resultado de su Suma es: ",resultado)

elif operacion == 2:
    resultado = num1 - num2
    print("El Resultado de su Resta es",resultado)

elif operacion == 3:
    resultado = num1 * num2
    print("El Resultado de su Multiplicación es",resultado)

elif operacion == 4:
   if num1 != 0 and num2 != 0:
    resultado = num1 / num2
    print("El Resultado de su División es",resultado)
   else:
    print("Por Favor,Intente Denuevo (Recuerda que no se puede dividir con el Número 0)")

else:
    print("Operación No Válida,Por Favor elija unas de las Opciones Proporcionadas por el Sistena(Suma,Resta,Division o Multiplicacion) y que el Número no Contenga Comas,Gracias")

