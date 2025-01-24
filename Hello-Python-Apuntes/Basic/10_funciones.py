### funciones
# def nombre_funcion(parametros):

def my_function():
    print("esto es una funcion")

my_function()

# Función con parámetros de entrada/argumentos
def suma_dos_valores (valor_uno: int, valor_dos):
    print(valor_uno + valor_dos)

suma_dos_valores(5, 7)
suma_dos_valores ("5", "7")
suma_dos_valores (1.4, 5.6)


# Función con parámetros de entrada/argumentos y retorno

def suma_dos_valores_con_retorno(valor_uno, valor_dos):
    mi_suma = valor_uno + valor_dos
    return mi_suma

mi_resultado = suma_dos_valores(1.4, 5.2)
print(mi_resultado)

mi_resultado = suma_dos_valores_con_retorno(10, 5)
print(mi_resultado)



# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Orrego", name="Angello")




# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Angello", "Orrego")
print_name_with_default("Angello", "Orrego", "Abor")

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")
