#Strings

my_strings = "Soy un Strings"

print(len(my_strings))

print(my_strings +" como va todo")

new_string = "este es un string \ncon salto de linea"
print(new_string)

string_tab = "\tEste string esta tabulado"
print(string_tab)

#formateo
name, lastname, age = "angello", "orrego", 26
print("mi nombre es {} {} y mi edad es {}".format(name,lastname,age))

print("mi nombre es %s %s y mi edad es %d"%(name,lastname,age))

print("mi nombre es"+ name +" "+ lastname+ " y mi idead es " + str(age))

print(f"mi nomnre es {name} {lastname} y mi idead es {age}")

#desempaquetamiento de caracteres

lenguaje = "python"

a, b, c, d, e, f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#reverse

reversed_lenguaje = lenguaje[::-1]
print(reversed_lenguaje)

#funciones

print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print(lenguaje.lower())
print(lenguaje.upper().isupper())