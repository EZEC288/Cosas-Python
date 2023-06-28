def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    cadena_invertida = cadena[::-1]

    if cadena == cadena_invertida:
        return "Es Palíndromo"
    else:
        return "No es Palíndromo"

resultado = es_palindromo("Yo Escribo el Código")
print(resultado)

resultado = es_palindromo("Hola Mundo")
print(resultado)



