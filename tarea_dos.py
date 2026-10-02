# try:
#     nro1 = float(input("Ingrese el primer numero: "))
#     nro2 = float(input("Ingrese el segundo numero: "))

#     division = nro1 / nro2
#     print(division)
# except ZeroDivisionError:
#     print("Error, no se puede dividir por '0'")


# try:
#     nro1 = 10
#     cad1 = "Auto"

#     suma = nro1 + cad1
#     print(suma)
# except TypeError:
#     print("Error, no se puede sumar un numero con una letra.")


# persona = {"nombre": "Juan", "edad": 30}
# try:
#     apellido_persona = persona["apellido"]
# except KeyError:
#     print("Error, no se puede acceder al dato")
    

#archivo1 = r"D:\zestudio\2026 2do cuatri\04. Python intermedio (Viernes 19-21)\Clase 2 - Excepciones\archivo.txt" si creo el archivo uso la ruta completa y ahi si lo toma.
import os

archivo1 = "archivo.txt"
try:
    with open(archivo1, "r") as archivo:
        contenido_arch= archivo.read()
except FileNotFoundError:
    print(f"Error, no existe el archivo: \"{archivo1}\"")

    with open(archivo1, "w") as archivo:
        pass #solo lo creamos no guardamos nada
    print(f"Se creo el archivo: \"{archivo1}\"")
    print(f"El archivo creado se guardo en: {os.path.abspath(archivo1)}") #para saber donde se guardo

#para evitar lo de la ruta usamos os se importa, obtiene la carpeta donde esta actualemnte el codigo gauradado
#luego lo concatena usando la barra segun tu os

# import os

# carpeta_actual = os.path.dirname(__file__)

# archivo1 = os.path.join(carpeta_actual, "archivo.txt")

# try:
#     with open(archivo1, "r") as archivo:
#         contenido_arch= archivo.read()
# except FileNotFoundError:
#     print(f"Error, no existe el archivo: \"{os.path.basename(archivo1)}\"")


# try:
#     nro1 = float(input("Ingrese el primer numero: "))
#     nro2 = float(input("Ingrese el segundo numero: "))

#     division = nro1 / nro2

# except ZeroDivisionError:
#     print("Error, no se puede dividir por '0'")
# except ValueError:
#     print("Error, el valor no es valido") #tira error al ingresar un caracter en cualquiera de los ingresados
# else:
#     print(f"EL resultado de la division es: {division:.2f}")