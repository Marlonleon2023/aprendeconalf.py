# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}


# Encuentra la longitud del conjunto it_companies
print(len(it_companies))

# Añade 'Twitter' a it_companies
it_companies.add("twitter")

print(it_companies)

"""Inserte varias empresas de TI a la vez en el conjunto it_companies"""
print("Inserte varias empresas de TI a la vez en el conjunto it_companies")
it_companies.update(["Samsung", "Alphabet", "Inte"])
print(it_companies)

"""Eliminar una de las empresas del conjunto it_companies"""
print("Eliminar una de las empresas del conjunto it_companies")
it_companies.remove("IBM")
print(it_companies)

"""¿Cuál es la diferencia entre eliminar y descartar?"""
# eliminar elimina el elmento del conjunnto y descartar la deja a un lado


# ejercicio 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


"""Unir A y B"""
C = A.union(B)
print(C)

"""Encuentra una intersección B"""
A.intersection(B)
print(A)

"""es un subconjunto de b"""
print("Es un subconjunto")
print(A.issubset(B))

"""¿Son A y B conjuntos disjuntos?"""
print("Son disjuntos")
print(A.isdisjoint(B))

"""Unir A con B y B con A"""
A = A.union(B)
B = B.union(A)
print(A, B)

"""¿Cuál es la diferencia simétrica entre A y B?"""
simetria = A.symmetric_difference(B)
print(simetria)  # nunguna soy iguales


del (A, B)
print()


# Ejercicios: Nivel 3

print("edades")
age = [22, 19, 24, 25, 26, 24, 25, 24]
"""Convierte las edades a un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es mayor?"""
st = set(age)
print(st)

"""En resumen, las cadenas son secuencias inmutables de caracteres, 
las listas son secuencias mutables de elementos, las tuplas son secuencias
inmutables de elementos y los conjuntos son colecciones no ordenadas de elementos únicos.
Cada tipo de datos tiene sus propias características y se utiliza en diferentes contextos
según los requisitos del problema."""


#<-------------------.---------------------->

"""Soy profesora y me encanta inspirar y enseñar a la gente. ¿Cuántas palabras únicas se han usado en la oración?
Utilice los métodos de división y configúrelo para obtener palabras únicas."""
oracion=('Soy profesora y me encanta inspirar y enseñar a la gente')
unicas=oracion.split()
unicas=set(oracion)
cantidadDePalabras=len(unicas)
print(unicas)