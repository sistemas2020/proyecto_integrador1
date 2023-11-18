import os
import readchar

def clear_terminal():
    """
    Borra la terminal según el sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_numero(numero):
    """
    Imprime el número en la terminal.
    """
    print(f"Número: {numero}")

if __name__ == "__main__":
    numero = 0

    while numero <= 50:
        clear_terminal()
        imprimir_numero(numero)
        tecla = readchar.readchar()  # Utiliza readchar para leer una tecla

        if tecla.lower() == 'n':  # La tecla se representa como un objeto de bytes
            numero += 1
        else:
            break

