"""Las líneas import os e import platform en Python importan dos módulos incorporados que permiten 
al programa interactuar con el sistema operativo y obtener información sobre él, respectivamente. 
os permite ejecutar operaciones del sistema, como crear carpetas o listar archivos, mientras que platform proporciona 
funciones para identificar el sistema operativo subyacente, como su nombre y arquitectura."""

import os
import platform

def validar_numero(valor: str) -> bool: #Funcion de tipo promesa vara detectar string y cambiarlas a boliano.
    """Verifica si una cadena de texto es un número entero válido."""
    return valor.isdigit()

def limpiar_pantalla():
    """Limpia la consola para una mejor visualización."""
    os_name = platform.system()
    if os_name == 'Windows': #Si el sistema es Windows borra con cls caso contrario con clear.
        os.system('cls')
    else:
        # Para macOS y Linux
        os.system('clear')