"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""

# asignaturas=["Matematicas","Fisica","Quimica","Hitoria","Lengua"]

# print("asignaturas del curso")
# print(asignaturas)


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
donde <asignatura> es cada una de las asignaturas de la lista."""

# asignaturas = ["Matematicas", "Fisica", "Quimica", "Hitoria", "Lengua"]
# for asignatura in asignaturas:
#  print("yo estudio: " + asignatura)

"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> 
donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.
"""
asignaturas = ["Matematicas", "Fisica", "Quimica", "Hitoria", "Lengua"]
for i in asignaturas:
    nota = int(input("ingresa nota de la asignatura {}: ".format(i)))
    print("En {} has sacado {} ".format(i, nota))

# preguntarle al usuario la nota en cada asignatura
#split() para obtener una lista de cadenas.

"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

# PRACTICAR FALTA MAS PARA APRENDER 

# Solicitar al usuario los números ganadores
numerosLoteria = input("Ingresa los números ganadores de la lotería, separados por espacios: ")

# Dividir los números ingresados por el usuario y convertirlos a enteros
numerosEspacio = numerosLoteria.split()  # Divide la cadena en una lista de números
numerosProcesados = []  # Crear una lista vacía para almacenar los números enteros
for numeroCadena in numerosEspacio:
    numeroEntero = int(numeroCadena)  # Convertir cada número de cadena a entero
    numerosProcesados.append(numeroEntero)  # Agregar el número entero a la lista

# Ordenar los números de menor a mayor
numerosOrdenados = sorted(numerosProcesados)

# Mostrar los números ordenados
print("Números ganadores de la lotería (ordenados de menor a mayor):", numerosOrdenados)
