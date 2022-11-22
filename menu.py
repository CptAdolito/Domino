
#Variable global para cambiar el ancho de la pantalla
#Sirve para que se centren correctamente todos los textos, menús, etc.
#Con el valor de 261 se centra bien en la consola de visual studio code
global screenWidth
screenWidth = 261

def colored(r, g, b, string):
    #Esta función te devuelve un string formateado con el color que quieras
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, string)

def imprimirMenu():                                                                                                      
    print("DDDDDDDDDDDDD             OOOOOOOOO     MMMMMMMM               MMMMMMMMIIIIIIIIIINNNNNNNN        NNNNNNNN     OOOOOOOOO                             ,,``──╓,         ".center(screenWidth))
    print("D::::::::::::DDD        OO:::::::::OO   M:::::::M             M:::::::MI::::::::IN:::::::N       N::::::N   OO:::::::::OO                        `░███▄░░░░░░░░░▒▒H─~".center(screenWidth))
    print("D:::::::::::::::DD    OO:::::::::::::OO M::::::::M           M::::::::MI::::::::IN::::::::N      N::::::N OO:::::::::::::OO                    ╓░░░░░░░░░░░░░████░▒▒▓".center(screenWidth))
    print("DDD:::::DDDDD:::::D  O:::::::OOO:::::::OM:::::::::M         M:::::::::MII::::::IIN:::::::::N     N::::::NO:::::::OOO:::::::O                  ¿░░░░░░╓▄██µ░░░▀▀▀░▒▒▓▓".center(screenWidth))
    print("  D:::::D    D:::::D O::::::O   O::::::OM::::::::::M       M::::::::::M  I::::I  N::::::::::N    N::::::NO::::::O   O::::::O                 ░,▄▄,░░░▀██▀░░░░░░░▒,╢▓▌".center(screenWidth))
    print("  D:::::D     D:::::DO:::::O     O:::::OM:::::::::::M     M:::::::::::M  I::::I  N:::::::::::N   N::::::NO:::::O     O:::::O               ╓░░███▀░░░░░░░░░░░░░▒╓╫█▀ ".center(screenWidth))
    print("  D:::::D     D:::::DO:::::O     O:::::OM:::::::M::::M   M::::M:::::::M  I::::I  N:::::::N::::N  N::::::NO:::::O     O:::::O              ∩░,░░░░░░░░░░░████░▒▒╥╫█▀  ".center(screenWidth))
    print("  D:::::D     D:::::DO:::::O     O:::::OM::::::M M::::M M::::M M::::::M  I::::I  N::::::N N::::N N::::::NO:::::O     O:::::O             ▒░ ▀▀▀▓▄╥ç╖ ░░░▀██▀░▒╫▓█▀   ".center(screenWidth))
    print("  D:::::D     D:::::DO:::::O     O:::::OM::::::M  M::::M::::M  M::::::M  I::::I  N::::::N  N::::N:::::::NO:::::O     O:::::O           ╓▒▄██▄░░░░▀▀▀▀▓▄▄g░░▒▒╣▓█▀    ".center(screenWidth))
    print("  D:::::D     D:::::DO:::::O     O:::::OM::::::M   M:::::::M   M::::::M  I::::I  N::::::N   N:::::::::::NO:::::O     O:::::O          ╥░░███▀░░░░░░░░░░░▀▀▒╫╫▓█▀     ".center(screenWidth))
    print("  D:::::D     D:::::DO:::::O     O:::::OM::::::M    M:::::M    M::::::M  I::::I  N::::::N    N::::::::::NO:::::O     O:::::O         ╣░▄▄▄░░░░░░░░░▄███░▒▒╫╫▓█▀      ".center(screenWidth))
    print("  D:::::D    D:::::D O::::::O   O::::::OM::::::M     MMMMM     M::::::M  I::::I  N::::::N     N:::::::::NO::::::O   O::::::O       ╓╝░████░░░░░▒▒▒▒████▒▒╫▓▓█▀       ".center(screenWidth))
    print("DDD:::::DDDDD:::::D  O:::::::OOO:::::::OM::::::M               M::::::MII::::::IIN::::::N      N::::::::NO:::::::OOO:::::::O      Æ╜░░╙▀▀░░░░▒▒▒░▄▄▄▒▒▒▒╫▓▓█▀        ".center(screenWidth))
    print("D:::::::::::::::DD    OO:::::::::::::OO M::::::M               M::::::MI::::::::IN::::::N       N:::::::N OO:::::::::::::OO      ▓░████░░░░░▒▒▒▒████▌▒▒╫▓▓█┘         ".center(screenWidth))
    print("D::::::::::::DDD        OO:::::::::OO   M::::::M               M::::::MI::::::::IN::::::N        N::::::N   OO:::::::::OO      ╒▓▒▒███▀░░▒▒▒▒▒▒▒▀██▀▒▒╫▓▓█           ".center(screenWidth))
    print("DDDDDDDDDDDDD             OOOOOOOOO     MMMMMMMM               MMMMMMMMIIIIIIIIIINNNNNNNN         NNNNNNN     OOOOOOOOO         ▀▓▓▓@▒▒▒▒▒▒▒▒▄███▒▒▒░╫▓▓█            ".center(screenWidth))
    print("                                                                                                                                   ▀▓▓▓▓▒▒▒▒▒████▌╢,▓▓▓█             ".center(screenWidth))
    print("                                                                                                                                      `▀▓▓▓▓╣▒▀▀▒╢▒▓▓██              ".center(screenWidth))
    print("                                                                                                                                          ╙▀▓▓▓╣╣▒▓▓██               ".center(screenWidth))
    print("                                                                                                                                             ╙▀▓▓▓██                 ".center(screenWidth))
    print("╔════════════════════════╗".center(screenWidth))
    print("║ 1. Jugar               ║".center(screenWidth))
    print("║ 2. Salir del juego     ║".center(screenWidth))
    print("╚════════════════════════╝".center(screenWidth))

