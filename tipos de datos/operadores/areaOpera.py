"""Obtenga el radio de un círculo usando el mensaje.
Calcula el área (área = pi xrxr) y la circunferencia (c = 2 x pi xr) donde pi = 3,14."""
radio=int(input("ingresa la medida del radio: "))
pi=3.1416
radio=pi*radio**2
c=2*pi
print("el area es: ",radio,"la cicunferencia es :",c)

"""Los números pares son 
divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no usando Python?"""
pares=int(input("ingresa un numero entero: "))

if pares%2==0:
    print("es par")
else:
    print("es impar")
    
"""Compruebe si la división del piso de 7 por 3 es igual al valor int convertido de 2,7."""
print("comprueba tu divicion")
divicion =7*3//2.7
print (int(divicion))

"""Escriba un script que solicite al usuario que ingrese las horas y
la tarifa por hora. ¿Calcular el salario de la persona?"""

horas=int(input("ingresa las hora trabajadas: "))
tarifa=int(input("ingresa la tarifa por hora: "))

salario=horas*tarifa
print("salario de la persona es :",salario)

"""Escriba un script que solicite al usuario que ingrese el número de años. Calcula el número de segundos
que puede vivir una persona. Supongamos que una persona puede vivir cien años"""

años=int(input("ingresa el numero de años que desees: "))
segundos=86400

vivir=años*segundos
print("los segundos que puedes vivir son:",vivir)