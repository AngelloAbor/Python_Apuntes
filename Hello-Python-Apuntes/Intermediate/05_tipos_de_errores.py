### error types

#syntax Error es un error de sintaxis (normalmente algo mal escrito falta de parentesis comas etc)

# print "hola"

#nameERROR por llamar una variable no definida o una variable mal escrita
name = 5
print(name)

#index error no encuentra el elemento ya que no pertenece  la lista

my_list = ["python", "java", "c", "javascript"]

# print(my_list[8])

# module not found

#import maths

import math

print(math.pi)

# attribute error cuando un modulo no pose x atributo nos lanza ese error
#print(math.PI)


#KEY ERRORS error a asociado a la clave de un diccionario en este caso al llamar una posicion 0 el diccionario entiende que buscamos una key llamada 0 la cual no existe

my_dict = {
    "nombre": "angello",
    "apellido": "orrego",
    "edad": 26
}

#print(my_dict[0])
print(my_dict["edad"])


#type error es cuando pasamos un tipo de dato que no se utiliza en una funcion ejemplo darle un string a una lista que busca x posicionamiento el cual solicita un numero no un str

#print(my_list["python"]) 
print(my_list[0])

#import error importamos algo y no lo localiza

#from math import PI
from math import pi
print(pi)

#value error, error al convertir un valor a otro ejemplo texto a numero
my_int = int("10 años")
#print(my_int)

#zero division error  error al dividir por 0