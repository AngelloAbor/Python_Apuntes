# exception handling
# parecido al try catch

numberOne = 5
numberTwo = 1

#numberTwo = "1"

#excepcion base: try except

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")
except:
    #se ejecuta si se produce una exepcion
    print("se ha producido un error")


# flujo completo de una excepcion: try except else finally

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")
except:
    #se ejecuta si se produce una exepcion
    print("se ha producido un error")
else: # se ejecuta si no se produce la excepcion
    print("la ejecucion continua correctamente")
finally: #opcional
    #se ejecuta siempre
    print("la ejecucion continua")

    
# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
