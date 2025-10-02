import gestionar_alumnos
import buscar_alumnos
import utilidades

# Mejoría (Se puede agregar más de un alumno. Editar alumnos.)
def mostrar_menu():
    """Muestra las opciones del menú principal."""
    utilidades.limpiar_pantalla()
    print("--- Sistema de Gestión de Alumnos ---")
    print("1. 👩‍🎓 Agregar un nuevo alumno")
    print("2. Ver todos los alumnos")
    print("3. Buscar alumno por nombre")
    print("4. Buscar alumno por edad")
    print("5. Eliminar alumno")
    print("6. Editar alumno")
    print("0. Salir")
    print("-------------------------------------")

# Función principal
def main():
    """Función principal del programa."""
    alumnos = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            gestionar_alumnos.agregar_alumno(alumnos)
        elif opcion == '2':
            gestionar_alumnos.ver_alumnos(alumnos)
        elif opcion == '3':
            buscar_alumnos.buscar_por_nombre(alumnos)
        elif opcion == '4':
            buscar_alumnos.buscar_por_edad(alumnos)
        elif opcion == '5':
            gestionar_alumnos.eliminar_alumno(alumnos)
        elif opcion == "6":
            gestionar_alumnos.editar_alumno(alumnos)
        elif opcion == '0':
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()