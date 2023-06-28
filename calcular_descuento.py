def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento/100)
    precio_con_descuento = precio - descuento
    return precio_con_descuento

precio_final = calcular_descuento(150,20)
print("$",precio_final)


precio_final = calcular_descuento(50,10)
print("$",precio_final)
