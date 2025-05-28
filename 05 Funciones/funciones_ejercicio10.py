# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definición de funciones

def calcular_promedio (a, b , c):
    return (a + b + c)/3

# Programa principal

a = float(input("Ingrese un número:"))
b = float(input("Ingrese un número:"))
c = float(input("Ingrese un número:"))

print(f"El promedio de los números ingresados es: {calcular_promedio (a, b , c)}")