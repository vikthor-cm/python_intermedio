# Calcular el mayor de dos números ingresados por teclado usando un operador ternario.
# nro1 = float(input("Ingrese el primer numero: "))
# nro2 = float(input("Ingrese el segundo numero: "))

# print(f"El mayor numero de los ingresados es el {f"primer numero: {nro1:.2f}" if nro1 > nro2 else f"segundo numero: {nro2:.2f}"}")
#mejor seria guardar el mayor y despues armar todo pero bueno para probar.


# Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

# lista_palabras = ["gato", "perro", "tortuga", "loro", "conejo"]

# def buscar_palabra(palabra_buscada, *args):
#     resultado = "Palabra encontrada." if palabra_buscada in args else "palabra no encontrada."
#     return resultado

# palabra_ingresada = input("Ingrese la palabra a buscar: ") 
# #puede tener el mismo nombre palabara_buscada pero es mas legible asi, no coliciona xq puedo llamarla como quiera desde la llamada y no afecta al nombre de como esta el argumento definido ene la funcoin 

# print(buscar_palabra(palabra_ingresada, *lista_palabras))

# Determinar si un número es par o impar
# nro3 = int(input("Ingrese un numero entero para determinar su paridad: "))
# paridad = "par" if nro3 % 2 == 0 else "impar"
# print(f"El numero ingresado es {paridad}.")

# Calcular el promedio de una lista de números usando args y un operador ternario

# def calcular_promedio(*args):
#     promedio = sum(args)/len(args) if len(args) > 0 else 0.0
#     return promedio

# nros = [6, 8, 8, 10, 6]

# promedio = calcular_promedio(*nros)
# print(f"El promedio de los numeros es: {promedio}")

# nros2 = []
# # vacio o negativo
# promedio = calcular_promedio(*nros2)
# print(f"El promedio de los numeros es: {promedio}")

# Imprimir un mensaje de error si no se pasan suficientes argumentos.

# def carga_argumentos(*args):

#     resultado = "Se realizaron las operaciones adecuadas." if len(args) >= 4 else "No se cargaron suficientes datos para realizar las operaciones."
#     return resultado

# lista_args = ["uno", "dos", "tres", "cuatro"]

# print(carga_argumentos(*lista_args))

# lista_args = ["uno", "dos"]

# print(carga_argumentos(*lista_args))


def carga_argumentos(*args):

    resultado = "Se realizaron las operaciones adecuadas." if len(args) >= 4 else "No se cargaron suficientes datos para realizar las operaciones."
    return resultado


# ya q estamos hacemos una funcion para cargar los datos
def ingreso_datos ():
    lista_args = []
    cant_nros = int(input("Ingrese la cantidad de numeros que va a ingresar: "))
    # vamos a ingresar nros en ves de palabras 

    for i in range(cant_nros):
        nro = int(input(f"Ingrese el numero de la posicion {i+1}: "))
        lista_args.append(nro)
    return lista_args
    # mejor seria un while pero tendria q preguntar cada ves, o sino poner un caracter de finalizacion, despues ver...

print(carga_argumentos(*(ingreso_datos ())))











