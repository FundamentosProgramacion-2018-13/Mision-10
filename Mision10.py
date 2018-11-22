# Autor: Juan Carlos Flores García, A01376511. Grupo 4

# Descripción:

import matplotlib.pyplot as plot

# 1
def listarEquiposOrdenados(nombre):
    entrada = open(nombre, "r")

    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    entrada.close()

    return listaEquipos

# 2
def


# 4
def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r")

    entrada.readline()
    entrada.readline()

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        pr = int(datos[8])
        pc = jg * 3 + je * 1
        if pr != pc:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


def graficarPuntos(nombre):
    entrada = open(nombre, "r")

    entrada.readline()
    entrada.readline()

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    # graficar
    plot.plot(listaEquipos, listaPuntos)

    plot.show()

def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print(ordenados)

    errores = reportarErrorPuntos("LigaMX.txt")
    print(errores)

    graficarPuntos("LigaMX.txt")

main()

