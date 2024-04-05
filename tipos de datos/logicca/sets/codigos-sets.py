"""Agregue un elemento usando add()"""
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')   # add() agrega un elemento a la lista 

"""Agregue varios elementos usando update() La actualización() 
permite agregar varios elementos a un conjunto. La actualización() toma un argumento de lista."""

st.update(['item5','item6','item7'])

"""Eliminar elementos de un conjunto"""
st.remove('item2')

"""Eliminar un elemmento aleatorio de una lista y devuelve el eliminado métodos pop() """
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

#Si estamos interesados ​​en el artículo eliminado.

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 

"""Borrar un elemento de un conjunto """
st.clear()

"""Eliminar un conjunto """
del st

"""Encontrar elementos de intersección"""
st1.intersection(st2) # {'item3', 'item2'}

"""Comprobar la diferencia entre dos conjuntos"""
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

"""Encontrar la diferencia simétrica entre dos conjuntos"""
st2.symmetric_difference(st1) # {'item1', 'item4'}

"""Unir conjuntos Si dos conjuntos no tienen uno o más elementos en común, los llamamos conjuntos disjuntos.
Podemos comprobar si dos conjuntos son conjuntos o separados utilizando el método isdisjoint() ."""

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

"""Unir conjuntos"""
#Podemos unir dos conjuntos usando el método union() o update() .
st3 = st1.union(st2)

"""Comprobación de subconjunto y superconjunto"""
#Subconjunto: essubconjunto()
#Superconjunto: essuperconjunto
st2.issubset(st1) # True
st1.issuperset(st2) # True

"""Conversión de lista a conjunto"""
st = set(lst)