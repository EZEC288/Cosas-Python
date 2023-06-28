notas = []

while True:
    nota = input("Ingrese Su Nota (O si desea salir Presione 'q'): ")
    if nota == 'q':
      break
    notas.append(float(nota))

    if nota:
       promedio = sum(notas) / 3
       print("Este es el Promedio de notas",promedio)
    else:
       print("No se Ingresaron Notas,Por Favor Intente de Nuevo")
