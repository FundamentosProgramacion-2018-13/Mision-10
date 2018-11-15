#Carlos Badillo García
#

import matplotlib.pyplot as plot

def reportarErroresPuntos(nombre):
    entrada = open(nombre, "r", encoding="UTF8")
    entrada.readline()      #Titulo 1 (no queremos procesar)
    entrada.readline()      #Titulo 2
    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        pr = int(datos[8])
        pc = (jg*3) + (je*1)

        if pr != pc:
            listaEquiposError.append(equipo)
    entrada.close()
    return listaEquiposError


def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF8")
    entrada.readline()
    entrada.readline()
    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()
    entrada.close()

    return listaEquipos


def puntosEquipos():

def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF8")
    entrada.readline()
    entrada.readline()

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()

def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    errores = reportarErroresPuntos("LigaMX.txt")
    print(ordenados)
    print(errores)
    print(graficarPuntos("LigaMX.txt"))

main()