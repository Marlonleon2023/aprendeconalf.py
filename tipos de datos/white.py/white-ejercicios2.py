"""Suma de Números Pares:
Escribe un bucle while que sume todos los números pares del 1 al 100."""

contador = 1
suma = 0
while contador < 100:
    contador += 1
    if contador % 2 == 0:
        suma += contador
        print("pares", contador)
print("suma", suma)


"""Validación de Entrada: Escribe un bucle while que solicite al usuario ingresar un 
número entre 1 y 10,
y continúe solicitando la entrada hasta que el usuario ingrese un número válido."""

numeroValido = 5

while True:
    ingresaNumber = int(input("ingresa un numero del 1 al  10: "))
    if ingresaNumber == numeroValido:
        print("El numero es valido")
        break
    elif ingresaNumber != numeroValido:
        print("numero invalido")
