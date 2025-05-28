# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con 
# el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara

# Definición de funciones

def operaciones_basicas(a , b ):
    return (a + b , a - b, a * b, a /b )
    
# Programa principal

a = int(input("Ingrese un número:"))
b = int(input("Ingrese un número:"))

print(f"El resultado de la suma, resta, multiplicación y división entre los números ingresados es respectivamente: {operaciones_basicas(a , b)}")