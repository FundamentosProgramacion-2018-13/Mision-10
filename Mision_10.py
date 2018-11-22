# Autor: Ithan Alexis Pérez Sánchez
# Matrícula: A01377717
# Descrición: Mision 10

# El codigo empieza después de esta linea
from typing import List

import matplotlib.pyplot as plot


def equiposOrdenados(Archivo):
    entrada = open(Archivo, "r")

    entrada.readline()
    entrada.readline()

    lista = []
    archivo = entrada.readlines()

    for linea in archivo:
        datos = linea.split("&")
        equipos = datos[0]
        alfa = equipos.upper()
        lista.append(alfa)

    lista.sort()

    return lista


def mostrarEquipos(Archivo):
    entrada = open(Archivo, "r")

    entrada.readline()  # Titulo1
    entrada.readline()  # Titulo2

    a = {}

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = datos[8]

        a[equipo] = int(puntos)

    return a


def menorPerdidos(Archivo):
    entrada = open(Archivo, "r")

    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2

    lista = []

    for linea in entrada:
        datos = linea.split("&")
        equipos = datos[0]
        juegosPerdidos = int(datos[4])

        if 4 > juegosPerdidos:
            lista.append(equipos)

    return lista


def buscarEquiposError(Archivo):
    entrada = open(Archivo, "r")

    equipos = []

    entrada.readline()  # Titulo1
    entrada.readline()  # Titulo2

    for linea in entrada:
        # linea = ¨¨
        datos = linea.split("&")  # ["Veracruz", "16", ...]
        equipo = datos[0]
        juegoGanados = int(datos[2])
        juegoEmpatatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = juegoGanados * 3 + juegoEmpatatados * 1

        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos

# Duda de como resolver
def diferenciaGoles(Archivo):
    pass


# Corregir el archivo nuevo
def nuevoArchivo(Archivo, salida):
    entrada = open(Archivo, "r")

    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2

    valor = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])

        if 16 >= puntos:
            valor.append(equipo)

        salida.write(str(valor))

    entrada.close()
    salida.close()
    return valor


def graficarPuntos(Archivo):
    entrada = open(Archivo, "r")

    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()

    entrada.close()


def main():
    salida = open("Puntos.txt", "w", encoding="UTF-8")
    print(equiposOrdenados("LigaMX.txt"))
    print(mostrarEquipos("LigaMX.txt"))
    print(menorPerdidos("LigaMX.txt"))
    print(buscarEquiposError("LigaMX.txt"))
    print(diferenciaGoles("LigaMX.txt"))
    print(nuevoArchivo("LigaMX.txt", salida))
    graficarPuntos("LigaMX.txt")


main()
