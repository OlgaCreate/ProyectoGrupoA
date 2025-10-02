def buscar_por_nombre(alumnos: list):
    """Busca y muestra alumnos por su nombre."""
    print("\n--- Buscar Alumno por Nombre ---")
    if not alumnos:
        print("No hay alumnos registrados para buscar.")
        return

    nombre_buscado = input("Ingresa el nombre a buscar: ").lower()
    resultados = []
    for alumno in alumnos:
        if nombre_buscado in alumno['nombre'].lower():
            resultados.append(alumno)
    
    if resultados:
        print("\nResultados encontrados:")
        for alumno in resultados:
            print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}")
    else:
        print("No se encontraron alumnos con ese nombre.")

def buscar_por_edad(alumnos: list):
    """Busca y muestra alumnos por su edad."""
    print("\n--- Buscar Alumno por Edad ---")
    if not alumnos:
        print("No hay alumnos registrados para buscar.")
        return

    try:
        edad_buscada = int(input("Ingresa la edad a buscar: "))
        resultados = []
        for alumno in alumnos:
            if alumno['edad'] == edad_buscada:
                resultados.append(alumno)

        if resultados:
            print("\nResultados encontrados:")
            for alumno in resultados:
                print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}")
        else:
            print("No se encontraron alumnos con esa edad.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número para la edad.")