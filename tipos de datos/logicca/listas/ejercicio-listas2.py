"""Escribir un programa que almacene en una 
lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas"""

# numero=[1,2,3,4,5,6,7,8,9,10]
# numero.reverse()
# for numer in numero:
#   print(numer, end=" ,")

"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en 
cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir"""

# almacenar asgnatura del curso
# pregunte al usuario que nota a sacado en cada  asignatura
#  eliminar lista asignatura aprobadas
# mostrar asignaturas perdidas

"""asignaturas=["Matemáticas", "Física", "Química", "Historia","Lengua"]
asignaturasReprobadas=[]
for i in asignaturas:
    nota =int(input("Que nota a sacado en  asignatura {}: ".format(i)))
    print("En {} Has sacado {}".format(i, nota))
    if nota > 6:
        print("haz aprobado")
    else:
        print("haz reprobado")
        asignaturasReprobadas.append(i)
print("Asignaturas a repetir:", asignaturasReprobadas)"""

"""Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante."""

# almacenar el abecedario
# Elimine letras que ocupen posiciones 3
# Lista resultante

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",]

for i in range(len(abecedario) - 1, -1, -1):
    if (i + 1) % 3 == 0:
        del abecedario[i]
print(abecedario)

"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

ingresa = input("ingresa una palabra polindroma: ")

palabraPolidroma = ingresa[::-1]  # [::-1]<- invierte  las palabras  al reves
print("Palabra Invertida :", palabraPolidroma)

if palabraPolidroma == ingresa:  # comáramos si palabra polindroma  es igual a ingresar
    print("Es una palabra polidroma ")
else:
    print("No es Palabra Plindroma")

"""Escribir un programa que pida al usuario una palabra y muestre por pantalla 
el número de veces que contiene cada vocal."""
vocales=["a","e","i","o","u"]
palabraVocal=input("ingresa una palabra: ")
contadorVocal=""
for palabra in palabraVocal:
    if palabra in vocales:
        contadorVocal+=palabra
print(contadorVocal)
  
  
  


