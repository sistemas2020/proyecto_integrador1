# Pedir el nombre del jugador por teclado
nombre_jugador = input("Por favor, introduce tu nombre: ")

print(f"Bienvenido, {nombre_jugador}!")
import readchar
# Bucle infinito
while True:
    # Lee un carácter desde la entrada
    tecla = readchar.readkey()

    # Imprime el carácter leído
    print(f"Tecla presionada: {tecla}")

    # Comprueba si la tecla presionada es la tecla de flecha arriba ("↑")
    if tecla == '↑':
        print("Se presionó la tecla de flecha arriba. Saliendo del bucle.")
        break
