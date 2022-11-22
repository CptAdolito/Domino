
#Este script contiene todas las funciones necesarias para ejecutar una partida
#Desde crear una ronda con los jugadores y puntos solicitados
#Hasta manejar los turnos, puntos, y ganadores
import fichaV2 as Ficha
import random
import imprimirTableroSencillo as imprimirTablero
import menu
import os
import menu

screenWidth = menu.screenWidth

def limpiar_pantalla():
    #Función para limpiar la pantalla. Usada continuamente en todo el programa
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def getFichasExtremos(fichas):
    #Devuelve las ficha que están en los extremos
    #Obtenemos la primera y la última ficha recorriendo la lista doblemente enlazada que es el tablero
    primeraFicha = fichas
    ultimaFicha = fichas
    while primeraFicha.conex2 != None:
        primeraFicha = primeraFicha.conex2
    while ultimaFicha.conex1 != None:
        ultimaFicha = ultimaFicha.conex1
    return primeraFicha, ultimaFicha

def crearRonda(nJugadores):
    #Creamos las fichas
    pozo = crearFichas()
    #Damos siete fichas a cada jugador
    jugadores = []
    for i in range(nJugadores):
        jugadores.append([])
        for j in range(7):
            f, pozo = sacarFichaDePozo(pozo)
            jugadores[i].append(f)

    #Creamos el orden de juego, aleatorio
    orden = []
    for i in range(nJugadores):
        orden.append(i)
    random.shuffle(orden)

    return jugadores, orden, pozo

def crearFichas():
    #Comenzamos estableciendo una función para crear todas las fichas.
    #Este algoritmo crea las 28 combinaciones de fichas únicas
    fichas = []
    for i in range(7):
        for j in range(7-i):
            fichas.append([i, 6-j])

    #Las barajeamos aletoriamente
    random.shuffle(fichas)
    #Creamos las fichas y las metemos en el pozo
    #El pozo es una lista enlazada
    pozo = Ficha.ficha(fichas[0][0], fichas[0][1])
    for i in range(27):
        nueva = Ficha.ficha(fichas[i+1][0], fichas[i+1][1])
        pozo.conex1 = nueva
        nueva.conex2 = pozo
        pozo = nueva
    
    return pozo

def lenPozo(pozo):
    #Devuelve el número de fichas en el pozo, que es una lista enlazada
    #Para ello la recorremos desde el inicio hasta llegar al final
    nPozo = 0
    f = pozo
    while f != None:
        nPozo += 1
        f = f.conex2
    return nPozo

def sacarFichaDePozo(pozo):
    #Sacamos una ficha del pozo y la devolvemos
    #Usado paar meter fichas del pozo a los jugadores
    #Se extrae la primera ficha, se eliminan sus conexiones y estableces la siguiente como la primera, y se borra su conexión tambien
    if pozo != None:
        n =lenPozo(pozo)
        if n == 1:
            #Es la ultima fichas, el pozo ahora queda vacío
            ficha = pozo
            pozo = None
        else:
            ficha = pozo
            pozo = pozo.conex2
            pozo.conex1 = None
            ficha.conex2 = None
    else:
        ficha = None
    return ficha, pozo

