# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla 
# el factorial de todos los números enteros entre 1 y el número que indique el usuario

# Definición de funciones

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        return resultado


# Programa princial

n = int(input("Ingrese un número: "))

print(factorial_iterativo(n))
