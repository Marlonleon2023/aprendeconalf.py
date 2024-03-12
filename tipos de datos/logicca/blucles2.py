"""Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
"""

# Numero Entero
# motrar triangulo rectangulo


numeroEntero = int(input("ingresa un numero entero: "))
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print("")

"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""
tablaMultiplicar = int(input("ingresa el numero de la tabla multi: "))
rang = 1
for w in range(rang, 11):
    rang = tablaMultiplicar
    print(rang, "x", w, "=", tablaMultiplicar * w)

"""Escribir un programa que pida al usuario un número entero y muestre 
por pantalla un triángulo rectángulo como el de más abajo."""

numeroInter = int(input("ingresa numero para trian: "))
for q in range(1, numeroInter + 1, 2):
    for s in range(q, 0, -2):
        print(s, end="")
    print("")


# --------WHILE------------------
"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta"""

contraseña = "marlon123"
ingresar = input("ingresa tu contraseña: ")
while contraseña != ingresar:
    print("contraseña incorrecta")
    ingresar = input("vuelve a ingresar contraseña: ")
    print("contraseña correcta")

"""Escribir un programa que pida al usuario un número entero y
muestre por pantalla si es un número primo o no."""

n = int(input("Ingresa un numero entero: "))
x = 2
while n % x != 0:
    x += 1
if x == n:
    print("es numero primo ")
else:
    print("no es primo")
