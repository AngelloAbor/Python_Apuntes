#listas

my_list = list()

my_other_list = []

print(len(my_list))

my_list =[35, 24, 62,30, 30, 17]

print(my_list)

print(len(my_list))

my_other_list =[26, 1.83, "Angello", "Orrego"]

print(my_other_list)

print(my_other_list[0])

#trabajar con elementos de una lista

my_other_list.append("Abor dev")
print(my_other_list)

my_other_list.insert(1, "soltero")
print(my_other_list)

my_other_list[1] = "cazado"
print(my_other_list)

my_other_list.remove("cazado")
print(my_other_list)

my_other_list.pop()
print(my_other_list)

del my_other_list[0]
print(my_other_list)

my_other_list.reverse()
print(my_other_list)

my_other_list.clear()
print (my_other_list)
