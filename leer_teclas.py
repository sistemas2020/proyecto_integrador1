import readchar
def leer_tecla():
    tecla= readchar.readkey()
    return tecla


print("Presiona las teclas en tu teclado. Para salir, presiona la tecla ↑ (UP).")
while True:
    tecla_presionada = leer_tecla()
    print(f"Tecla presionada: {tecla_presionada}")

    if tecla_presionada == 'a':
        print("¡Tecla UP presionada! Saliendo del programa.")
        break