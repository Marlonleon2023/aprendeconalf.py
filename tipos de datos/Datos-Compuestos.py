#Creeando Una lista (se pueden modificar)
lista = ["Lucas Dalto "," soy Dalto",True,1.85]

#Creeando Una tupla (no pueden modificar)

tupla = ("Lucas Dalto","Soy Dalto",True,1.85)


# Esto es Valido
lista [3] = "Maquinola"
# Esto NO
#tupla [3] = "Maquinola"

#creando un conjunto (set) (no se piede llama ra los elemoentos por su indice no almacena duplicados)

conjunto = {"Lucas Dalto","Soy Dalto",True,1.85}

#print(conjunto[3]) -> no se puede acceder al elemento

#  creando un diccionario(dict) (la estructura es key :value y separamos con comas)
Dicionario ={
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'esta emocionado' : True,
    'altura'  : 1.85,
    'dato_duplicado' : "soy Dalto"
}

print(Dicionario['altura'] + 2)


