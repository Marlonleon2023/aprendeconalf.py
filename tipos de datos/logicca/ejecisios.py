"""Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla si es mayor de edad o no."""

tuEdad = int(input("ingresa tu edad : "))

if tuEdad >= 18:
    print("Eres Mayor de edad")
else:
    print("no eres mayor de edad")


"""Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla
si la contraseña introducida por el usuario coincide con la guardada 
en la variable sin tener en cuenta mayúsculas y minúsculas"""

# variable

contraseñaGuardada = "marlon123zxx"

ingresaContraseña = input("ingresa tu contraseña: ")

if ingresaContraseña == contraseñaGuardada:
    print("has ingresado con exito")
else:
    print("contraseña incorrecta ")


"""Escribir un programa que pida al usuario dos números y muestre 
por pantalla su división. Si el divisor es cero el programa debe mostrar un error."""


dividendo = int(input("ingrese dividendo: "))
divisor = int(input("ingrese divisor: "))

if divisor == 0:

    print(TabError)
else:
    print(dividendo / dividendo)

"""Escribir un programa que pida al usuario un número entero y muestre 
por pantalla si es par o impar"""


print("ingresa un numero entero")

entero = int(input("ingresa el primer numero: "))

if entero % 2 == 0:
    print("es par")
else:
    print("es impar")


"""Para tributar un determinado impuesto se debe ser mayor de 16 años y 
tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un 
programa que pregunte al usuario su edad y sus 
ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no"""

# ingresos >= 1000 mesuales

# mayor = 16

mayor = int(input("ingresa tu edad: "))

ingresosMensuales = int(input("ingresos mensuales: "))
if mayor > 16 and ingresosMensuales >= 1000:
    print("tienes que tributar")
else:
    print("no tienes que tributar")


"""Los alumnos de un curso se han dividido en dos 
grupos A y B de acuerdo al sexo y el nombre. El grupo 
A esta formado por las mujeres con un nombre anterior a la M y 
los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y 
muestre por pantalla el grupo que le corresponde."""


# grupo A = mujeres  l hombres  M
# grupo B = resto

nombre = input("ingresa tu nombre: ")
sexo = input("ingresa tu sexo (M o H)?: ")

if sexo == "M" or sexo == "H":
    print("grupo A")
else:
    print("grupo B")

"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por 
pantalla el tipo impositivo que le corresponde."""

rentaAnual = int(input("ingreso de Renta anual: "))


# tipo de impositivo

if rentaAnual < 10000:
    descuento = 0.05
    print("tu impositivo es :", rentaAnual * descuento)
elif rentaAnual < 20000:
    descuento = 0.15
    print("tu impositivo es :", rentaAnual * descuento)
elif rentaAnual < 35000:
    descuento = 0.20
    print("tu impositivo es :", rentaAnual * descuento)
elif rentaAnual < 60000:
    descuento = 0.30
    print("tu impositivo es :", rentaAnual * descuento)
elif rentaAnual > 60000:
    descuento = 0.45
    print("tu impositivo es :", rentaAnual * descuento)

"""En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser
0.0, 0.4, 0.6 o más,
pero no valores intermedios entre las cifras mencionadas.
A continuación se muestra una tabla con los niveles 
correspondientes a cada puntuación.
La cantidad de dinero conseguida en cada nivel es de 
2.400€ multiplicada por la puntuación del nivel."""

# Escribir un programa que lea la puntuación del usuario e
# indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

# inaceptable=0.0
# aceptable=0.4
# meritorio=0.6 #"o mas"
# puntuacionUsuario=0.4
puntuacionUsuario = float(input("ingresa tu puntuacion: "))

if puntuacionUsuario == 0.0:
    print(
        "Rendimiento Inaceptable",
        puntuacionUsuario,
        "cantidad de dinero conseguido",
        puntuacionUsuario * 2.400,
    )
elif puntuacionUsuario == 0.4:
    print(
        "Rendimiento Aceptable",
        puntuacionUsuario,
        "cantidad de dinero conseguido",
        puntuacionUsuario * 2.400,
    )
elif puntuacionUsuario >= 0.6:
    print(
        "Rendimiento Meritorio",
        puntuacionUsuario,
        "cantidad de dinero conseguido",
        puntuacionUsuario * 2.400,
    )

"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar 
gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€."""

# edad
# precio de entrada

edad = int(input("ingresa tu edad : "))

if edad < 4:
    print("Entra gratis")
if edad > 4:
    precio = 5
    print("Debes pagar:", precio, "$")
if edad > 18:
    precio = 10
    print("Debes pagar:", precio, "$")


"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
que lleva."""


#pizza vegerariana-> pimiento y tofu
#pizza no Vegetariana ->Peperoni, Jamón y Salmón.

pizaa=input("que tipo de pizza quieres (vegetariana o no )?: ")


    

