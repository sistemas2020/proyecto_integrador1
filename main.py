# Pedir el nombre del jugador por teclado
nombre_jugador = input("Por favor, introduce tu nombre: ")

print(f"Bienvenido, {nombre_jugador}!")
import os
import readchar
from typing import List, Tuple

def generar_laberinto(size: int) -> List[List[str]]:
    laberinto = [["#" if i % 2 == 0 and j % 2 == 0 else "." for j in range(size)] for i in range(size)]
    return laberinto

def mostrar_laberinto(laberinto: List[List[str]]) -> None:
    for fila in laberinto:
        print("".join(fila))

def limpiar_pantalla() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(laberinto: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]) -> None:
    px, py = inicio

    while (px, py) != final:
        limpiar_pantalla()
        laberinto[py][px] = "P"
        mostrar_laberinto(laberinto)
        laberinto[py][px] = "."

        tecla = readchar.readkey()

        if tecla == '\x1b[A' and py > 0 and laberinto[py - 1][px] != "#":
            py -= 1
        elif tecla == '\x1b[B' and py < len(laberinto) - 1 and laberinto[py + 1][px] != "#":
            py += 1
        elif tecla == '\x1b[D' and px > 0 and laberinto[py][px - 1] != "#":
            px -= 1
        elif tecla == '\x1b[C' and px < len(laberinto[0]) - 1 and laberinto[py][px + 1] != "#":
            px += 1

if __name__ == "__main__":
    size = 11
    laberinto = generar_laberinto(size)
    inicio = (0, 0)
    final = (size - 1, size - 1)

    main_loop(laberinto, inicio, final)
