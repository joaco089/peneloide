#Voy a simular los lansamientos de un dado, 
#Menu: lansar el dado
#mostrar reporte de los lanzamientos
#salir

#reporte
#numero de lansamientos
#sumar el total de lansamientos
#sacar el promedio de los datos lanzados
#contabilizar cuantas veces salio 1,2,3,4,5,6
pasadas = 0
caida_1 = 0
caida_2 = 0
caida_3 = 0
caida_4 = 0
caida_5 = 0
caida_6 = 0
lista_dado = ""
valor_total = 0
promedio_dado = 0
while True:
    print("\nCalificaciones")
    print("1. Lanzar el dado")
    print("2. Mostrar reporte de dado")
    print("3. Salir\n")
    while True:
        try:
            opcion_primera = int(input("Ingrese su opcion\n"))
            if opcion_primera > 3 and opcion_primera < 1:
                print("Error, opcion no valida")
            else:
                break
        except:
            print("Error valor no reconocido")

    match opcion_primera:
        case 1:
            if pasadas <= 5:
                while True:
                    try:
                        valor_dado = int(input("Ingrese el valor del dado\n"))
                        if valor_dado > 6 or valor_dado < 1:
                            print("Error, opcion no valida")
                        else:
                            break
                    except:
                        print("Error valor no reconocido")
                pasadas += 1   
                match valor_dado:
                    case 1:
                        caida_1 += 1
                    case 2:
                        caida_2 += 1
                    case 3:
                        caida_3 += 1
                    case 4:
                        caida_4 += 1
                    case 5:
                        caida_5 += 1
                    case 6:
                        caida_6 += 1 
                valor_total += valor_dado
            else:
                if pasadas == 0:
                    promedio_dado = 0
                else:
                    promedio_dado = valor_total / pasadas
                promedio_dado_r = round(promedio_dado,0)
                print(f"veces que se tiro el dado {pasadas}")
                print(f"suma de los valores del dado {valor_total}")
                print(f"promedio de los dados lanzados {promedio_dado_r}")
                print(f"veces que salio 1:  {caida_1}")
                print(f"veces que salio 2:  {caida_2}")
                print(f"veces que salio 3:  {caida_3}")
                print(f"veces que salio 4:  {caida_4}")
                print(f"veces que salio 5:  {caida_5}")
                print(f"veces que salio 6:  {caida_6}")
                while True:
                    try:
                        print("Deseas reiniciar el programa? S/N")
                        reinicio = input("Ingrese su opcion\n").upper
                        if reinicio != "S" and reinicio != "N":
                            print("Error... opcion incorrecta")
                        else:
                            break
                    except:
                        print("Error")
                if reinicio == "S":
                    pasadas = 0
                    caida_1 = 0
                    caida_2 = 0
                    caida_3 = 0
                    caida_4 = 0
                    caida_5 = 0
                    caida_6 = 0
                    lista_dado = ""
                    valor_total = 0
                    promedio_dado = 0
                else:
                    print("Gracias por usar el programa")
                    break



        
        case 2:
            if pasadas == 0:
                promedio_dado = 0
            else:
                promedio_dado = valor_total / pasadas
            promedio_dado_r = round(promedio_dado,0)
            print(f"veces que se tiro el dado {pasadas}")
            print(f"suma de los valores del dado {valor_total}")
            print(f"promedio de los dados lanzados {promedio_dado_r}")
            print(f"veces que salio 1:  {caida_1}")
            print(f"veces que salio 2:  {caida_2}")
            print(f"veces que salio 3:  {caida_3}")
            print(f"veces que salio 4:  {caida_4}")
            print(f"veces que salio 5:  {caida_5}")
            print(f"veces que salio 6:  {caida_6}")
        case 3:
            print("Gracias por usar el programa")
            break

            