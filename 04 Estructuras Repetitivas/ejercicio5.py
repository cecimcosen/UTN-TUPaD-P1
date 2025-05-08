# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random

contador = 0
num = 0
numero_aleatorio = random.randint(0, 9)  # Genera un número entre 0 y 9, ambos incluidos

while num != numero_aleatorio:
    num = int(input("Elegí un número comprendido entre 0 y 9: "))
    contador = contador + 1

print("Necesitaste" , contador , "intentos para adivinarlo")
