#file handling

#.txt file
import xml
import csv
import os
import json

txt_file = open("Hello-Python-Apuntes\Intermediate\my_file.txt", "r+")
txt_file.write(
    "Mi nombre es Angello \nMi apellido es Orrego\nTengo 26 años\nQuiero aprender python")



#print(txt_file.read())
#print(txt_file.readline())
#print(txt_file.readline())
#for line in txt_file.readlines():
#    print(line)

txt_file.write("\nvivo en chile hola")
print(txt_file.readline())


#.json file
import json

json_file = open("Hello-Python-Apuntes\Intermediate\my_file.json", "w+")

json_test = {
    "nombre": "Angello",
    "surname": "Orrego",
    "edad": 26,
    "lenguajes": ["Python", "html", "css"],
    "website": "abor.com"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

json_dict = json.load(open("Hello-Python-Apuntes\Intermediate\my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["nombre"])


#.csv file 

csv_file = open("Hello-Python-Apuntes\Intermediate\my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Nombre", "Apellido", "Edad", "Lenguaje"])
csv_writer.writerow(["Angello", "Orrego", "26", "Python"])
csv_writer.writerow(["Jeni", "", "23", ""])

csv_file.close()

with open("Hello-Python-Apuntes\Intermediate\my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)