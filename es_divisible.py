def es_divisible(num1,num2):
    if num1 % num2 == 0:
        return "Es Divisible"
    else:
        return "No es Divisible"
    
resultado = es_divisible(10,2)
print(resultado)

resultado = es_divisible(2,8)
print(resultado)