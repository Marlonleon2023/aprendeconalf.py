"""Escribir un programa que pida al usuario una palabra y luego muestre 
por pantalla una a una las letras de la palabra introducida empezando por la última."""

palabra = input("ingresa una palabra: ")
for x in palabra:
    print(x)


"""Escribir un programa en el que se pregunte al usuario por una frase
y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."""
# frase
# letra
frase = input("ingresa una frace: ")
letra = input("ingresa una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(
    "numero de letras encontrada con la :",
    letra,
    "es",
    contador,
    "la frase es : ",
    frase,
)


"""Escribir un programa que muestre el eco de todo 
lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""

x = "salir"
while True:
    ingreseloqueSea = input(
        "ingresa cualquier palabra para termina ingresa (salir): "
    ).lower()
    if ingreseloqueSea == x:
        break
print("gracias por usar nuestro programa")
