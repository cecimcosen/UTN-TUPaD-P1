# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definición de funciones

def segundos_a_horas(segundos):
    return (segundos / 3600)

# Programa principal

segundos = float(input("Ingrese la cantidad de segundos:"))

print(f"La cantidad de horas es: {segundos_a_horas(segundos)}")

