# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

numero = 1
suma = 0

while numero != 0:
    print ("Ingrese un número entero:")
    numero = int(input())
    suma += numero

print ("La suma de todos los números ingresados es: " , suma)  