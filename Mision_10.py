#Jesus Roberto Herrera Vieyra A01377230
# ISDR

import matplotlib.pyplot as plot


def buscarEquiposError(nombreArchivo):

    entrada = open(nombreArchivo,"r", encoding="")
    equipos = []
    entrada.readline()
    entrada.readline()     #Se leen las primeras lineas y se descartan


    for linea in entrada:  #Se separan los datos para poder seleccionar los que se desean guardar
        datos = linea.split("&")
        equipo = datos[0]
        juegosGanados = int(datos[2])
        juegosEmpatados = int(datos[3])
        puntos = int(datos[8])
        puntosReales = (juegosGanados*3) + juegosEmpatados

        if puntosReales != puntos:
            equipos.append(equipo)

    entrada.close()
    return equipos


def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="")
    entrada.readline()
    entrada.readline()
    equiposCorregidos = []
    puntosFinales = []

    for linea in entrada:   #Se separan y se escogen los datos deseados
        datos = linea.split("&")
        equiposCorregidos.append(datos[0])
        puntosFinales.append(int(datos[8]))

    plot.plot(equiposCorregidos, puntosFinales)
    plot.show()

    entrada.close()


def main():
    errores = buscarEquiposError("LigaMx.txt")
    print(errores)
    graficarPuntos("LigaMx.txt")

main()