def imprimirEstadoPartida(jugadoes, pozo, orden, fichas, ronda, puntosNecesarios, puntos, numerosDisponibles, color):
    #Esta función imprime el estado de la partida en cada ronda.
    #Se imprime el tablero, el jugador actual con sus puntos y fichas y una tabla de puntos con los jugadores restantes
    #Imprimimos el estado de la partida
    print()
    print(f"RONDA {ronda} - {puntosNecesarios} PUNTOS NECESARIOS PARA GANAR".center(screenWidth))
    print()
    #Obtenemos el tablero
    tablero = imprimirTablero.imprimirTablero(fichas)
    #Imprimimos el tablero
    for i in tablero:
        print(i)
    print("")
    #Imprimimos el estado del jugador actual
    print(f"Jugador {orden[0]+1}: {puntos[orden[0]]} Puntos".center(screenWidth))

    #Imprimimos las fichas del jugador
    #Para ello obtengo la impresión de todas sus fichas y las uno en una sola línea
    fichasJugador = list()
    for i in range(len(jugadoes[orden[0]])):
        fichasJugador.append(jugadoes[orden[0]][i].imprimir())

    #Guardamos que fichas se pueden colocar 
    fichasValidas = list()
    for i in range(len(jugadoes[orden[0]])):
        if jugadoes[orden[0]][i].v1 in numerosDisponibles or jugadoes[orden[0]][i].v2 in numerosDisponibles:
            fichasValidas.append(i)

    #Imprimimos los números correspondientes a cada ficha
    if not color:
        #Si no estamos en modo color simplemente añadimos los números bien centrados
        for i in range(len(fichasJugador)):
            fichasJugador[i] = list(fichasJugador[i])
            if i<10: #Los números de dos cifras ocupan un caracter más, restamos un espacio anterior para que quede centrado
                fichasJugador[i].append("  "+str(i+1)+"  ")
            else:
                fichasJugador[i].append(" "+str(i+1)+"  ")
        #Uno todas las filas de mi matriz parahacerla un vector de lineas de texto, fácil de imprimir.
        #Además, las centramos a la vezque las unimos
        fichasJugador = [str(" ".join(i)).center(screenWidth) for i in zip(*fichasJugador)]

    else:
        #En el modo color pinto los números de verde si se pueden colocar y de rojo si no
        for i in range(len(fichasJugador)):
            fichasJugador[i] = list(fichasJugador[i])
            coloreado = menu.colored(0,255,0,str(i+1))  if i in fichasValidas else menu.colored(255,0,0,str(i+1))
            if i<10:
                fichasJugador[i].append("  "+ coloreado +"  ")
            else:
                fichasJugador[i].append(" "+ coloreado +"  ")
        #Las unimos, esta vez no las centramos aún
        fichasJugador = [str(" ".join(i)) for i in zip(*fichasJugador)]

        #Centramos las lineas, esta vez por separado porque la ultima fila se centra distinta
        for i in range(len(fichasJugador)-1):
            fichasJugador[i] = fichasJugador[i].center(screenWidth)
        #Para centrar la fila coloreada hay que tener en cuenta que la forma en la que se colorea es añadiendo caracteres "invisibles", 34 por color en este caso
        #(Mejor explicado en el código de menu.py)
        fichasJugador[len(fichasJugador)-1] = fichasJugador[len(fichasJugador)-1].center(screenWidth+34*(len(jugadoes[orden[0]])))

    #Imprimimos las fichas del jugador
    for i in fichasJugador:
        print(i)

    #Imprimimos los datos restantes, es decir, una tabla con los otros jugadores y sus puntos y fichas restantes
    print("")
    print("           PIEZAS PUNTOS".center(screenWidth))
    for i in range(len(jugadoes)-1):
        #Los campos que superan la decena ocupan 1 caracter más, hay que tener cuidado para centrarlos correctamente
        linea1 = "    " + str(len(jugadoes[orden[i+1]])) if len(jugadoes[orden[i+1]])<10 else "   " + str(len(jugadoes[orden[i+1]]))
        linea2 = "      " + str(puntos[orden[i+1]]) if puntos[orden[i+1]]<10 else "     " + str(puntos[orden[i+1]])
        print(f"JUGADOR {orden[i+1]+1}:{linea1}{linea2}  ".center(screenWidth))
    print()
    #Conseguimos las fichas que quedan en el pozo y lo imprimimos
    nPozo = lenPozo(pozo)
    print(f"Pozo: {nPozo} piezas".center(screenWidth))
    print()

