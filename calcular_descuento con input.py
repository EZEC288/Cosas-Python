def calcular_descuento(precio,porcentaje_descuento):
    descuento = precio *(porcentaje_descuento/100)
    precio_con_descuento = precio - descuento
    return precio_con_descuento

precio = float(input("Ingrese El Precio: "))
porcentaje_descuento = float(input("Ingrese el Descuento: "))

precio_final = calcular_descuento(precio, porcentaje_descuento) 
print("$",precio_final) 


