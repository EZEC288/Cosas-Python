notas = []

num_notas = int(input("Ingrese la Cantidad de Notas: "))

for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)


if notas:
    divisor = float(input("Ingrese la Cantidad por la Cual desea Dividir su Nota: "))
    promedio = sum(notas) / divisor
    print("Su Promedio es:",promedio)

if promedio == 6:
    print("Aprobó (con un Puntaje Justo) la Materia y/o la Carrera")

elif promedio < 6:
     print("Desaprobó, Necesita Estudiar y Repasar lo Dado")

elif promedio >=7:
    print("Aprobó Exitosamente La Materia y/o Carrera")

elif promedio >=9:
    print("Felicitaciones, Aprobó La Materia y/o Carrera, se nota que Estudió Mucho")

else:
    print("No se Ingresaron Notas, Comprueba Otra Vez")             