def ejecutarRonda(njuagdoes, ronda, puntosNecesarios, puntos, color):
    #Comenzamos repartiendo fichas y turnos
    ok = False
    while not ok: #El bucle es solo necesario en el muy improbable caso de que no se haya repartido ninguna doble. En ese caso se vuelve a repartir
        jugadores, orden, pozo = crearRonda(njuagdoes)
        #Comenzamos la ronda, el jugador que tenga la ficha con el doble más alto coloca ficha
        fichas = None
        inicial = 0
        #Buscamos quén y dónde tiene la doble más alta
        for i in range(len(jugadores)):
            for j in range(len(jugadores[i])):
                if jugadores[i][j].v1 == jugadores[i][j].v2:
                    ok = True
                    if fichas != None:
                        if jugadores[i][j].v1 > jugadores[inicial][fichas].v1:
                            fichas = j
                            inicial = i
                    else:
                        fichas = j
                        inicial = i
    #Esta ficha será la inicial de la ronda y su jugador será el que empiece
    fichas = jugadores[inicial].pop(fichas)

    limpiar_pantalla()
    print()
    input(f"ABRE LA MESA EL JUGADOR {str(inicial+1)}".center(screenWidth))
    #Establezco a este como inicial, que acaba de jugar así que se va al ultimo lugar
    orden.append(orden.pop(orden.index(inicial))) #Esta líne se repite varias veces más. Sirve para rotar el turno

    #Jugamos la ronda
    vecesSaltado = 0
    fin = False
    while not fin:
        #Imprimimos el turno
        #Puede no parecer útil ya que continuamente se ve quén es el siguiente, pero sirve para ocultar la pantalla mientras cambian sitios
        #Así, ningún jugador puede ver las fichas del resto de los jugadores
        limpiar_pantalla()
        print( "╔═══════════════════╗".center(screenWidth))
        print(f"║TURNO DEL JUGADOR {str(orden[0]+1)}║".center(screenWidth))
        input( "╚═══════════════════╝".center(screenWidth)) #Siempre que tenemos un input es para que el jugador pueda leer lo que está sucediendo, sin que se limpie rápidamente
        limpiar_pantalla()
        #Comprobamos que el jugador puede jugar
        primera, ultima = getFichasExtremos(fichas)
        numerosDisponibles = [primera.v1, ultima.v2]
        puede = False
        for i in jugadores[orden[0]]:
            if i.v1 in numerosDisponibles or i.v2 in numerosDisponibles:
                puede = True
        
        #Si puede seguimos jugando, si no vamos al pozo
        if puede:
            ok = False
            vecesSaltado = 0
        else:
            #COMPROBAR POZO, si hay fichas coges una
            nPozo = lenPozo(pozo)
            if nPozo > 0:
                #Imprimimos el estado de la partida
                imprimirEstadoPartida(jugadores, pozo, orden, fichas, ronda, puntosNecesarios, puntos, numerosDisponibles, color)
                #Sacamos una ficha del pozo
                print("\n")
                #No se puede elegir ficha, solo sacar una del pozo
                input(f"Jugador {orden[0]+1} debe robar una pieza del pozo. (ENTER)".center(screenWidth))
                f, pozo = sacarFichaDePozo(pozo)
                jugadores[orden[0]].append(f)
                #Hacemos que la proxima ronda sea de este jugador también
                for i in range(njuagdoes-1):
                    orden.append(orden.pop(0))
            else:
                #Si no hay se salta el turno
                print()
                print( "╔══════════════════════════════════════════════════════════════╗".center(screenWidth))
                print(f"║SE SALTA EL TURNO DEL JUGADOR {str(orden[0]+1)} PORQUE NO PUEDE COLOCAR FICHAS║".center(screenWidth))
                input( "╚══════════════════════════════════════════════════════════════╝".center(screenWidth))
                vecesSaltado += 1 #Si el contador llegase al número de jugadores, se acabaría la partida porque nadie puede colocarar fichas, un caso raro pero posible
            ok = True
            
        while not ok:
            limpiar_pantalla()
            #Imprimimos el estado de la partida
            imprimirEstadoPartida(jugadores, pozo, orden, fichas, ronda, puntosNecesarios, puntos, numerosDisponibles, color)
            #Obtenemos la ficha que el jugador va a colocar
            print("\n")
            print(f"Jugador {orden[0]+1} ¿Qué ficha quieres colocar? (1-{len(jugadores[orden[0]])}):".center(screenWidth))
            entrada = (screenWidth//2-6)*" " + "=> "
            entrada = input(entrada)

            #Se limpia la entarada y se repite hasta que sea válida.
            if entrada.isdigit() and int(entrada) > 0 and int(entrada) <= len(jugadores[orden[0]]):
                if jugadores[orden[0]][int(entrada)-1].v1 in numerosDisponibles or jugadores[orden[0]][int(entrada)-1].v2 in numerosDisponibles: #Si la ficha está disponible para colocar
                    
                    #Hay que enlazar la ficha en su posición en la lista enlazada
                    fichaNueva = jugadores[orden[0]].pop(int(entrada)-1)
                    #Comprobamos si debe ser horizontal o vertical
                    if fichaNueva.v1 != fichaNueva.v2:
                        fichaNueva.pos = 1
                    #Comprobamos si la ficha es la primera o la ultima
                    primera, ultima = getFichasExtremos(fichas)
                    if primera.v1 == fichaNueva.v2 or primera.v1 == fichaNueva.v1:
                        #La ficha es la primera, va a la izquieda
                        if primera.v1 == fichaNueva.v1:
                            #Hay que cambiar el orden
                            auxiliar = fichaNueva.v2
                            fichaNueva.v2 = fichaNueva.v1
                            fichaNueva.v1 = auxiliar
                        #Las conectamos
                        fichaNueva.conex1 = primera
                        primera.conex2 = fichaNueva
                    
                    else:
                        #La ficha es la ultima, va a la derecha
                        if ultima.v2 == fichaNueva.v2:
                            #Hay que cambiar el orden
                            auxiliar = fichaNueva.v2
                            fichaNueva.v2 = fichaNueva.v1
                            fichaNueva.v1 = auxiliar
                        #Las conectamos
                        fichaNueva.conex2 = ultima
                        ultima.conex1 = fichaNueva
                    ok = True
        
        #Comprobamos si el jugador ha ganado la ronda
        #Ganador por cierre
        if vecesSaltado == len(jugadores):
            ganador = orden[0]
            for i in orden:
                if len(jugadores[i]) > len(jugadores[ganador]):
                    ganador = i
            fin = True

        #Ganador por dominó
        if len(jugadores[orden[0]]) == 0:
            ganador = orden[0]
            fin = True

        #Cambiamos de turno
        orden.append(orden.pop(0))

    #Cerramos la partida
    limpiar_pantalla()
    print()
    print("RONDA FINALIZADA".center(screenWidth))
    
    #Se cuentan los puntos del ganador y se anuncian
    puntos = 0
    for i in range(len(jugadores)):
        if i != ganador:
            for j in jugadores[i]:
                puntos += j.v1 + j.v2
    input(f"El jugador {ganador+1} ha ganado la ronda con {puntos} puntos".center(screenWidth))
    limpiar_pantalla()
    return ganador, puntos

def ejecutarPartida(nJugadores, puntosNecesarios, color):
    #Creamos lista de puntos
    puntos = list()
    for i in range(nJugadores):
        puntos.append(0)
    #Comenzamos la partida
    #Se juega hasta que algún jugadore llegue a los puntos necesarios
    fin = False
    ronda = 1
    while not fin:
        #Jugamos la ronda
        ganadorRonda, puntosGanadorRonda = ejecutarRonda(nJugadores, ronda, puntosNecesarios, puntos, color)
        #Actualizamos los puntos
        puntos[ganadorRonda] += puntosGanadorRonda
        #Comprobamos si algún jugador ha ganado  
        for i in range(nJugadores):
            if puntos[i] >= puntosNecesarios:
                ganador = i
                fin = True
        ronda += 1
    return ganador
