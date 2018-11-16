# Alex Fernando Leyva Martinez - A01747078 - GRUPO 04
# Liga MX

import matplotlib.pyplot as plot


def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()
    entrada.close()
    return listaEquipos


def mostrarEquiposPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()

    dupla = {}

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        dupla[equipo] = puntos

    entrada.close()
    return dupla



def mostrarPartidosPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()

    listaEquipos = []
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        juegosPerdidos = int(datos[4])
        if juegosPerdidos <= 3:
            listaEquipos.append(equipo)

    return listaEquipos


def reportarError(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()          # Título 1
    entrada.readline()          # Título 2

    listaEquiposError =[]

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        juegosGanados = int(datos[2])
        juegosEmpatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntosCalculados = juegosGanados*3 + juegosEmpatados*1
        if puntosCalculados != puntosReportados:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError



def mostrarMenorDiferencia(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()

    listaEquiposMenorDiferencia = {}


    minimo = 0
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        diferenciaGoles = (int(datos[7]))
        listaEquiposMenorDiferencia[equipo] = diferenciaGoles

        for diferencia in listaEquiposMenorDiferencia.values():
            if diferencia > minimo:
                diferencia = minimo
            for minimo in listaEquiposMenorDiferencia.values():
                if diferenciaGoles == diferencia:
                    listaEquiposMenorDiferencia[equipo] = diferencia


    entrada.close()
    return listaEquiposMenorDiferencia
                                                # menor = min(diferenciaGoles)
                                                # if equipo == menor:
                                                # listaEquiposMenorDiferencia.append(equipo)

                                                # entrada.close()
                                                # return listaEquiposMenorDiferencia



def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()


    listaEquipos = []
    listaPuntos = []


    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    # Graficar
    plot.plot(listaEquipos, listaPuntos)
    plot.show()


def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print(ordenados)
    Error = reportarError("LigaMX.txt")
    print(Error)
    graficarPuntos("LigaMX.txt")
    puntos = mostrarEquiposPuntos("LigaMX.txt")
    print(puntos)
    perdidos = mostrarPartidosPerdidos("LigaMX.txt")
    print(perdidos)
    diferencia = mostrarMenorDiferencia("LigaMX.txt")
    print(diferencia)

main()
