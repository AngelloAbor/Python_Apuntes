# regular expresion

#comprobar si una cadena de texto puede poseer algun elemento
import re

my_string = "Esta es la leccion numero 7:  Leccion de Expresiones regulares."

my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros."

#match nusca desde el comienzo
match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])



match = print(re.match("Esta no es la leccion", my_other_string))
if not (match == None):
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])


print(re.match("Esta es la leccion", my_other_string))

print(re.match("Expresiones regulares.", my_string))


# search busca en cualquier sitio

search = re.search("leccion", my_string, re.I)
print(search)
start,end = search.span()
print(my_string[start:end])

# findall crea un listado con las veces que lo encuentra

findall = re.findall("leccion", my_string, re.I)
print(findall)


#split crea una lista dividiendo el termino que colocamos en este leccion es el punto que utilizamos para dividir la cadena de texto

split = re.split("leccion", my_string, re.I)
print(split)

#sub modifica la palabra que encuentra con la que colocamos
print(re.sub("Expresiones", "expresiones", my_string))


#PATTERNS
# crea una lista con las coincidencias encontradas 

pattern = r"leccion|Expresiones"

print(re.findall(pattern, my_string))