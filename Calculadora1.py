num1 = input("Ingrese Un Numero: ")
num2 = input("Ingrese Otro Numero: ")

num1_float = float(num1)
num2_float = float(num2)

suma = num1_float + num2_float
print("Este es el Resultado de la Suma:",suma)

resta = num1_float - num2_float
print("Este es el Resultado de la Resta:",resta)

multiplicacion = num1_float * num2_float
print("Este es el Resultado de la Multiplicacion:",multiplicacion)

division = num1_float / num2_float
print("Este es el Resultado de la División:",division)

try:
    num1_float = float(num1)
    num2_float = float(num2)

except ValueError:
    print("Ingresa solo Numeros Válidos,Recuerda que los Números Décimales van con 'Puntos' y no con 'Comas'")