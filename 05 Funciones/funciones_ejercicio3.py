# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de funciones

def informacion_personal(nombre, apellido, edad, residencia):
    return (nombre , apellido , edad , residencia)

# Programa principal

nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input("Ingresa tu edad:")
residencia = input("Ingresa tu residencia:")

print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")