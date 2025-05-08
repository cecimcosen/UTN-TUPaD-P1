# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un número entero positivo:"))

sumatoria = 0

for cont in range(0,num +1):
    sumatoria += cont

print(f"La suma de los números entre 0 y {num} es: {sumatoria}")