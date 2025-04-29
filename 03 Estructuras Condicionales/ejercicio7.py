# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación 
# al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla

texto = input("Ingresa una frase o palabra: ")

ultima_letra = texto[-1].lower()

if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o' or ultima_letra == 'u':
    texto = texto + '!'

print(texto)
