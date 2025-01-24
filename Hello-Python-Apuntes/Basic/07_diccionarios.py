#DICCIONARIOS
# Son colecciones desordenadas de elementos. Se diferencian de las listas porque los elementos se acceden no por un índice, sino por una clave.

# Creación de un diccionario
my_dict =dict()

my_other_dict = {
    'nombre': 'angello',
    'apellido': 'orrego',
    'edad': 26,
    'mascota': 'tocino',
}

print(type(my_dict))
print(type(my_other_dict))

print(my_other_dict)

my_dict ={
    'nombre': 'angello',
    'apellido': 'orrego',
    'edad': 26,
    'mascota': 'tocino',
    'lenguajes': {"python", "HTML", "CSS", "JS"},
}

print(my_dict)

print(len(my_dict))

# Acceder a un elemento de un diccionario
print(my_dict['nombre'])
#print(my_dict[0]) #esto no funciona ya que 0 no es un elemento no se puede buscar por posicion


my_dict["Direccion"] = "Calle 123" #agregar un nuevo elemento al diccionario
print(my_dict)

#como eliminar elementos
del my_dict['Direccion']
print(my_dict)

#podemos buscar nombres del campo no de datos dentro del diccionario
print("angello" in my_dict)
print("nombre" in my_dict)

print(my_dict.items())#
print(my_dict.keys())#
print(my_dict.values())#

numeros = [1,2,3]

result= dict.fromkeys(numeros)
print(result)

numeros = [1,2,3]
value = 0
result= dict.fromkeys(numeros, value)
print(result)

numeros = [1,2,3]

result= dict.fromkeys(numeros, "hola")
print(result)