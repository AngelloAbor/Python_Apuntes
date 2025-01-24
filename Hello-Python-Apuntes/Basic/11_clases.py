### clases

#class MyPerson:
#   pass

#print(MyPerson)


class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Persona("Angello", "Orrego")
print(f"{my_person.name} {my_person.surname}")

class Persona2:
    def __init__(self):
        self.name = "angello"
        self.surname = "orrego"
    def walk(self):
        print(f"{self.name} esta caminando")

my_person2 = Persona2()
print(f"{my_person2.name} {my_person2.surname}")
my_person2.walk()


#class datos:
#    def __init__(self, name, surname):
#        self.full_name = f"[name] [surname]"

#nombre_completo = datos("Angello", "Abor")
#print(nombre_completo.full_name)
