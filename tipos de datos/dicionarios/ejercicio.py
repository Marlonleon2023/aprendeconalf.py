"""Desarrolla un programa en Python que permita al usuario ingresar información sobre varias personas. 
El programa debe solicitar al usuario que ingrese el nombre y la edad de cada persona.
Una vez que el usuario haya ingresado la información de todas las personas, 
el programa debe imprimir un mensaje indicando si cada persona es menor o mayor de edad. 
El programa debe continuar permitiendo al usuario ingresar información hasta que decida terminar"""

# usuario pueda ingresasr inforcion sobre varias personas
# debe perdir nombre y edad de cada persona 
# un mensaje si el usuario es menor o mayor de edad 
#hasta que el decida terminar 

personas=[]




while True:
    nombre=input("Ingresa tu Nombre si deseas  terminar ingresa -> 'salir' : ")
    if nombre.lower()=='salir':
        print("haz terminado")
        break
    edad=int(input("ingresa tu edad: "))
    
    if edad >=18:
        estado="eres mayor de edad"
    elif edad<18:
        estado="eres menor de edad "
        
    persona = { 'nombre':nombre,
             'edad':edad,
             'estado':estado
    }
    personas.append(persona)
print(f"{nombre},{estado}\n")
for persona in personas:
    print(f"Nombre:", persona['nombre'], "Edad:", persona['edad'], "Estado:", persona['estado'])
    
        
    
