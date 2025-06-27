import time
# Diccionario de datos

partituras = {
    "Marcha en Re Mayor": "Bach",
    "Estudio N° 37": "Cramer",
    "Sonata en Mib menor": "Beethoven",
    "Fantasía Impromptu N°66": "Chopin",
    "Estudio N°10": "Chopin",
    "Siciliana": "Shumann",
    "San Nicolás": "Schumann",
    "Dos Scherzos": "Schubert",
    "Pequeña Canción": "Mozart"
}

# Definición de funciones

def mostrar_partituras():
    print("\nListado de partituras:\n")
    for titulo, compositor in partituras.items():
        print(f"Título: {titulo} - Compositor: {compositor}")

def buscar_por_titulo():
    busqueda = input("\nIngrese el título de la partitura a buscar: ")
    encontrado = False
    for titulo in partituras:
        if titulo.lower() == busqueda.lower():
            print(f"\nEncontrado: {titulo} - Compositor: {partituras[titulo]}")
            encontrado = True
            break
    if not encontrado:
        print("\nLa partitura no se encuentra en el listado.")

def buscar_por_compositor():
    busqueda = input("\nIngrese el nombre del compositor a buscar: ")
    encontrado = False
    print(f"\nObras de {busqueda.capitalize()}:")
    for titulo, compositor in partituras.items():
        if compositor.lower() == busqueda.lower():
            print(f"- {titulo}")
            encontrado = True
    if not encontrado:
        print("No se encontraron partituras de ese compositor.")

def buscar_binaria():
    lista_ordenada = sorted(partituras.items())
    titulos = [titulo for titulo, _ in lista_ordenada]
    busqueda = input("\nIngrese el título de la partitura a buscar (binaria): ")
    izquierda = 0
    derecha = len(titulos) - 1
    encontrado = False

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if titulos[medio].lower() == busqueda.lower():
            compositor = dict(lista_ordenada)[titulos[medio]]
            print(f"\nEncontrado: {titulos[medio]} - Compositor: {compositor}")
            encontrado = True
            break
        elif busqueda.lower() < titulos[medio].lower():
            derecha = medio - 1
        else:
            izquierda = medio + 1

    if not encontrado:
        print("\nLa partitura no se encuentra (búsqueda binaria).")

def ordenar_burbuja():
    lista = list(partituras.items())
    n = len(lista)
    inicio = time.perf_counter()
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][0].lower() > lista[j + 1][0].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    fin = time.perf_counter()

    print("\nPartituras ordenadas por título (burbuja):\n")
    for titulo, compositor in lista:
        print(f"Título: {titulo} - Compositor: {compositor}")
    print(f"\nTiempo de ordenamiento (burbuja): {fin - inicio:.6f} segundos")

def ordenar_seleccion():
    lista = list(partituras.items())
    n = len(lista)
    inicio = time.perf_counter()
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j][0].lower() < lista[min_index][0].lower():
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    fin = time.perf_counter()

    print("\nPartituras ordenadas por título (selección):\n")
    for titulo, compositor in lista:
        print(f"Título: {titulo} - Compositor: {compositor}")
    print(f"\nTiempo de ordenamiento (selección): {fin - inicio:.6f} segundos")

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[0].lower() < pivote[0].lower()]
        mayores = [x for x in lista[1:] if x[0].lower() >= pivote[0].lower()]
        return quicksort(menores) + [pivote] + quicksort(mayores)

def ordenar_quicksort():
    lista = list(partituras.items())
    inicio = time.perf_counter()
    ordenada = quicksort(lista)
    fin = time.perf_counter()

    print("\nPartituras ordenadas por título (quicksort):\n")
    for titulo, compositor in ordenada:
        print(f"Título: {titulo} - Compositor: {compositor}")
    print(f"\nTiempo de ordenamiento (quicksort): {fin - inicio:.6f} segundos")

def menu():
    while True:
        print("\n----- Obras disponibles -----")
        print("1. Mostrar todas las partituras")
        print("2. Buscar partitura por título (lineal)")
        print("3. Buscar partituras por compositor")
        print("4. Buscar partitura por título (binaria)")
        print("5. Ordenar por título (burbuja)")
        print("6. Ordenar por título (selección)")
        print("7. Ordenar por título (quicksort)")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_partituras()
        elif opcion == "2":
            buscar_por_titulo()
        elif opcion == "3":
            buscar_por_compositor()
        elif opcion == "4":
            buscar_binaria()
        elif opcion == "5":
            ordenar_burbuja()
        elif opcion == "6":
            ordenar_seleccion()
        elif opcion == "7":
            ordenar_quicksort()
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú

menu()


