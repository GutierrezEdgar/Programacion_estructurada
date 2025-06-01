"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

# 1.- Funcion que no recibe parametros y no regresa valor
def solocitarDatos1():
    nombre=input("nombre: ")
    telefono=input("Telefono: ")
    print(f"nombre: {nombre} y su telefono {telefono}")

# 3.- Funcion que recibe parametros y no regresa valor
def solocitarDatos3(nom,tel):
    nombre=nom
    telefono=tel
    print(f"nombre: {nombre} y su telefono {telefono}")

# 2.- Funcion que no recibe parametros y regresa valor
def solocitarDatos2():
    nombre=input("nombre: ")
    telefono=input("Telefono: ")
    return nombre,telefono

# 4.- Funcion que recibe parametros y regresa valor
def solocitarDatos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre,telefono

#mandar llamar o invocar las funciones

solocitarDatos1

nombre=input("escribe el nombre: ")
telefono=input("escribe el telefono: ")
solocitarDatos3(nombre,telefono)

nom,tel=solocitarDatos2()
print(f"\t\nLos datos de la agenda son:\n nombre: {nom}\n telefono:{tel} ")

nombre=input("escribe el nombre: ")
telefono=input("escribe el telefono: ")
nom,tel=solocitarDatos4(nombre,telefono)
print(f"\t\nLos datos de la agenda son:\n nombre: {nom}\n telefono:{tel}")