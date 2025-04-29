# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, 
# primavera o verano.

hemisferio = input("Ingrese el hemisferio en el cual se encuentra (N/S): ")
mes = int(input("Ingrese el mes del año en el que se encuentra (1-12): "))
dia = int(input("Ingrese el día del mes en el que se encuentra(1-31): "))


if hemisferio.upper() == "N":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 23):
        estacion = "Verano"
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        estacion = "Otoño"
    else:
        estacion = "Invierno"

elif hemisferio.upper() == "S":
    if (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        estacion = "Primavera"
    elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        estacion = "Otoño"
    else:
        estacion = "Invierno"
else:
    estacion = "Hemisferio inválido"

print(f"Te encuentras en: {estacion}.")