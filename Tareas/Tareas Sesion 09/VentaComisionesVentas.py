pasada = 0
precio_descuento = 0
precio_neto = 0
precio_bruto = 0
comision = 0
productos_mayor_300 = 0
suma_descuentos = 0
cantidad_total_productos = 0
try:
    nombre = input("Ingrese su nombre:\t")
except:
    print("Ingrese un nombre valido")
while True:
    print("=========")
    print("1. Registrar venta")
    print("2. Mostrar estadisticas")
    print("3. Salir")
    while True:
        try:
            opcion_primera = int(input("Ingrese su opcion:\t"))
            if opcion_primera > 3 or opcion_primera < 1:
                print(f"Error la opcion {opcion_primera} no es valida")
            else:
                break
        except:
            print(f"No re reconocio la respuesta")
    match opcion_primera:
        case 1:
            while True:
                try:
                    precio_producto = float(input("Ingrese el precio del producto:\t"))
                    if precio_producto < 0:
                        print(f"Error el precio {precio_producto} no es valida")
                    else:
                        break
                except:
                    print(f"No re reconocio la respuesta")
            while True:        
                try:
                    cantidad_producto = int(input("Ingrese la cantidad_producto:\t"))
                    if cantidad_producto < 0:
                        print(f"Error el precio {precio_producto} no es valida")
                    else:
                        break
                except:
                    print(f"No re reconocio la respuesta")
                

            precio_bruto += (precio_producto * cantidad_producto)
            if precio_bruto > 200:
                dcto = 0.15
            else:
                dcto = 0
            precio_descuento += round((precio_bruto * dcto),1)
            suma_descuentos += round(precio_descuento,1)
            precio_neto += (precio_bruto - precio_descuento)
            if precio_neto > 300:
                productos_mayor_300 +=  (1 * cantidad_producto)
            comision += (precio_neto * 0.08)
            pasada += 1
            cantidad_total_productos += cantidad_producto


        case 2:
            promedio_descuento_venta = round(suma_descuentos / cantidad_total_productos,1)
            porcentaje_meta = round((precio_bruto * 100) / 5000,1)
            comision_r = round(comision,1)
            print(f"\n==============")
            print(f"Total recaudado sin descuento: {precio_bruto}")
            print(f"Total recaudado con descuento aplicado: {precio_neto}")
            print(f"Comision recaudada para el vendedor: {comision_r}")
            print(f"Porcentaje de la meta alcanzada (5000): {porcentaje_meta}%")
            print(f"Promedio de descuento aplicado por venta: {promedio_descuento_venta}")
            print(f"Cantidad de ventas que superaron los 300$: {productos_mayor_300}")
            print(f"===============\n")

        case 3:
            print(f"Gracias por usar el programa {nombre}")
            break


        