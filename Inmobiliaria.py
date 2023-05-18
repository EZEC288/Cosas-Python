
from datetime import datetime

inmuebles = [
    {"año": 2010, "metros": 150, "habitaciones": 4, "garaje": True, "zona": "C", "estado": "Disponible"},
    {"año": 2016, "metros": 80, "habitaciones": 2, "garaje": False, "zona": "B", "estado": "Reservado"},
    {"año": 2000, "metros": 180, "habitaciones": 4, "garaje": True, "zona": "A", "estado": "Disponible"},
    {"año": 2015, "metros": 95, "habitaciones": 3, "garaje": True, "zona": "B", "estado": "Vendido"},
    {"año": 2008, "metros": 60, "habitaciones": 2, "garaje": False, "zona": "C", "estado": "Disponible"}
]

def agregar_inmueble():
    año = int(input("Año del inmueble: "))
    metros = int(input("Metros cuadrados del inmueble: "))
    habitaciones = int(input("Número de habitaciones: "))
    garaje = input("¿Tiene garaje? (S/N): ").upper() == "S"
    zona = input("Zona del inmueble (A, B, C): ").upper()
    estado = input("Estado del inmueble (Disponible, Reservado, Vendido): ").capitalize()

    if zona not in ["A", "B", "C"]:
        print("Error: La Zona del Inmueble debe ser en: A, B o C.")
        return
    if estado not in ["Disponible", "Reservado", "Vendido"]:
        print("Error: El estado del Inmueble debe estar en: Disponible, Reservado, Vendido.")
        return
    if año < 2000:
        print("Error: El año del Inmueble debe ser como mínimo el año 2000.")
        return
    if metros < 60:
        print("Error: Los Metros deben ser como mínimo 60 Metros Cuadrados.")
        return
    if habitaciones < 2:
        print("Error: Las Habitaciones deben tener un mínimo de 2 lugares.")

    antiguedad = datetime.now().year - año
    if zona == "A":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == "B":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2

    nuevo_inmueble = {"año": año, "metros": metros, "habitaciones": habitaciones, "garaje": garaje, "zona": zona, "estado": estado, "precio": precio}
    inmuebles.append(nuevo_inmueble)
    print("Inmueble agregado correctamente.")

def editar_inmueble():
    indice = int(input("Ingrese el índice del inmueble a editar: "))
    if indice < 0 or indice >= len(inmuebles):
        print("Error: El índice del inmueble no es válido.")
        return

    inmueble = inmuebles[indice]

    print("Datos actuales del inmueble:")
    print(inmueble)

    print("Ingrese los nuevos datos del inmueble:")
    año = int(input("Año del inmueble: "))
    metros = int(input("Metros cuadrados del inmueble: "))
    habitaciones = int(input("Número de habitaciones: "))
    garaje = input("¿Tiene garaje? (S/N): ").upper() == "S"
    zona = input("Zona del inmueble (A, B, C): ").upper()
    estado = input("Estado del inmueble (Disponible, Reservado, Vendido): ").capitalize()

    if zona not in ["A", "B", "C"]:
        print("Error: La Zona del Inmueble debe ser en: A, B o C.")
        return
    if estado not in ["Disponible", "Reservado", "Vendido"]:
        print("Error: El estado del Inmueble debe estar en: Disponible, Reservado, Vendido.")
        return
    if año < 2000:
        print("Error: El año del Inmueble debe ser como mínimo el año 2000.")
        return
    if metros < 60:
        print("Error: Los Metros deben ser como mínimo 60 Metros Cuadrados.")
        return
    if habitaciones < 2:
        print("Error: Las Habitaciones deben tener un mínimo de 2 lugares.")

    antiguedad = datetime.now().year - año
    if zona == "A":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == "B":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2

    inmueble["año"] = año
    inmueble["metros"] = metros
    inmueble["habitaciones"] = habitaciones
    inmueble["garaje"] = garaje
    inmueble["zona"] = zona
    inmueble["estado"] = estado
    inmueble["precio"] = precio

    print("Inmueble editado correctamente.")

def eliminar_inmueble():
    indice = int(input("Ingrese el índice del inmueble a eliminar: "))
    if indice < 0 or indice >= len(inmuebles):
        print("Error: El índice del inmueble no es válido.")
        return

    inmuebles.pop(indice)
    print("Inmueble eliminado correctamente.")

def cambiar_estado():
    indice = int(input("Ingrese el índice del inmueble a cambiar de estado: "))
    if indice < 0 or indice >= len(inmuebles):
        print("Error: El índice del inmueble no es válido.")
        return

    inmueble = inmuebles[indice]

    print("Estado actual del inmueble:", inmueble["estado"])

    estado = input("Ingrese el nuevo estado del inmueble (Disponible, Reservado, Vendido): ").capitalize()
    if estado not in ["Disponible", "Reservado", "Vendido"]:
        print("Error: El estado del Inmueble debe estar en: Disponible, Reservado, Vendido.")
        return

    inmueble["estado"] = estado
    print("Estado del inmueble cambiado correctamente.")

def buscar_inmuebles_por_presupuesto(presupuesto):
    inmuebles_disponibles = []
    for inmueble in inmuebles:
        if inmueble["estado"] in ["Disponible", "Reservado"] and inmueble["precio"] <= presupuesto:
            inmuebles_disponibles.append(inmueble)
    return inmuebles_disponibles

while True:
    print("--- Menú ---")
    print("1. Agregar inmueble")
    print("2. Editar inmueble")
    print("3. Eliminar inmueble")
    print("4. Cambiar estado del inmueble")
    print("5. Buscar inmuebles por presupuesto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_inmueble()
    elif opcion == "2":
        editar_inmueble()
    elif opcion == "3":
        eliminar_inmueble()
    elif opcion == "4":
        cambiar_estado()
    elif opcion == "5":
        presupuesto = float(input("Ingrese el presupuesto máximo: "))
        inmuebles_en_presupuesto = buscar_inmuebles_por_presupuesto(presupuesto)
        print("Inmuebles encontrados:")
        for inmueble in inmuebles_en_presupuesto:
            print(inmueble)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