def imprimirMenuColor():
    #Para centrarlo correcramente, hay que añadir 29 caracteres + los caracteres que ocupe el color extra al ancho de la pantalla por cada color añadido por linea
    #Ejemplo: Si coloreo una parte de la linea con rojo (255,0,0) el valor queda 29+3+1+1=32
    print((colored(255, 100, 47,"DDDDDDDDDDDDD             OOOOOOOOO     MMMMMMMM               MMMMMMMMIIIIIIIIIINNNNNNNN        NNNNNNNN     OOOOOOOOO         ")+"                    ,,``──╓,         ").center(screenWidth+32*1+5))
    print((colored(255, 100, 47,"D::::::::::::DDD        OO:::::::::OO   M:::::::M             M:::::::MI::::::::IN:::::::N       N::::::N   OO:::::::::OO       ")+"                 `░"+colored(0,0,0,"███▄")+"░░░░░░░░░▒▒H─~").center(screenWidth+32*2+5))
    print((colored(255, 100, 47,"D:::::::::::::::DD    OO:::::::::::::OO M::::::::M           M::::::::MI::::::::IN::::::::N      N::::::N OO:::::::::::::OO     ")+"               ╓░░░░░░░░░░░░░"+colored(0,0,0,"████")+"░▒▒▓").center(screenWidth+32*2+5))
    print((colored(255, 100, 47,"DDD:::::DDDDD:::::D  O:::::::OOO:::::::OM:::::::::M         M:::::::::MII::::::IIN:::::::::N     N::::::NO:::::::OOO:::::::O    ")+"              ¿░░░░░░"+colored(0,0,0,"╓▄██µ")+"░░░"+colored(0,0,0,"▀▀▀")+"░▒▒▓▓").center(screenWidth+32*3+5))
    print((colored(255, 100, 47,"  D:::::D    D:::::D O::::::O   O::::::OM::::::::::M       M::::::::::M  I::::I  N::::::::::N    N::::::NO::::::O   O::::::O    ")+"             ░"+colored(0,0,0,"+▄▄+")+"░░░"+colored(0,0,0,"▀██▀")+"░░░░░░░▒,╢▓▌").center(screenWidth+32*3+5))
    print((colored(255, 100, 47,"  D:::::D     D:::::DO:::::O     O:::::OM:::::::::::M     M:::::::::::M  I::::I  N:::::::::::N   N::::::NO:::::O     O:::::O    ")+"           ╓░░"+colored(0,0,0,"███▀")+"░░░░░░░░░░░░░▒╓╫█▀ ").center(screenWidth+32*2+5))
    print((colored(255, 100, 47,"  D:::::D     D:::::DO:::::O     O:::::OM:::::::M::::M   M::::M:::::::M  I::::I  N:::::::N::::N  N::::::NO:::::O     O:::::O    ")+"          ∩░,░░░░░░░░░░░"+colored(0,0,0,"████")+"░▒▒╥╫█▀  ").center(screenWidth+32*2+5))
    print((colored(255, 100, 47,"  D:::::D     D:::::DO:::::O     O:::::OM::::::M M::::M M::::M M::::::M  I::::I  N::::::N N::::N N::::::NO:::::O     O:::::O    ")+"         ▒░ ▀▀▀▓▄"+colored(209, 191, 50,"╥ç╖")+" ░░░"+colored(0,0,0,"▀██▀")+"░▒╫▓█▀   ").center(screenWidth+32*3+10))
    print((colored(255, 100, 47,"  D:::::D     D:::::DO:::::O     O:::::OM::::::M  M::::M::::M  M::::::M  I::::I  N::::::N  N::::N:::::::NO:::::O     O:::::O    ")+"       ╓▒"+colored(0,0,0,"▄██▄")+"░░░░▀▀▀▀▓▄▄g░░▒▒╣▓█▀    ").center(screenWidth+32*2+5))
    print((colored(255, 100, 47,"  D:::::D     D:::::DO:::::O     O:::::OM::::::M   M:::::::M   M::::::M  I::::I  N::::::N   N:::::::::::NO:::::O     O:::::O    ")+"      ╥░░"+colored(0,0,0,"███▀")+"░░░░░░░░░░░▀▀▒╫╫▓█▀     ").center(screenWidth+32*2+5))
    print((colored(255, 100, 47,"  D:::::D     D:::::DO:::::O     O:::::OM::::::M    M:::::M    M::::::M  I::::I  N::::::N    N::::::::::NO:::::O     O:::::O    ")+"     ╣░"+colored(0,0,0,"▄▄▄")+"░░░░░░░░░"+colored(0,0,0,"▄███")+"░▒▒╫╫▓█▀      ").center(screenWidth+32*3+5))
    print((colored(255, 100, 47,"  D:::::D    D:::::D O::::::O   O::::::OM::::::M     MMMMM     M::::::M  I::::I  N::::::N     N:::::::::NO::::::O   O::::::O    ")+"   ╓╝░"+colored(0,0,0,"████")+"░░░░░▒▒▒▒"+colored(0,0,0,"████")+"▒▒╫▓▓█▀       ").center(screenWidth+32*3+5))
    print((colored(255, 100, 47,"DDD:::::DDDDD:::::D  O:::::::OOO:::::::OM::::::M               M::::::MII::::::IIN::::::N      N::::::::NO:::::::OOO:::::::O    ")+"  Æ╜░░"+colored(0,0,0,"╙▀▀")+"░░░░▒▒▒░"+colored(0,0,0,"▄▄▄")+"▒▒▒▒╫▓▓█▀        ").center(screenWidth+32*3+5))
    print((colored(255, 100, 47,"D:::::::::::::::DD    OO:::::::::::::OO M::::::M               M::::::MI::::::::IN::::::N       N:::::::N OO:::::::::::::OO     ")+" ▓░"+colored(0,0,0,"████")+"░░░░░▒▒▒▒"+colored(0,0,0,"████▌")+"▒▒╫▓▓█┘         ").center(screenWidth+32*3+5))
    print((colored(255, 100, 47,"D::::::::::::DDD        OO:::::::::OO   M::::::M               M::::::MI::::::::IN::::::N        N::::::N   OO:::::::::OO      ")+"╒▓▒▒"+colored(0,0,0,"███▀")+"░░▒▒▒▒▒▒▒"+colored(0,0,0,"▀██▀")+"▒▒╫▓▓█           ").center(screenWidth+32*3+5))
    print((colored(255, 100, 47,"DDDDDDDDDDDDD             OOOOOOOOO     MMMMMMMM               MMMMMMMMIIIIIIIIIINNNNNNNN         NNNNNNN     OOOOOOOOO         ")+"▀▓▓▓@▒▒▒▒▒▒▒▒"+colored(0,0,0,"▄███")+"▒▒▒░╫▓▓█            ").center(screenWidth+32*2+5))
    print(("                                                                                                                                   ▀▓▓▓▓▒▒▒▒▒"+colored(0,0,0,"████▌")+"╢,▓▓▓█             ").center(screenWidth+32*1))
    print(("                                                                                                                                      `▀▓▓▓▓╣▒"+colored(0,0,0,"▀▀")+"▒╢▒▓▓██              ").center(screenWidth+32*1))
    print(("                                                                                                                                          ╙▀▓▓▓╣╣▒▓▓██               ").center(screenWidth))
    print(("                                                                                                                                             ╙▀▓▓▓██                 ").center(screenWidth))
    print((colored(24, 199, 119,"╔════════════════════════╗")).center(screenWidth+32*1+5))
    print((colored(24, 199, 119,"║")+" 1. Jugar               "+colored(24, 199, 119,"║")).center(screenWidth+32*2+4*2))
    print((colored(24, 199, 119,"║")+" 2. Salir del juego     "+colored(24, 199, 119,"║")).center(screenWidth+32*2+4*2))
    print((colored(24, 199, 119,"╚════════════════════════╝")).center(screenWidth+32*1+5))
                                                                                                                                                                                                                                           

