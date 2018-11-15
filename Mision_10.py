#Autor: Samantha Martínez Franco A01747686


import matplotlib.pyplot as plot

def mostrarNombresEquipos(nombreArchivo):
    entrada=open(nombreArchivo,"r")
    entrada.readline()
    entrada.readline()
    listaEquipos=[]
    for linea in entrada:
        datos=linea.split("&")
        listaEquipos.append(datos[0].upper())
    listaEquipos.sort()

    entrada.close()
    return listaEquipos

def mostrarNombresPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()
    diccionario = {}
    for linea in entrada:
        datos = linea.split("&")
        diccionario[datos[0]]=int(datos[8])
    return diccionario


def reportarEquiposPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()
    listaEquipos = []
    for linea in entrada:
        datos = linea.split("&")
        equipo=datos[0]
        partidosPerdidos=int(datos[4])
        if partidosPerdidos<=3:
            listaEquipos.append(equipo)
    return listaEquipos


def reportarErroresPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()
    listaEquiposError = []
    for linea in entrada:
        datos = linea.split("&")
        equipo=datos[0]
        juegosGanados=int(datos[2])
        juegosEmpatados=int(datos[3])
        puntos=int(datos[8])
        puntosCalculados=juegosGanados*3+juegosEmpatados
        if puntos!=puntosCalculados:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()
    listaEquipos = []
    listaPuntos=[]

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))
    plot.plot(listaEquipos,listaPuntos)
    plot.show()


def mostrarDiferenciaGoles(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()
    puntos = {}
    for linea in entrada:
        datos = linea.split("&")
        equipo=datos[0]
        diferenciaGoles=int(datos[7])
        puntos[diferenciaGoles]=equipo
    listaPuntos=[puntos.keys()]
    listaPuntos.sort()
    menordiferencia=listaPuntos[0]
    equipoDiferencia=puntos[menordiferencia]
    return equipoDiferencia



def main():
    nombreArchivo="LigaMX.txt"
    ordenados=mostrarNombresEquipos(nombreArchivo)
    #print(ordenados)

    error=reportarErroresPuntos(nombreArchivo)
    #print(error)
    #graficarPuntos(nombreArchivo)

    #print(mostrarNombresPuntos(nombreArchivo))

    #print(reportarEquiposPerdidos(nombreArchivo))

    print(mostrarDiferenciaGoles(nombreArchivo))
main()
