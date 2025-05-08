# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num_1 = int(input("Ingrese un número entero:"))
num_2 = int(input("Ingrese un número entero:"))

menor = min(num_1, num_2)
mayor = max(num_1, num_2)

sumatoria = 0

for cont in range(menor + 1, mayor):
    sumatoria += cont

print(f"La suma de los números entre {menor} y {mayor}, excluyéndolos, es: {sumatoria}")