def menuInicial(color=False):
    #Imprimo el menú correspondiente
    if color:
        imprimirMenuColor()
    else:
        imprimirMenu()

    #Elijo una opción
    print("SELECCIONA UNA OPCIÓN:".center(screenWidth))

    entrada = (screenWidth//2-3)*" " + "=> "
    entrada = input(entrada)
    #Limpio la entrada y la devuelvo
    try:
        entrada = int(entrada)
        if entrada == 1: #Jugar
            return 1
        elif entrada == 2: #Salir del juego
            return 2
        else:
            return 0 #Si la entrada no es válida se vuelve a preguntar
    except:
        return 0 #Si la entrada no es válida se vuelve a preguntar

def PantallaFinal(ganador):
    print()
    print()
    print("╔═══════════════════╗".center(screenWidth))
    print(f"║ GANA EL JUGADOR {ganador+1} ║".center(screenWidth))
    print("╚═══════════════════╝".center(screenWidth))
    input()

def NumeroJugadores():
    #Menu para preguntar el numero de jugadores
    numerocorrecto = False
    #Lo pregunto hasta que la respuesta sea válida
    while numerocorrecto == False:
        print()
        print('¿Cuantas personas quieren jugar?'.center(screenWidth))
        try:
            entrada = (screenWidth//2-6)*" " + "=> "
            numero = int(input(entrada))
            if numero > 1 and numero < 5:
                numerocorrecto = True
            else: #Si no lo es vuelvo a preguntar porque no salgo del bucle
                print('Número de jugadores no válido. Introduzca un valor entre el 2 y el 4'.center(screenWidth))
                numerocorrecto = False
        except:#Si no lo es vuelvo a preguntar porque no salgo del bucle
            print("Introduzca un valor correcto entre el 2 y el 4".center(screenWidth))
    return numero

def CantidadPuntos():
    #Menu para preguntar la cantidad de puntos a los que se va a jugar
    #Funciona de manera similar al del numeros de jugadores
    numerocorrecto = False
    while numerocorrecto == False:
        print()
        print('¿A cuántos puntos queréis jugar? (Por defecto es 30)'.center(screenWidth))
        try:
            entrada = (screenWidth//2-6)*" " + "=> "
            numero = int(input(entrada))
            if numero > 0 and numero < 101:
                numerocorrecto = True
            else:
                print('Número de puntos no válido. Introduzca un valor entre el 1 y el 100'.center(screenWidth))
                numerocorrecto = False
        except:
            print("Introduzca un valor correcto entre el 1 y el 100".center(screenWidth))
    return numero
