
#Este script sólo contiene la clase ficha
#Es la clase principal del programa y consiste en cada las fichas
#Pueden funcionar no solo como objetos para imprimir, sino también como listas enlazadas.
class ficha():
    def __init__(self, v1=0, v2=0, conex1=None, conex2=None, pos=0):
        #V1 es izquierda y v2 es derecha
        self.conex1 = conex1 #Conexión 1, derecha
        self.conex2 = conex2 #Conexión 2, izquierda

        #Si la ficha es vertical arriba <-> derecha ; abajo <-> izquierda
        self.pos = pos #Posicion (1 horizontal, 0 vertical)
        #Los valores dependen de las conexiones
        if conex2:
            self.v1 = v1 if conex2.v2 == v1 else v2
            self.v2 = v2 if conex2.v2 == v1 else v1
        elif conex1:
            self.v1 = v1 if conex1.v1 == v2 else v2
            self.v2 = v2 if conex1.v1 == v2 else v1
        else:
            self.v1 = v1
            self.v2 = v2
        

    def imprimir(self):
        #Imprime la ficha en la consola
        #Hay distintos casos posibles
        #Que la ficha sea horizontal o vertical
        #En el caso horizontal la pieza consta de 3 lineas
        #En el caso vertical la pieza consta de 5 lineas

        if self.pos == 1: #La pieza es horizontal

            linea1 = "┌───┬───┐"
            linea2 = "│ " +str(self.v1) + " │ " + str(self.v2) + " │"
            linea3 = "└───┴───┘"
            return linea1, linea2, linea3
        else: #La pieza es vertical. Lo planteamos como parte de arriba y parte de abajo.
            linea1 = "┌───┐"
            linea2 = "│ " +str(self.v1) + " │"
            linea3 = "├───┤"
            linea4 = "│ " +str(self.v2) + " │"
            linea5 = "└───┘"
            return linea1, linea2, linea3, linea4, linea5
            