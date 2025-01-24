### SETS ###
#que es un sets
#un set es una coleccion desordenada de elementos unicos
my_set = set()
print(type(my_set))
my_other_set = {1, 2, 3, 4, 5, 5}
print(type(my_other_set))
print(my_other_set)

print(len(my_other_set))

# print(my_other_set[0]) #error


my_other_set.add("hola")
print(my_other_set)

my_other_set.add("hola")
print(my_other_set)
#los set no admiten repetidos.


my_other_set.add(6)
print(my_other_set)

my_other_set.add("Angello")
print(my_other_set)
#los set no tienen orden
#son mutables

print("Angello" in my_other_set)
print("bingo" in my_other_set)
print("Angello" not in my_other_set)
print("bingo" not in my_other_set)


my_other_set.clear() #limpia el set (lo deja vacio)
print(len(my_other_set))

# del my_other_set #lo elimina

my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print(my_list)

my_other_set = {6, 7, 8, 9, 10}

my_new_set = my_set.union(my_other_set)

print(my_new_set)

print(my_new_set.union(my_set).union(my_other_set).union({"HOLA"}))

print(my_new_set.difference(my_set))