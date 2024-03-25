"""Crea una tupla vacía"""

"""Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
Únase a tuplas de hermanos y hermanas y asígnelas a hermanos
¿Cuántos hermanos tiene usted?
Modifica la tupla de hermanos y agrega el nombre de tu padre y tu madre y asígnalo a family_members"""

conjunto = ("marlon", "sarai", "breiner", "samuel")

print("¿Cuántos hermanos tiene usted?: ", len(conjunto))

conjuntoFamiliar = ("andres", "jhoana")

family_members = conjunto + conjuntoFamiliar
print("tu grupo familiar es: ", family_members)

"""jercicios: Nivel 2
Desempaquetar hermanos y padres de family_members
Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una 
variable llamada food_stuff_tp.
Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
Corte el elemento o elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.
Corte los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt
Eliminar completamente la tupla food_staff_tp
Compruebe si existe un elemento en tupla:
Compruebe si 'Estonia' es un país nórdico

Compruebe si 'Islandia' es un país nórdico

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')"""

hemanos = family_members[0:4]
padres = family_members[4:6]
print("hermanos", hemanos, "padres", padres)


frutas = ("Manzana", "Pera", "Fresas", "Mango")
verduras = ("Tomate", "Espinacas", "Zanahoria", "Apio")
ProductosAnimales = ("Leche", "Carne", "Pollo")

food_stuff_tp = frutas + verduras + ProductosAnimales
print(food_stuff_tp)

print(food_stuff_tp)

food_stuff_lt = food_stuff_tp[
    :
]  # copia la tupla [:] los corchetes 2 puntos o la duplica
mitades = food_stuff_lt[4:6]
primeros = food_stuff_lt[0:3]
ultimos = food_stuff_lt[7:10]
print("it", food_stuff_lt)
print("mitades", mitades, "primeros", primeros, "ultimos", ultimos)


del food_stuff_tp


nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

print("es un pais nordico: ", nordic_countries in ["Islandia"])
