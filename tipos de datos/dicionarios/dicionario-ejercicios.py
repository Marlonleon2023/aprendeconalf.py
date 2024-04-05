"""Agregue nombre, color, raza, patas y edad al diccionario de perros"""


perro = {
    'nombre':'manchas',
    'color':'negro y blanco',
    'raza':'criolla',
    'patas':'cuatro',
    'edad':2,
}


"""Cree un diccionario de estudiantes y agregue nombre,
apellido, sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario."""

estudiantes = {
           'nombre':'Marlon Esteban',
           'apellido':'Leon Rojas',
           'Sexo':'Hombre',
           'edad':22,
           'estado civil':'Soltero',
           'habilidades':['inteligentes', 'proativo', 'positivo'],
           'pais':'Colombia',
           'ciudad':'Ibague',
           'dirreccion':'Mz a casa 19 b',
           }

#Obtener la longitud del diccionario del estudiante
print(len(estudiantes))
#Obtenga el valor de las habilidades y verifique el tipo de datos, debería ser una lista
#print(estudiantes['Habilidades'], "que tipo es",type(estudiantes['Habilidades']))

#Modifique los valores de las habilidades agregando una o dos habilidades
estudiantes['habilidades'].append('correr')
estudiantes['habilidades'].append('saltar')


print(estudiantes)

"""Obtenga las claves del diccionario como una lista"""

keys=estudiantes.keys()

print("claves en listas",keys)

"""Obtener los valores del diccionario como una lista"""

values=estudiantes.values()
print("valores",values)

"""Cambie el diccionario a una lista de tuplas usando el método items()"""


print("cambiando a lista ",estudiantes.items())

"""Eliminar uno de los elementos del diccionario"""

estudiantes.pop('habilidades')
print(estudiantes)

#Eliminar uno de los diccionarios

del estudiantes


    
              