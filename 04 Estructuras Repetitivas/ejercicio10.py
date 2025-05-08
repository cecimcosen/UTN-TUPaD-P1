# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingresa un número: "))
invertido = 0

while (numero > 0):
  ultimo_digito = numero % 10
  invertido = (invertido * 10) + ultimo_digito
  numero = int(numero / 10)

print(invertido)