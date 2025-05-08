# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).



contador = 0
num_pares = 0
num_impares = 0
num_negativo_impar = 0
num_negativo_par = 0
num_positivo_impar = 0
num_positivo_par = 0

while contador <= 100:
    num = int(input("Ingresa un número entero:"))
    contador = contador + 1
    if num % 2 == 0:
        num_pares = num_pares + 1 
        if num >= 0:
            num_positivo_par = num_positivo_par + 1
        else:
            num_negativo_par = num_negativo_par + 1

    else:
        num_impares = num_impares + 1
        if num >= 0:
            num_positivo_impar = num_positivo_impar + 1
        else:
            num_negativo_impar = num_negativo_impar + 1

print ("El total de números pares es: " , num_pares )
print ("El total de números impares es: " , num_impares )
print ("El total de números positivos es: " , (num_positivo_par + num_positivo_impar) )
print ("El total de números negativos es: " , (num_negativo_par + num_negativo_impar ))