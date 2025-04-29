# Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Define la lista de números aleatorios, es decir, crea una lista de números con 50 números del 1-100 de forma aleatoria

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula los parámetros estadísticos difininendo una variable por cada parámetro

from statistics import mode, median, mean

MODA = mode (numeros_aleatorios)
MEDIANA = median (numeros_aleatorios)
MEDIA = mean (numeros_aleatorios)

# Estructura comparativa

if MEDIA > MEDIANA > MODA:
    print("Existe sesgo positivo") 
elif MEDIA < MEDIANA < MODA:
    print ("Existe sesgo negativo")
elif MEDIA == MEDIANA == MODA:
    print ("Sin sesgo")