# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definición de funciones

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal

celsius = float(input("Ingrese la temperatura en grados °C: "))

print(f"La temperatura en grados Fahrenhit es: {celsius_a_fahrenheit(celsius)}")