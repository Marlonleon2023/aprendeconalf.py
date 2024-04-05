"""Creando un diccionario
Para crear un diccionario usamos llaves, {} o la función incorporada dict() ."""


#Ejemplo:

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

"""El diccionario anterior muestra que un valor
puede ser cualquier tipo de datos: cadena, booleano, lista, tupla, conjunto o un diccionario."""


"""longitud de un diccionario"""
# Se en ncuentra igual con la funcion len

print(len(person))


"""Acceder a elementos del diccionario"""
#Podemos acceder a los elementos del Diccionario haciendo referencia a su nombre clave.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4

"""el método get . El método get devuelve Ninguno,
que es un tipo de datos de objeto NoneType, si la clave no existe."""
# Metodo get saber si existe en el diccionario o no 

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

"""Agregar elementos a un diccionario"""
# Normal
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

# se pueden de las dos maneras

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


"""Modificar elementos en un diccionario"""
person['first_name'] = 'Eyob'
person['age'] = 252


"""Comprobación de claves en un diccionario (in)"""
#Usamos el operador in para verificar si existe una clave en un diccionario.

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False


"""Eliminar pares de clave y valor de un diccionario
pop(clave) : elimina el elemento con el nombre de clave especificado:
popitem() : elimina el último elemento
del : elimina un elemento con el nombre de clave especificado"""

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married'] 


"""Cambiar el diccionario a una lista de elementos metodo (items())"""
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dct.items() convierte el diccionario en una lista


"""Borrar un diccionario clear()"""
print(dct.clear()) #dct seria el nombre que le dimos al dicionario .clear borrar


"""Eliminar un diccionario (del dtc)"""
#Si no utilizamos el diccionario podemos borrarlo por completo

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct


"""Copiar un diccionario metodo (copy())"""

#Podemos copiar un diccionario usando un método copy() 
# . Usando la copia podemos evitar la mutación del diccionario original

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


"""Obtener claves de diccionario como una lista metodo keys()"""
#El método keys() nos proporciona todas las claves de un diccionario en forma de lista.

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()   # imprimira el diccionario como una lista mas no la cambiara
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])


"""Obtener valores del diccionario como una lista"""
#El método de valores nos proporciona todos los valores de un diccionario como una lista.

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])







