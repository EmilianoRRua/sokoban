import msvcrt

# Definimos los niveles
niveles = [
    [
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 3, 3, 3, 3, 3, 3, 1,
        1, 3, 3, 3, 0, 3, 3, 1,
        1, 3, 3, 3, 3, 3, 3, 1,
        1, 3, 3, 3, 3, 3, 3, 1,
        1, 5, 3, 3, 3, 2, 3, 1,
        1, 3, 3, 3, 3, 3, 3, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
    ],
    [
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 3, 3, 3, 3, 1, 5, 1,
        1, 3, 3, 3, 3, 1, 5, 1,
        1, 3, 2, 1, 3, 1, 3, 1,
        1, 3, 3, 1, 3, 1, 3, 1,
        1, 3, 2, 3, 3, 3, 3, 1,
        1, 0, 3, 1, 3, 3, 3, 1,
        1, 1, 1, 1, 1, 1, 1, 1,   
    ],    
        [
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 3, 3, 3, 3, 3, 0, 1,
        1, 3, 2, 2, 3, 3, 3, 1,
        1, 3, 3, 1, 1, 3, 1, 1,
        1, 3, 3, 3, 3, 3, 3, 1,
        1, 1, 1, 1, 1, 3, 3, 1,
        1, 5, 3, 3, 3, 3, 3, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
    ],
    [
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 3, 3, 3, 3, 3, 3, 1,
        1, 3, 2, 2, 3, 2, 3, 1,
        1, 3, 3, 3, 3, 3, 3, 1,
        1, 3, 1, 1, 3, 3, 3, 1,
        1, 5, 5, 3, 3, 2, 3, 1,
        1, 5, 1, 1, 3, 0, 3, 1,
        1, 1, 1, 1, 1, 1, 1, 1,   
    ],
]

# Inicializamos el nivel actual
nivel_actual = 0
mapa_inicial = niveles[nivel_actual]

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

movimientos = []

def mover_jugador(direccion):
    global posicion_jugador
    if direccion == b'w':  # Arriba
        nueva_posicion = posicion_jugador - columnas
    elif direccion == b's':  # Abajo
        nueva_posicion = posicion_jugador + columnas
    elif direccion == b'a':  # Izquierda
        nueva_posicion = posicion_jugador - 1
    elif direccion == b'd':  # Derecha
        nueva_posicion = posicion_jugador + 1
    movimientos.append(mapa[:])
    if mapa[nueva_posicion] in [3, 5]:  # Si el jugador se moverá a un espacio vacío o a una meta
        if mapa[posicion_jugador] == 7:  # Si el jugador está sobre la meta
            mapa[posicion_jugador] = 5  # Deja la meta
        else:
            mapa[posicion_jugador] = 3  # Deja un espacio vacío
        if mapa[nueva_posicion] == 5:  # Si el jugador se moverá a la meta
            mapa[nueva_posicion] = 7  # Coloca al jugador sobre la meta
        else:
            mapa[nueva_posicion] = 0  # Coloca al jugador en un espacio vacío
        posicion_jugador = nueva_posicion
    elif mapa[nueva_posicion] in [2, 6]:  # Si el jugador se moverá a una caja o a una caja sobre la meta
        if direccion == b'w':  # Arriba
            nueva_posicion_caja = nueva_posicion - columnas
        elif direccion == b's':  # Abajo
            nueva_posicion_caja = nueva_posicion + columnas
        elif direccion == b'a':  # Izquierda
            nueva_posicion_caja = nueva_posicion - 1
        elif direccion == b'd':  # Derecha
            nueva_posicion_caja = nueva_posicion + 1
        if mover_caja(nueva_posicion, nueva_posicion_caja):  # Si la caja puede ser movida
            if mapa[posicion_jugador] == 7:  # Si el jugador está sobre la meta
                mapa[posicion_jugador] = 5  # Deja la meta
            else:
                mapa[posicion_jugador] = 3  # Deja un espacio vacío
            if mapa[nueva_posicion] == 6:  # Si la caja está sobre la meta
                mapa[nueva_posicion] = 7  # Coloca al jugador sobre la meta
            else:
                mapa[nueva_posicion] = 0  # Mueve al jugador
            if mapa[nueva_posicion_caja] == 5:  # Si la caja se moverá a la meta
                mapa[nueva_posicion_caja] = 6  # Coloca la caja sobre la meta
            else:
                mapa[nueva_posicion_caja] = 2  # Mueve la caja
            posicion_jugador = nueva_posicion
        elif tecla == b'q':  # Habilidad especial
            if mapa[posicion_jugador] == 0:  # Si el jugador está en un espacio vacío
             mapa[posicion_jugador] = 7  # Coloca al jugador sobre una meta

def mover_caja(posicion_actual, nueva_posicion):
    if mapa[nueva_posicion] in [3, 5]:  # Si la nueva posición es un espacio vacío o una meta
        return True
    else:  # Si la nueva posición es una pared o otra caja
        return False

def fin_del_juego():
    global nivel_actual
    if 2 not in mapa:  # ¿No hay Metas?
        print("Fin del Juego")
        # Avanza al siguiente nivel
        nivel_actual += 1
        if nivel_actual < len(niveles):  # Si hay más niveles
            reiniciar_nivel()  # Inicia el siguiente nivel



def reiniciar_nivel():
    global mapa, posicion_jugador, posicion_caja, nivel_actual
    mapa = niveles[nivel_actual].copy()
    posicion_jugador = mapa.index(0)
    posicion_caja = mapa.index(2)
imprimir_mapa()



while True:
    tecla = msvcrt.getch()
    if tecla == b'r':
        reiniciar_nivel()
    elif tecla == b'q':  # Habilidad especial
        if mapa[posicion_jugador] in [0, 3]:  # Si el jugador está en un espacio vacío o sobre una meta
            mapa[posicion_jugador] = 7  # Transforma al jugador en jugador-meta
    elif tecla == b'z':  # Retrocede
        if movimientos:  # Si hay movimientos para retroceder
            # Restaura el estado completo del mapa al estado anterior
            mapa = movimientos.pop()
            # Actualiza la posición del jugador y de la caja
            posicion_jugador = mapa.index(0)
            posicion_caja = mapa.index(2)
    elif 2 not in mapa:  # ¿No hay Metas?
        fin_del_juego()  
    else:
        mover_jugador(tecla)
    imprimir_mapa()
