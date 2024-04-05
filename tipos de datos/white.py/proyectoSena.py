"""El Centro de Industria y Construcción del Sena regional Tolima,
quiere implementar un sistema de control de ingreso que permita contar
los estudiantes que ingresan durante los  seis días a la semana como también
el número de estudiantes por formación. Para el ejemplo vamos a tener en cuenta
las siguientes formaciones: ADSO, producción multimedia,  Desarrollo de videojuegos,
Sistemas El algoritmo debe indicar el total de estudiantes clasificados 
por cada programa,por día. Y al finalizar la semana debe generar 
un reporte con la cantidad de estudiantes que ingresaron al centro de formación.
"""

# Sistema de control de ingreso
# ya permine contar los estudiantes que ingresan en los 6 dias
# ya permite contar el numero de esrtudiantes  por formaccion
# ya indica el total de estudiantes clasificados
# ya genera un reporte de los estudiates que ingresaron
# indicar el total de estudiantes clasificados por cada programa,por día. ya lo hace


print("Bienvenido al Sistema de Control de Ingreso de Estudiantes")
print("El Centro de Industria y Construcción del Sena")

estudenContador = 0
dias = 1
Adso = 0
producción = 0
multimedia = 0
DesarrolloVideojuegos = 0
Sistemas = 0
ingresoenDia = 0

while dias <= 6:  #  los dias que recorre
    print("dia:", dias)
    estudianteDia = 0  #---> cada dia que pase el contador se reiniciara para no sumar los del dia anterior
    for _ in iter(int, 1):  #  la cantidad de estudiantes que permitira ingresar es indefinido
   
        estudiantes = input("ingresa tu (Nombre) para terminar dia ingresa -> 'salir': ")
        if estudiantes.lower() == "salir":
            print("haz terminado dia")
            break
        estudenContador += 1            #-->realizar un seguimiento del número total de estudiantes que ingresan
        estudianteDia += 1           #-->calcular cuántos estudiantes ingresaron en cada día de la semana.
        
        # ingres tu formacion
        print("Que (Formación) perteneces")
        print(
            "\n",
            "1.Adso\n",
            "2.producción\n",
            "3.multimedia\n",
            "4.Desarrollo de juegos\n",
            "5.Sistemas",
        )
        opcion = int(input("Digite Numero # de tu formacion: "))
        # formacion del estudiante, contar cuantos estudiantes  hay en cada formacion y en cual
        if opcion == 1:
            print("Adso")
            Adso += 1
        elif opcion == 2:
            print("producción")
            producción += 1
        elif opcion == 3:
            print("multimedia")
            multimedia += 1

        elif opcion == 4:
            print("Desarrollo de juegos")
            DesarrolloVideojuegos += 1
        elif opcion == 5:
            print("Sistemas")
            Sistemas += 1
        else:
            print("formacion invalida")
    
    # Mostrar total de estudiantes clasificados por programa por día
    print(f"Total de estudiantes de ADSO para el día {dias}:Ingresaron {Adso}")
    print(f"Total de estudiantes de producción multimedia para el día {dias}:Ingresaron {producción}")
    print(f"Total de estudiantes de desarrollo de videojuegos para el día {dias}:Ingresaron {DesarrolloVideojuegos}")
    print(f"Total de estudiantes de sistemas para el día {dias}:Ingresaron {Sistemas}")

    dias += 1
    if estudianteDia > 0: #-->si al menos un estudiante ingresó durante el día actual, 
        ingresoenDia += 1 #-->se incrementa en 1 el contador
        
    
# se muestran los resultados al finalizar la semana

print(f"Dias trascurridos son:  {ingresoenDia} dias ")
print("Dias contados",dias - 1,"Numero total de estudiantes por semana:",estudenContador,)
print(f"Total de estudiantes de la formacion Adso {Adso} ")
print(f"Total de estudiantes de la formacion produccion {producción} ")
print(f"Total de estudiantes de la formacion multimedia {multimedia} ")
print(f"Total de estudiantes de la formacion desarrollo juegos {DesarrolloVideojuegos} ")
print(f"Total de estudiantes de la formacion sistemas {Sistemas} ")
