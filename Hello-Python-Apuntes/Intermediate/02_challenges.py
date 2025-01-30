## retos de codigo

'''
El famoso FIZZ BUZZ
Escribe un programa que muestre por consola los numeros de 1 a 100 (includios y con salto de linea entre cada impresion) sustituyendo los siguientes:
- multiplos de 3 por la palabra fizz
multiplos de 5 por la palabra buzz
multiplos de 3 y 5 fizzbuzz
'''
def fizzbuzz():
    for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)
fizzbuzz()

'''
Es un anagrama
Escribe una funcion que reciba dos cadenas y retorne True si son anagramas o False si no lo son
un anagrama consiste en formar una palabra reordenando las letras de la palabra inicial
2 palabras iguales no son anagramas
'''

def is_anagram(str1, str2):
    if str1.lower() == str2.lower():
        return False
    elif sorted(str1.lower()) == sorted(str2.lower()):
        return True
    else:
        return False

print(is_anagram("HOLAa","aloh"))

'''
Fibonacci
Escribe un programa que imprima los 50 primeros numeros de la sucesion de fibonacci empezando en 0
    la serie fibonacci se compone por una sucesion de numeros en la que el siguiente numero siempre es la suma de los 2 anteriores
'''



def fibonacci():
    num1 = 0
    num2= 1
    for i in range(0,51):
        print (num1)
        fib = num1 + num2
        num1 = num2
        num2 = fib
fibonacci()

def fibonacci_50():
    a,b = 0, 1
    while a < 50:
        print(a)
        a,b = b, a+b
fibonacci_50()


'''
Es un numero primo?

escribe un programa que se encargue de comprobar si un numero es priomo o no
imprime los numeros de 1 a 100 y di si lo es
'''

def es_primo():
        for numero in range(1, 101):
            if numero >= 2:
                is_divisible = False
                for index in range(2, numero):
                    if numero %  index == 0:
                        is_divisible = True
                        break
                if  not is_divisible:
                    print(numero)
es_primo()
