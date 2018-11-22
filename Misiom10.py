# Autor: Luisa Fernanda Arellano Alvarado
# mision 10

import matplotlib.pyplot as plot


# funcion 4
def BuscarEquiposConError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline() # Título 1
    entrada.readline() # Título 2 borrar

    for linea in entrada:
        datos = linea.split("&") # split separar datos, ["veracruz" , "16",...]
        equipo = datos[0]
        juegosganados = int(datos[2])
        juegosempatados = int(datos[3]) # datos en la posición 3
        puntosReportados = int(datos[8])
        puntos = juegosganados*3 + juegosempatados*1
        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()
    return equipos

def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2 borrar
    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()
    entrada.close


'''''
def MostrarNombres(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding= "UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()  # Títul
    nombres = []
    for linea in entrada:
        d = entrada.upper
        nombres.append(d)
    entrada.close()
'''


def MMostrarNombres(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    listaEquipos = []
    entrada.readline()
    entrada.readline()
    for linea in entrada:
        datos=linea.split("&")
        listaEquipos.sort()
        listaEquipos.append(datos[0])
    entrada.close()
    return listaEquipos


def DefinirPerdedor (nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    perdedores = []
    entrada.readline()  # Titulo 1 borrado
    entrada.readline()  # Titulo 2 borrardo
    for linea in entrada:
        datos=linea.split("&")
        equipo=datos[0]
        juegosPerdidos= int(datos[4])
        if juegosPerdidos <= 3:
            perdedores.append(equipo)
    entrada.close()
    return perdedores


def main():
    errores = BuscarEquiposConError("LigaMX.txt")
    print(errores)
    graficarPuntos("LigaMX.txt")
    print(MMostrarNombres("LigaMX.txt"))
    print(DefinirPerdedor("LigaMX.txt"))


main()
