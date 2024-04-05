""""Desarrolla un programa en Python para un club deportivo que registre a sus miembros.
El programa debe permitir al usuario ingresar el nombre y la edad de cada miembro.
Una vez que el usuario haya ingresado la información de todos los miembros,
el programa debe imprimir un mensaje indicando si cada miembro es elegible para competir
en categorías juveniles o si debe competir en categorías de adultos. 
El programa debe continuar permitiendo al usuario ingresar información hasta que decida terminar."""
# nombre 
# edad 
# programa que registre sus miembros 
#es elegible para competir juveniles o adultos 

personas = []

while True:
    miembro=input("ingresa tu nombre , para terminar --> 'salir' : ")
    if miembro.lower() == 'salir':
        print("haz terminado")
        break
        
    edad=int(input("ingresa tu edad: "))
       
    if edad>=18:
        categoria='adultos'
    elif edad<18:
        categoria='juveniles'
        
    persona = {'miembro':miembro,
                'edad':edad,
                'categorias':categoria
    }
        
    personas.append(persona)
    print(f"{miembro},{categoria}\n")
for persona in personas:
     print(f"Miembro",persona['miembro'],"Edad",persona['edad'],"Categorias",persona['categorias'])
     
     
     
     
     
     
     
        
    
