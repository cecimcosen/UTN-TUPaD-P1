# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

# Defino la función

def funcion_fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return funcion_fibonacci(posicion - 1) + funcion_fibonacci(posicion - 2) 

posicion = int(input("Ingrese una posición:"))    

# Programa principal

for i in range(posicion + 1):
    print(f"En la posición {i} obtenemos el valor fibonacci: {funcion_fibonacci(i)}")