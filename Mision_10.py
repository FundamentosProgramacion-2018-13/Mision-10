#Autor Claudio Mayoral García

import matplotlib.pyplot as plot


def listarPuntajes(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaPuntos1 = []
    for linea in entrada:
        datos = linea.split("&")
        for linea in range(1, 4):
            jg = int(datos[linea])
            listaPuntos1.append(jg)

    return listaPuntos1


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


def reportarErrorPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        pr = int(datos[8])
        pc = jg*3 + je
        if pr != pc:
            listaEquipos.append(equipo)
    entrada.close()

    return listaEquipos

def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaEquipos = []
    listaPuntos = []
    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))
    plot.plot(listaEquipos,listaPuntos)

    plot.show()

def mostrarEquiposPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaPerdidos = []
    for linea in entrada:
        datos = linea.split("&")
        perdidos = int(datos[4])
        if perdidos <= 3:
            listaPerdidos.append(datos[0])
    entrada.close()
    return listaPerdidos

def mostrarEquiposyPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    entablar = {}
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        entablar[equipo] = puntos
    entrada.close()
    return entablar


def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print(ordenados)
    errores = reportarErrorPuntos("LigaMX.txt")
    print(errores)
    graficarPuntos("LigaMX.txt")
    mostrarEquipoyPunto = mostrarEquiposyPuntos("LigaMX.txt")
    print(mostrarEquipoyPunto)
    equiposPerdidos = mostrarEquiposPerdidos("LigaMX.txt")
    print(equiposPerdidos)
    puntos = listarPuntajes("LigaMX.txt")
    print(puntos)
main()
