# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definición de funciones

def calcular_imc(peso,altura):
    return peso / (altura**2)

# Programa principal

peso = float(input("Ingrese su peso en kg:"))
altura = float(input("Ingrese su altura en m:"))

print(f"Su IMC es: {calcular_imc(peso,altura):.2f}")