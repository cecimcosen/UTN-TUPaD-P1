# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

tope = 100
suma = 0

for i in range(0,tope): 
    num = int(input("Ingrese un número:"))

    suma = suma + num

media = suma/tope

print ("La media de los valores ingresados es: " , media )