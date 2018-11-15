#Autor : Joshua Sánchez martínez A01274269
#Sigue una serie de distintos pasos para obtener resultados varios


import matplotlib.pyplot as plot


def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()  #Título 1
    entrada.readline()  #Título 2

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jG = int(datos[2])
        jE = int (datos[3])
        pR = int(datos[8])
        pC = jG*3 + jE*1
        if pR != pC:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


def  listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo,"r",encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    entrada.close()

    return listaEquipos


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

    #graficar
    plot.plot(listaEquipos,listaPuntos)

    plot.show()


def puntosPorEquipo(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        p = int(datos[8])
        listaEquipos.append(equipo)
        listaEquipos.append(p)

    entrada.close()
    return listaEquipos


def perdidos (nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()  #Título 1
    entrada.readline()  #Título 2

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        per = int(datos[4])
        if per <= 3:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print(ordenados)
    errores = reportarErrorPuntos("LigaMX.txt")
    print(errores)
    puntos = puntosPorEquipo("LigaMX.txt")
    print(puntos)
    graficarPuntos("LigaMX.txt")
    pperdidos=perdidos("LigaMX.txt")
    print(pperdidos)




main()