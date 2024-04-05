"""Contador Regresivo: Escribe un bucle while que cuente hacia atrás desde 10 hasta 1."""
contador=10

while contador>0:
    print(contador)
    contador-=1
    
import random
"""Adivinar el Número: Escribe un programa que genere un número aleatorio y pida al usuario adivinarlo. 
Utiliza un bucle while para permitir múltiples intentos hasta que el usuario adivine el número correcto."""
print("numero aleatorio")
aleatoria=random.randint(1,10)
while True:
    adivinalo=int(input("adivina un numero del 1 al 20 si quieres  salir ingresa (0): "))
    if adivinalo==0:
        print("gracias por jugar")
        break
    elif aleatoria==adivinalo:
        print("has adivinado",aleatoria)
    else:
        print("vuelve a intentarlo")
        
        
        

    
    
    

    