"""Obtenga información del usuario mediante input ("Ingrese su edad:"). 
Si el usuario tiene 18 años o más, envíe su opinión: tiene edad suficiente para conducir.
Si tiene menos de 18 años, envíe su opinión para esperar la cantidad de años que faltan. Producción:"""

edad=int(input("ingresa tu edad: "))

if edad >=18:
    print("tiene edad suficiente edad para conducir")
else:
    falta=18-edad
    print("te faltan",falta,"años para poder conducir")
    
    
"""Obtenga dos números del usuario mediante el mensaje de entrada. Si a es mayor que b,
devuelve a es mayor que b, si a es menor que b,
devuelve a es menor que b; de lo contrario, a es igual a b. Producción:"""

a=3
b=5

if a >b:
    print("a es mayor que b")
elif a<b:
    print("a es menor que b")
else:
    print("a es igual que  b")
    
    
"""Escriba un código que califique a los estudiantes según sus puntuaciones:

80-100, A
70-79, B
60-69, C
50-59, D
0-49, F
"""

estudiantes=int(input("ingrese tu calificacion: "))

if estudiantes >=80:
    print("A")
elif estudiantes >=70:
    print("B")
elif estudiantes >=60:
    print("C")
elif estudiantes >=50:
    print("D")
else:
    print("F")



