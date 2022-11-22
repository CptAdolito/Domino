
#Script principal del programa.
#Para jugar ejecuta este script
import gameHandler
import menu
import sys

if __name__ == "__main__":
    modo = 0
    salir = False
    color = False
    #Primero obtenemos si se va a jugar con o sin color
    #El color afecta al menú y se indica en verde las fichas que se pueden colocar y en rojo las que no
    #Esto sirve para facilitar la identificación de las fichas que se pueden colocar ya que, al usar números en vez de puntos, no se ve tan rápido
    print()
    print("Escribe COLOR si quieres jugar con GRÁFICOS A COLOR.                 ".center(menu.screenWidth))
    print("Escribe cualquier otra cosa si deseas jugar en modo BLANCO Y NEGRO   ".center(menu.screenWidth))
    print("El modo a COLOR puede NO FUNCIONAR CORRECTAMENTE en todos los equipos".center(menu.screenWidth))
    entrada = (menu.screenWidth//2-6)*" " + "=> "
    entrada = input(entrada)
    #Limpiamos la entrada para que se pueda escribir en mayúsculas o minúsculas y con espacio al final
    entrada = entrada.upper()
    entrada = entrada.split(" ")
    if entrada[0] == "COLOR":
        color = True
    while not salir:
        while modo == 0: #Si la entrada no es válida se vuelve a preguntar
            gameHandler.limpiar_pantalla()
            modo = menu.menuInicial(color)
        #-------------#
        #----SALIR----#
        #-------------#
        if modo == 2:
            salir = True

        #-------------#
        #----JUGAR----#
        #-------------#
        elif modo == 1:
            ganador = None
            #Obtengo el numero de jugadores
            gameHandler.limpiar_pantalla()
            nJugadores = menu.NumeroJugadores()
            #Obtengo el nùmero de puntos
            gameHandler.limpiar_pantalla()
            puntos = menu.CantidadPuntos()
            #Ejecuto la partida
            gameHandler.limpiar_pantalla()
            ganador = gameHandler.ejecutarPartida(nJugadores, puntos, color)
            #Anuncio el ganador
            gameHandler.limpiar_pantalla()
            menu.PantallaFinal(ganador)
            gameHandler.limpiar_pantalla()
            #Vuelvo al menú principal
            modo = 0
    #Apagamos el programa
    sys.exit(0)
