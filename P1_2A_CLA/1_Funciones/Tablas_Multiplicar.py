"""
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones:
1.- Sin estructuras de control
2.- Sin funciones 

"""

#Version 1
num=int("Inserta el numero de la tabla de multiplicar: ")
multi=num*1
print(f"2 x 1 = {milti}")
multi=num*2
print(f"{num} x 2 = {milti}")
multi=num*3
print(f"{num} x 3 = {milti}")
multi=num*4
print(f"{num} x 4 = {milti}")
multi=num*5
print(f"{num} x 5 = {milti}")
multi=num*6
print(f"{num} x 6 = {milti}")
multi=num*7
print(f"{num} x 7 = {milti}")
multi=num*8
print(f"{num} x 8 = {milti}")
multi=num*9
print(f"{num} x 9 = {milti}")
multi=num*10
print(f"{num} x 10 = {milti}")



#Version 2
"""
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones:
1.- con estructuras de control
2.- Sin funciones 

"""

num=int(input("ingrese el numero de la tabla de multiplicar"))
for i in range(1,11,1):
    multi=num*i
    print(f"{num} x {i} = {multi}")

    #Version 3
"""
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones:
1.- con estructuras de control
2.- con funciones 

"""

num=int(input("ingrese el numero de la tabla de multiplicar"))
for i in range(1,11,1):
    multi=num*i
    print(f"{num} x {i} = {multi}")
