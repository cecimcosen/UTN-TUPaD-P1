#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
nombre_mayusculas = nombre.upper()
nombre_minusculas = nombre.lower()
nombre_primera_mayus = nombre.title()

print ("Elija una opción: ")
print ("1. Si quiere su nombre en mayusculas")
print ("2. Si quiere su nombre en minúsculas")
print ("3. Si quiere su nombre con la primera letra mayúscula")

opcion = int(input("Tu elección: "))

if opcion == 1:
    print(nombre_mayusculas)
elif opcion == 2:
    print (nombre_minusculas)
else:
    print (nombre_primera_mayus)


