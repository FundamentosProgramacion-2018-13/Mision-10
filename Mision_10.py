# Autor: Alejandro Torices Oliva
# Es un

import matplotlib.pyplot as plot


def sumaPuntos(nombre):
    entrada = open(nombre, 'r')
    entrada.readline()
    entrada.readline()

    puntosXequipo = {}

    for linea in entrada:
        datos = linea.split('&')
        equipo = datos[0]
        puntos = int(datos[8])
        puntosXequipo[equipo] = puntos
    print(puntosXequipo)


def reportarErrorPuntos(nombre):
    entrada = open(nombre, 'r')
    entrada.readline()
    entrada.readline()

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split('&')
        equipo = datos[0]
        jGanados = int(datos[2])
        jEmpatados = int(datos[3])
        pReportados = int(datos[8])
        pCalculados = jGanados*3 + jEmpatados
        if pReportados != pCalculados:
            listaEquiposError.append(equipo)
    print(listaEquiposError)

    entrada.close()


def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, 'r')
    entrada.readline()
    entrada.readline()

    listaEquipos = []

    for linea in entrada:
        datos = linea.split('&')
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    entrada.close()

    return listaEquipos


def graficarPuntos(nombre):
    entrada = open(nombre, 'r')
    entrada.readline()
    entrada.readline()

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split('&')
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    # Graficar
    plot.plot(listaEquipos, listaPuntos)

    plot.show()


def main():
    ordenados = listarEquiposOrdenados('LigaMX.txt')
    reportarErrorPuntos('LigaMX.txt')
    graficarPuntos('LigaMX.txt')
    print(ordenados)
    sumaPuntos('LigaMX.txt')

main()
