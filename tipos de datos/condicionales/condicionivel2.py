"""Consulta si la temporada es Otoño, Invierno, Primavera o Verano.
Si la entrada del usuario es: septiembre, octubre o noviembre, la temporada es otoño.
Diciembre, enero o febrero, la temporada es invierno.
Marzo, abril o mayo, la temporada es primavera 
Junio, julio o agosto, la temporada es verano"""

mes=input("ingresa el mes que deseas consultar: ").lower()

if mes in ["septiembre","octubre","noviembre"]:
    print("Temporada de Otoño")
elif mes in ["diciembre","enero","febrero"]:
    print("Temporada de Invierno")
elif mes in ["marzo","abril","mayo"]:
    print("teporada de primmavera")
elif mes in ["junio","julio","agosto"]:
    print("Teporada de Verano")
else:
    print("Temporada no valida")
    
    
"""La siguiente lista contiene algunas frutas:
Si una fruta no existe en la lista, agregue la fruta a la lista e imprima la lista modificada. 
Si la fruta existe print('Esa fruta ya existe en la lista')"""


fruits = ['banana', 'orange', 'mango', 'lemon']

fruitsm=input("ingrea la fruta que quieres : ")

if fruitsm not in fruits:
    fruits.append(fruitsm)
    print(fruits)
else:
    print("Esa fruta ya existe en la lista")




"""Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!
    """
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

"""Verificar si el diccionario 'person' tiene la clave 'skills'; si es así, imprimir 
la habilidad intermedia en la lista de habilidades.  ---->🔥
Verificar si el diccionario 'person' tiene la clave 'skills'; si es así, 
verificar si la persona tiene la habilidad 'Python' e imprimir el resultado.🔥
Si las habilidades de una persona son solo JavaScript y React, imprimir('Es un desarrollador front-end'); 🔥
si las habilidades de una persona son Node, Python, MongoDB, imprimir('Es un desarrollador back-end'); 🔥
si las habilidades de una persona son React, Node y MongoDB, imprimir('Es un desarrollador fullstack');🔥
de lo contrario, imprimir('Título desconocido') - ¡para resultados más precisos, se pueden anidar más condiciones!
Si la persona está casada y si vive en Finlandia, imprimir la información en el siguiente formato:"""

if "skills" in person:
    skills=person["skills"]
    if len (skills)>=3:
        print("habilidad intermedia: ", skills[len(skills)//2])
    if "Python" in skills:
         print("la persona tiene la habilidad python")


if "skills" in person:
    skills = person["skills"]
    if skills == ["JavaScript", "React"]:
        print("Es un desarrollador front-end")
    elif set(skills) == {"Node", "Python", "MongoDB"}:
        print("Es un desarrollador back-end")
    elif set(skills) == {"React", "Node", "MongoDB"}:
        print("Es un desarrollador fullstack")
    else:
        print("Título desconocido")

if person.get("is_married") and person.get("country") == "Finland":
    print(f"Nombre: {person['first_name']} {person['last_name']}, Edad: {person['age']}, País: {person['country']}, Estado Civil: Casado")