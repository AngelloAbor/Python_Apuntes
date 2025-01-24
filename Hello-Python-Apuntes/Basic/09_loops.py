#loops

#bucles/loops/ciclos iterativos

my_condition = 0

print("While loop")
while my_condition < 10:
    print(my_condition)
    my_condition += 1
print("End of the loop")

my_condition = 1
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print ("es igual a 15")
        break
    print(my_condition)
print("hola")

#for

my_list = [1, 2, 3, 4, 5, 6]

for element in my_list:
    print(element)

my_tuple = ( 26, 1.83, "Angello", "Orrego" )

for element in my_tuple:
    print(element)

my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)


my_dict ={
    'nombre': 'angello',
    'apellido': 'orrego',
    'edad': 26,
    'mascota': 'tocino',
    'lenguajes': {"python", "HTML", "CSS", "JS"},
}

for element in my_dict:
    print(element) #con los diccionarios iteramos las claves no los valores que esta posee