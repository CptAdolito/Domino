
#Este script sirve paar imprimir el tablero, es decir, las fichas colocadas
import menu
screenWidth = menu.screenWidth

def imprimirTablero(fichaInicial):
    #Obtenemos la primera y la última ficha, además de la cantidad de fichas entre medias.
    primeraFicha = fichaInicial
    ultimaFicha = fichaInicial
    n = 1
    while primeraFicha.conex2 != None:
        n += 1
        primeraFicha = primeraFicha.conex2
    while ultimaFicha.conex1 != None:
        n += 1
        ultimaFicha = ultimaFicha.conex1
    
    maxFichas = 6 #El número máximo de fichas a imprimir por lado
    #El mayor problema de imprimirlo es que se puede salir de la pantalla
    #Para evitarlo establecemos un límite de fichas a imprimir

    #Dos casos posibles: Imprimimos todas, imprimimos las máximas a cada lado
    if n <= maxFichas*2:
        r = imprimir(primeraFicha, ultimaFicha)
    elif n > maxFichas*2:
        r = imprimir(primeraFicha, ultimaFicha, maxFichas)
    return r

def imprimir(primeraFicha, ultimaFicha, nFichas = None):
    #El string que sirve como unión enre los dos lados si no se imprime entero.
    #Sirve para dar a entender que existen fichas entre medias.
    union = [[" ".center(5), " ".center(5), "...".center(5), " ".center(5), " ".center(5)]]
    if nFichas == None: #Imprimimos todas recorriendo la lista enlazada en orden.
        resultado = list()
        ficha = primeraFicha
        while ficha.conex1 != None:
            resultado.append(ficha.imprimir())
            ficha = ficha.conex1
        resultado.append(ficha.imprimir())
    else: #Imprimimos sólo el número de fichas que sean necesarias, recorriendo la lista enlazada por ambos lados.
        resultado1 = list()
        resultado2 = list()
        ficha = primeraFicha
        n=0
        while ficha.conex1 != None and n <= nFichas:
            resultado1.append(ficha.imprimir())
            ficha = ficha.conex1
            n += 1
        ficha = ultimaFicha
        n=0
        while ficha.conex2 != None and n <= nFichas:
            resultado2.append(ficha.imprimir())
            ficha = ficha.conex2
            n += 1
        
        #Unimos ambos con la unión.
        #Hay que dar la vuelta a la lista resultado2 para que quede bien, ya que se ha recorrido hacia atrás.
        resultado2.reverse()
        resultado = resultado1 + union + resultado2
    
    #Limpiamos las filas y las dejamos listas para imprimir
    resultado = list(resultado)
    for i in range(len(resultado)):
        resultado[i] = list(resultado[i])
        #Si las fichas son horizontales necesitan espacios arriba y abajo para que no se descentren las verticales
        if len(resultado[i]) < 5:
            resultado[i].insert(0, "         ")
            resultado[i].append("         ")

    #Sumamos las filas para dejarlo en una sola lista de 5 elementos
    #Además las centramos en la consola
    resultado = [str("".join(i)).center(261) for i in zip(*resultado)]
            
    return resultado
