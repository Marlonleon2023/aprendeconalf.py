"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

e = 0
for e in range(1):
    usuario = input("ingresa una plabra: ")

"""Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

# edad
# Todos los años ha cumplido muestre


edad = int(input("ingresa tu edad: "))
for a in range(edad, 0, -1):
    print(a)


"""Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""


numeroEntero = int(input("ingresa un numero entero +: "))
for b in range(1, numeroEntero + 1, 2):
    print(b)


"""Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la 
inversión, cada año que dura la inversión"""

# cantidad a invertir
# interes anual
# numero de años
# prin capital obetenida
inversion = int(input("ingresa la cantidad a invertir: "))
interes = float(input("ingresa el interes anual: ")) / 100
años = int(input("ingresa el numero de años: "))
for i in range(años):
    cantidadTotal = inversion * (1 + interes) ** (1 + i)
    print(
        "el capital obtenido es :", cantidadTotal, "esta invercion duro:", i + 1, "años"
    )
