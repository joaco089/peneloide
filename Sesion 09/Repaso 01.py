#Deseo ingresar N estudiantes, de los cuales requiero ingresar 3 calificaciones y un porcentaje de asistencias.
#menu:
#1. INGRESAR LAS CALIFICACIONES Y ASISTENCIA
# 2. MOSTRAR LAS ESTADISTICAS
#Mostrar, Cuantos estudiantes sacando su promedio de notas han aprovado 11-20 desaprovado 8- 10.99, reprovado 0-7.99
#Si tiene 11 para arriba si su asistencia es del 60 %
# El porcentaje de estudiantes aprovados, desaprovados, reprovados 
# Promedio de asistencia de todos los estudiantes
# 3. SALIR
estudiantes_ingresados = 0
suma_asistencia = 0
suma_notas = 0
aprovado = 0
desaprovado = 0
reprovado = 0
desaprovado_asistencia = 0
lista_estudiantes = ""
while True:
    print("\nCalificaciones")
    print("1. Ingresar calificaciones y asistencias")
    print("2. Mostrar estadisticas")
    print("3. Mostrar lista de estudiantes")
    print("4. Salir\n")
    while True:
        try:
            opcion_primera = int(input("Ingrese su opcion\n"))
            if opcion_primera > 4 and opcion_primera < 1:
                print("Error, opcion no valida")
            else:
                break
        except:
            print("Error valor no reconocido")

    match opcion_primera:
            case 1:
                try:
                        nombre = input("Ingrese su Nombre:\n")
                except:
                        print("Error, Nombre no valida")

                while True:
                    try:
                        nota_ingresada_primera = int(input("Ingrese su PRIMERA nota:\n"))
                        if nota_ingresada_primera > 20 or nota_ingresada_primera < 0:
                            print("Error, opcion no valida")
                        else:
                            break
                    except:
                        print("Error, Nota no valida")
                while True:
                    try:
                        nota_ingresada_segunda = int(input("Ingrese su SEGUNDA nota:\n"))
                        if nota_ingresada_segunda > 20 or nota_ingresada_segunda < 0:
                            print("Error, opcion no valida")
                        else:
                            break
                    except:
                        print("Error, Nota no valida")
                while True:   
                    try:
                        nota_ingresada_tercera = int(input("Ingrese su TERCERA nota:\n"))
                        if nota_ingresada_tercera > 20 or nota_ingresada_tercera < 0:
                            print("Error, opcion no valida")
                        else:
                            break
                    except:
                        print("Error, Nota no valida")
                while True:
                    try:
                        porcentaje_asistencia = int(input("Ingrese su Porcentaje de ASISTENCIA:\n"))
                        if porcentaje_asistencia > 100 or porcentaje_asistencia < 0:
                            print("Error, opcion no valida")
                        else:
                            break
                    except:
                        print("Error, Nota no valida")
                    
                suma_notas_estudiante = nota_ingresada_primera + nota_ingresada_segunda + nota_ingresada_tercera
                nota_estudiante = suma_notas_estudiante / 3

                estudiantes_ingresados += 1
                suma_notas += nota_estudiante
                suma_asistencia += porcentaje_asistencia

                if nota_estudiante > 11 and porcentaje_asistencia > 60:
                    aprovado += 1
                    estado = "APROVADO"

                elif nota_estudiante > 11:
                    desaprovado_asistencia += 1
                    estado = "DESAPROVADO POR ASISTENCIA"

                elif nota_estudiante < 11 and nota_estudiante >= 8:
                    desaprovado += 1
                    estado = "DESAPROVADO"

                else:
                    reprovado += 1
                    estado = "REPROVADO"

                lista_estudiantes += f"{nombre}\nPromedio: {nota_estudiante} Asistencia: {porcentaje_asistencia}% Estado:{estado}\n"
                    
            case 2:
                porcentaje_aprovado = (aprovado / estudiantes_ingresados) * 100
                porcentaje_desaprovado = (desaprovado / estudiantes_ingresados) * 100
                porcentaje_reprovado = (reprovado / estudiantes_ingresados) * 100
                porcentaje_desaprovado_asistencia = (desaprovado_asistencia / estudiantes_ingresados) * 100
                porcentaje_asistencia = suma_asistencia / estudiantes_ingresados
                
                print(f"El porcentaje de aprovados \n{porcentaje_aprovado}%\nEl porcentaje de desaprovados\n{porcentaje_desaprovado}%\nEl porcentaje de desaprovados por asistencia\n{porcentaje_desaprovado_asistencia}%\nEl porcentaje de reprovados\n{porcentaje_reprovado}%")
                print(f"El porcentaje de asistencia de todos los estudiantes es {porcentaje_asistencia}%")

            case 3:
                print("\n\nLISTA DE ESTUDIANTES")
                print(lista_estudiantes)
                
            case 4:
                print("\n\nGracias por usar el programa\n\n")
                break





            


            
            


 
        
        