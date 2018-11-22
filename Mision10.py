#David Rodriguez

import matplotlib.pyplot as plot


def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaEquipos = []
    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())
    listaEquipos.sort()
    entrada.close()
    return listaEquipos

def mostrarPuntos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaEquiposYPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquiposYPuntos.append(datos[0])
        listaEquiposYPuntos.append(datos[8])
    return listaEquiposYPuntos

def mostrarTresOMenos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaTresOMenos = []
    for linea in entrada:
        datos = linea.split("&")
        if int(datos[4]) >= 3:
            listaTresOMenos.append(datos[0])
    return listaTresOMenos


def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaEquiposError = []
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        pr = int(datos[8])
        pc = jg*3 + je*1
        if pr != pc:
            listaEquiposError.append(equipo)
    entrada.close()
    return listaEquiposError


def graficarPuntos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
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
    ordenados = listarEquiposOrdenados("ligaMX.txt")
    print(ordenados)
    puntos = mostrarPuntos("ligaMX.txt")
    print(puntos)
    tres = mostrarTresOMenos("LigaMX.txt")
    print(tres)
    errores = reportarErrorPuntos("ligaMX.txt")
    print(errores)
    graficar = graficarPuntos("ligaMX.txt")
    print(graficar)

main()