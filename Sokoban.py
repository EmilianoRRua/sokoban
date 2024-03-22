import msvcrt

mapa_inicial = [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 3, 3, 3, 3, 3, 3, 1,
    1, 3, 3, 3, 0, 3, 3, 1,
    1, 3, 3, 3, 3, 3, 3, 1,
    1, 3, 3, 3, 3, 3, 3, 1,
    1, 5, 3, 3, 3, 2, 3, 1,
    1, 3, 3, 3, 3, 3, 3, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
]

filas = 8
columnas = 8
posicion_jugador = mapa_inicial.index(0)  # Aqui Ubicamos al Jugador
posicion_caja = mapa_inicial.index(2)  # Aqui ubicamos la Caja
posicion_meta = mapa_inicial.index(5)  # Aqui ubicamos la Meta

mapa = mapa_inicial.copy()

def imprimir_mapa():
    for i in range(filas):
        for j in range(columnas):
            indice = i * columnas + j
            if mapa[indice] == 1:               # PAREDES
                print(" 🧱 ", end="")
            elif mapa[indice] == 2:             # CAJAS
                print(" ❄️. ", end="")
            elif mapa[indice] == 3:             # ESPACIOS
                print("    ", end="")
            elif mapa[indice] == 0:             # JUGADOR
                print(" 🐧 ", end="")
            elif mapa[indice] == 5:             # META
                print(" 💧 ", end="")
            elif mapa[indice] == 6:             # CAJA SOBRE META
                print(" 🧊 ", end="")
            elif mapa[indice] == 7:             # JUGADOR SOBRE META
                print(" 🐧 ", end="")
        print()

def mover_jugador(direccion):
    global posicion_jugador
    if direccion == b'w':  # Arriba
        nueva_posicion = posicion_jugador - columnas
        if mapa[nueva_posicion] == 3:
            mapa[posicion_jugador] = 3
            mapa[nueva_posicion] = 0
            posicion_jugador = nueva_posicion
        elif mapa[nueva_posicion] == 2:
            if mover_caja(nueva_posicion, nueva_posicion - columnas):
                mapa[posicion_jugador] = 3
                mapa[nueva_posicion] = 0
                mapa[nueva_posicion - columnas] = 2
                posicion_jugador = nueva_posicion
    elif direccion == b's':  # Abajo
        nueva_posicion = posicion_jugador + columnas
        if mapa[nueva_posicion] == 3:
            mapa[posicion_jugador] = 3
            mapa[nueva_posicion] = 0
            posicion_jugador = nueva_posicion
        elif mapa[nueva_posicion] == 2:
            if mover_caja(nueva_posicion, nueva_posicion + columnas):
                mapa[posicion_jugador] = 3
                mapa[nueva_posicion] = 0
                mapa[nueva_posicion + columnas] = 2
                posicion_jugador = nueva_posicion
    elif direccion == b'a':  # Izquierda
        nueva_posicion = posicion_jugador - 1
        if mapa[nueva_posicion] == 3:
            mapa[posicion_jugador] = 3
            mapa[nueva_posicion] = 0
            posicion_jugador = nueva_posicion
        elif mapa[nueva_posicion] == 2:
            if mover_caja(nueva_posicion, nueva_posicion - 1):
                mapa[posicion_jugador] = 3
                mapa[nueva_posicion] = 0
                mapa[nueva_posicion - 1] = 2
                posicion_jugador = nueva_posicion
    elif direccion == b'd':  # Derecha
        nueva_posicion = posicion_jugador + 1
        if mapa[nueva_posicion] == 3:
            mapa[posicion_jugador] = 3
            mapa[nueva_posicion] = 0
            posicion_jugador = nueva_posicion
        elif mapa[nueva_posicion] == 2:
            if mover_caja(nueva_posicion, nueva_posicion + 1):
                mapa[posicion_jugador] = 3
                mapa[nueva_posicion] = 0
                mapa[nueva_posicion + 1] = 2
                posicion_jugador = nueva_posicion

def mover_caja(posicion_actual, nueva_posicion):
    if mapa[nueva_posicion] == 3:
        return True
    return False

def reiniciar_nivel():
    global mapa, posicion_jugador, posicion_caja
    mapa = mapa_inicial.copy()
    posicion_jugador = mapa.index(0)
    posicion_caja = mapa.index(2)

imprimir_mapa()

while True:
    tecla = msvcrt.getch()
    if tecla == b'r':
        reiniciar_nivel()
    else:
        mover_jugador(tecla)
    imprimir_mapa()
