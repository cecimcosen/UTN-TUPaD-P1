# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

#  Solicita la edad al usuario

edad = int(input("Ingrese su edad: "))

# Clasifica según la edad

if edad < 12:
    print("Sos un/a niño/a.")
elif edad < 18:
    print("Sos un/a adolescente.")
elif edad < 30:
    print("Sos un/a adulto/a joven.")
else:
    print("Sos un adulto.")