# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

# Se establece una constante que servirá para comparar

EDAD_MINIMA = 18

# Solicita la edad al usuario

edad = int(input("Ingrese su edad: "))

# Estructura de decisión que compara la edad ingresada por el usuario con la edad mínima para ser mayor de edad

if edad >= EDAD_MINIMA:
    print( "Es mayor de edad")


