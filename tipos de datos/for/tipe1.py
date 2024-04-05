"""Suma de Números: Escribe un bucle for que sume todos los números del 1 al 100."""
sumaTotal=0
for numero in  range(1,101):
    sumaTotal+=numero
    print(sumaTotal)
    
    

"""Impresión de Elementos: Dado un lista de nombres, escribe un bucle for que imprima cada nombre en la lista."""

nombres = ["Juan", "María", "Pedro", "Ana"]

for listas in nombres:
    print('nombres de la lista son : ',listas)
    
    
"""Tabla de Multiplicación: Escribe un bucle for anidado que genere la tabla de multiplicación del 1 al 10."""
print('Tabla de multiplicar')

for multi in range(2,12):
    for resultad in range(multi):
        multi=1
        total=multi*resultad
    print(f"{multi}x{resultad}={total}")
        
    
"""Búsqueda de Elementos: Dada una lista de números, 
escribe un bucle for que busque un número específico y muestre un mensaje si lo encuentra."""
#lista de numeros 
#buscar numero 
#si es encontrado mostrar numero 
numero=[1,2,3,4,5,6,15,34,56,78,98,44,90]
buscar=78
for ñ in numero:
   if buscar==ñ:
    print("se ha encontrado")
    break
else:
    print('no se ha encontrado')


   
    