"""Creando listas"""

#listas = ["Lunes", "Martes", "Miercoles" ,"jueves","viernes",4,3,6,7,8,[1,2,3],True]
#print(listas[1:3])
#print(len(listas)) cntar el numero de datos guardados 
listas=[1,2,3,4,5]
#listas.append(6) agregar un elemento a la lista en el final
#listas.append("marlon") se puede volver a agregar
#listas.insert(2,3) #agregar el valor colocando el indice despues el numero deseado
#listas.extend([6,7,8]) #agregar varios elementos de golpe 
print((listas))



"""Buscar un elemento en la lista"""
#lista =[1,2,3,4,5,"marlon"]
#saber si un elemento esta dentro de la lista o no

#print(10 in lista)


"""En que indice se ubica dicho elemento """
#print(lista.index("marlon"))

"""Valores Repetidos"""

#determinar cuaantos valores existes
#lista =[1,2,3,4,5,"marlon",1,2,3,1,"marlon"]
#print(lista.count("marlon")) 

"""Eliminar un dato en la lista"""
# del lista[0:2] elimina varios elemntos de una lista con su indice inicial hasta donde deses
#lista.pop(3) #busca en el indice para eliminar
#lista.remove(5) #elimina directamente el numero dado
#lista.clear()   #limpiar o borrar la lista 
#print(lista)


"""Invertir una lista en reverso"""

#lista.reverse()
#print(lista)

"""Elemmetos que se copien dos veces listaa"""
#lista =[1,2,3,4,5,"marlon"]*2

"""Ordenar los elementos de la lista"""
lista =[5,4,-7,9,0,1,3]
lista.sort(reverse=True) # al contrario reverse= true

print(lista)

"""Sumar buscar la edad maxima y la edad minima en una lista"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()  # Ordenar una lista
edadPromedio=sum(ages)/10  # sum sumar datos de una lista 
mediana=ages[4:5]
edadMediana=sum(mediana)/2 
edadMaxima=max(ages) # sacar el valor maximmmo de una lista 
edadMinima=min(ages) # sacar el valor minimo de una lista

