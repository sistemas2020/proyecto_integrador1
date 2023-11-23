# Pedir el nombre del jugador por teclado
nombre_jugador = input("Por favor, introduce tu nombre: ")

print(f"Bienvenido, {nombre_jugador}!")
import os
from typing import List, Tuple

def generar_laberinto(size: int) -> List[List[str]]:
    # Función para generar un laberinto utilizando el generador de la página proporcionada
    # El laberinto se representa como una matriz de caracteres
    # Utiliza # para las paredes y . para los caminos
    laberinto = [["#" if i % 2 == 0 and j % 2 == 0 else "." for j in range(size)] for i in range(size)]
    return laberinto

def mostrar_laberinto(laberinto: List[List[str]]) -> None:
    # Función para mostrar el laberinto en la pantalla
    for fila in laberinto:
        print("".join(fila))

def limpiar_pantalla() -> None:
    # Función para limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(laberinto: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]) -> None:
    # Función principal que maneja el bucle del juego
    px, py = inicio

    while (px, py) != final:
        limpiar_pantalla()
        laberinto[py][px] = "P"
        mostrar_laberinto(laberinto)
        laberinto[py][px] = "."

        tecla = input("Presiona una tecla de flecha (↑ ↓ ← →) para mover al jugador: ")

        if tecla == '↑' and py > 0 and laberinto[py - 1][px] != "#":
            py -= 1
        elif tecla == '↓' and py < len(laberinto) - 1 and laberinto[py + 1][px] != "#":
            py += 1
        elif tecla == '←' and px > 0 and laberinto[py][px - 1] != "#":
            px -= 1
        elif tecla == '→' and px < len(laberinto[0]) - 1 and laberinto[py][px + 1] != "#":
            px += 1

if __name__ == "__main__":
    # Configuración del tamaño del laberinto
    size = 11
    # Generar laberinto
    laberinto = generar_laberinto(size)
    # Coordenadas de inicio y final
    inicio = (0, 0)
    final = (size - 1, size - 1)

    # Ejecutar el bucle principal
    main_loop(laberinto, inicio, final)
