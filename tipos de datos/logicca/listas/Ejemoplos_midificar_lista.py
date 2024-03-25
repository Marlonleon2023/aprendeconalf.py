"""Creacion de listas"""

creacion = ["avion", "ave", "tortuga", "perro", "gato", "celular"]
# longitud de la lista
print(len(creacion))

"""Obtenga el primer elemento, el elemento del medio y el último elemento de la lista."""
print(
    "1 element", creacion[0], "segun elemt", creacion[2], "final element", creacion[5]
)

"""Declare una lista llamada Mixed_data_types, ponga su (nombre, edad, altura, estado civil, dirección)"""

Mixed_data_types = ["marlon", 22, 1.60, "soltero", "limon"]

print(Mixed_data_types)

"""Declare una variable de lista llamada it_companies y asigne valores iniciales Facebook, 
Google, Microsoft, Apple, IBM, Oracle y Amazon."""
print("COMPAÑIAS")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Imprimir el número de empresas de la lista.
print(len(it_companies))

# Imprimir la primera, mediana y última empresa.
print("primera", it_companies[0], "mediana", it_companies[3], "ultima", it_companies[6])

# Imprimir la lista después de modificar una de las empresas
it_companies[3] = "Instagram"
print(it_companies)

# Agregar una empresa de TI a it_companies

it_companies.insert(4, "Ti")
print(it_companies)

it_companies[3] = "APPLE"
print(it_companies)

"""Compruebe si una determinada empresa existe en la lista it_companies."""
print("Facebook" in it_companies)

"""Ordenar la lista usando el método sort()"""
it_companies.sort()
print(it_companies)

"""Invierta la lista en orden descendente usando el método reverse"""
it_companies.reverse()
print(it_companies)

#Elimine las primeras 3 empresas de la lista
#it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[0:2]
it_companies.clear()
print("Elemetos eliminados",it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

listaUnidas=front_end+back_end

print(listaUnidas)

"""Después de unirse a las listas en la pregunta 26. Copie la lista unida 
y asígnela a una variable full_stack. Luego inserte Python y SQL después de Redux."""
print("LISTAS UNIDAS")
listaUnidas.extend(["SQL","Redux"])
print(listaUnidas)