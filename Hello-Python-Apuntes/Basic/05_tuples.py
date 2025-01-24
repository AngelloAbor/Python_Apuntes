### tuplas

my_tuple = tuple()

my_other_tuple = ( 23, 1.60, "Jenifer", "Savoy")

my_tuple = ( 26, 1.83, "Angello", "Orrego" )

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])

print(my_tuple.count("Angello"))

print(my_tuple.index(1.83))

#las tuplas no permiten cambiar los elementos que la componen. no son mutables
#my_tuple[0]=27 
#print(my_tuple)
#esto tira error

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
#esto crea una nueva tupla con los elementos de las tuplas sumadas
print(my_tuple[1:6])
#esto imprime los elementos de la tupla desde el indice 1 hasta el 6

##como editar una tupla
my_tuple = list(my_tuple)
my_tuple[0] = 27
my_tuple.insert(2,"Abor")
print(my_tuple)
print(type(my_tuple))
my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)
#transformamos la tupla a lista para poder modificarla para luego una vez modificada volverla otra ves a tupla

del my_tuple