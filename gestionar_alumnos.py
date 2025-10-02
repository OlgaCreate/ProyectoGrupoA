import utilidades

#Mejoría se puede agregar más de 1 alumno
def agregar_alumno(alumnos: list):
    """Solicita los datos de un alumno y lo agrega a la lista."""
    
    alumnos_temporal = []
    
    while True:        
        print("\n--- Agregar Nuevo Alumno ---")
        nombre = input("Ingresa el nombre del alumno: ").strip()
        
        while True:
            edad_str = input("Ingresa la edad del alumno: ").strip()
            if utilidades.validar_numero(edad_str):
                edad = int(edad_str)
                break
            else:
                print("La edad debe ser un número entero. Intenta de nuevo.")

        nuevo_alumno = {
            'nombre': nombre.capitalize(),
            'edad': edad
        }
        
        alumnos.append(nuevo_alumno) #lista global
        alumnos_temporal.append(nuevo_alumno)
        
        opcion = input("Quieres agregar otro alumno? (s/n)").lower()
        if opcion == "n":
            break
        elif opcion == "s":
            continue
        else:
            print("Opción no válida.")
    for alumno in alumnos_temporal:
        print(alumno)
            

def ver_alumnos(alumnos: list):
    """Muestra la lista completa de alumnos."""
    print("\n--- Lista de Alumnos ---")
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        for alumno in alumnos:
            print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}") 

def eliminar_alumno(alumnos: list):
    """Elimina un alumno de la lista por su nombre."""
    print("\n--- Eliminar Alumno ---")
    if not alumnos:
        print("No hay alumnos para eliminar.")
        return

    nombre_a_eliminar = input("Ingresa el nombre del alumno a eliminar: ")
    alumno_encontrado = False
    alumnos_nuevos = []
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre_a_eliminar.lower():
            alumno_encontrado = True
            print(f"Alumno '{alumno['nombre']}' eliminado.")
        else:
            alumnos_nuevos.append(alumno)
    
    alumnos[:] = alumnos_nuevos
    
    if not alumno_encontrado:
        print("No se encontró un alumno con ese nombre.")
        
        
# nueva función para editar alumno
def editar_alumno(alumnos: list):
    """Busca y edita alumnos por su nombre."""
    
    print("\n--- Buscar Alumno por Nombre ---")
    if not alumnos:
        print("No hay alumnos registrados para buscar.")
        return

    nombre_buscado = input("Ingresa el nombre completo a buscar: ").lower()
    for alumno in alumnos:
        if nombre_buscado in alumno['nombre'].lower():
            nuevo_nombre = input("Escribe nuevo nombre del alumno: ")
            alumno["nombre"] = nuevo_nombre.title()
            print(f"El nombre ha sido modificado con éxito: {alumno}")
            return