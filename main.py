from typing import List, Tuple
import os
import random
from functools import reduce

class Juego:
    def __init__(self, size: int):
        self.size = size

    def generar_laberinto(self) -> List[List[str]]:
        laberinto = [["#" if i % 2 == 0 and j % 2 == 0 else "." for j in range(self.size)] for i in range(self.size)]
        return laberinto

    def mostrar_laberinto(self, laberinto: List[List[str]]) -> None:
        for fila in laberinto:
            print("".join(fila))

    def limpiar_pantalla(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_loop(self, laberinto: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]) -> None:
        px, py = inicio

        while (px, py) != final:
            self.limpiar_pantalla()
            laberinto[py][px] = "P"
            self.mostrar_laberinto(laberinto)
            laberinto[py][px] = "."

            tecla = input("Presiona una tecla para continuar...")

            if tecla == '\x1b[A' and py > 0 and laberinto[py - 1][px] != "#":
                py -= 1
            elif tecla == '\x1b[B' and py < len(laberinto) - 1 and laberinto[py + 1][px] != "#":
                py += 1
            elif tecla == '\x1b[D' and px > 0 and laberinto[py][px - 1] != "#":
                px -= 1
            elif tecla == '\x1b[C' and px < len(laberinto[0]) - 1 and laberinto[py][px + 1] != "#":
                px += 1

class JuegoArchivo(Juego):
    def __init__(self, carpeta_mapas: str):
        self.carpeta_mapas = carpeta_mapas
        mapa, inicio, final = self.leer_mapa_desde_archivo()
        super().__init__(size=len(mapa))
        self.laberinto = mapa
        self.inicio = inicio
        self.final = final

    def leer_mapa_desde_archivo(self) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
        archivos_mapas = os.listdir(self.carpeta_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = os.path.join(self.carpeta_mapas, nombre_archivo)

        with open(path_completo, "r") as file:
            dimensiones_inicio_fin = map(int, file.readline().split())
            filas, columnas, inicio_x, inicio_y = dimensiones_inicio_fin

            contenido_mapa = reduce(lambda x, y: x + y, file.readlines()).strip()

        if columnas > 0:
            mapa = list(map(list, map(str.strip, contenido_mapa.split('\n'))))
            inicio = (inicio_x, inicio_y)
            final = (columnas - 1, filas - 1)
            return mapa, inicio, final
        else:
            raise ValueError("El número de columnas debe ser mayor que cero.")

def main():
    size = 11
    juego = Juego(size)
    laberinto = juego.generar_laberinto()
    inicio = (0, 0)
    final = (size - 1, size - 1)

    juego.main_loop(laberinto, inicio, final)

if __name__ == "__main__":
    main()


