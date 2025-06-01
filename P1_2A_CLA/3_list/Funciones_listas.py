"""
Liat (Array)
Son colleciones o conjuntos de datos/valores bajo un miasmo nombre, para acceder a los valores se hace con un indice numerico

nota: son valores si son modificables

La lista es una coleccion ordenada y modificable, permite miembros duplicados.

"""

import os
os.system("clear")

#Funciones mas comunes en las listas

paises=["Mexico","Brasil","España","Canada"]

numeros=[23,12,100,34]

varios=["Hola",true,33,3,12]

#Ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)
paises.sort()
print(paises)

#Agregar o insertar o agregar un elemento a la lista
#1er forma
print(paises)
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,Honduras)
print(paises)

#Eliminar o borrar o quitar un elemento a la lista
#1er forma
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da Forma
paises remove("Honduras")
print(paises)


#buscar un elemento dentro de una lista
#paises=["Mexico","Brasil","España","Canada"]

print("Brasil" in paises)

#contar el numero de veces que un elementos esta dentro de una lista
#numeros=[23,12,100,34]
print(numeros)
print(numeros count(12))
numeros insert(1,12)
print(numeros)
print(numeros count(12))

#Dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
print(paises reverse())
print(numeros reverse())
print(numeros)
print(paises)

#conocer el indice o la posicion de un valor de la lista
posicion=paises index("España")

paises[posicion]="ESPAÑA"
print(paises)

#unir el contenido de 2 o mas listas en una sola
#numeros=[23,12,100,34]
numeros2=[300,500,100]

print(numeros)
print(numeros2)
numeros.extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)

