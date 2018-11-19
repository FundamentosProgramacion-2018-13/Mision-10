# Autor: David Isaí LópeZ Jaimes


import matplotlib.pyplot as plot

# 1. Ordenar los los nombres en mayusculas y alfabeticamente
def ordenarEpuipos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equiposOrdenados = []
    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2
    for linea in entrada:
        datos = linea.split("&")
        equiposOrdenados.append(datos[0])
    equiposOrdenados.sort()
    entrada.close()
    return equiposOrdenados


# 2. Manda equipos con sus respectivos puntos
def puntosEquipos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equiposPuntos = {}
    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2
    for linea in entrada:
        datos = linea.split("&")
        equiposPuntos[datos[0]] = int(datos[1])

    entrada.close()
    return equiposPuntos

# 3. Regresa lista con los equipos que han perdido 3 partidos o menos
def menorPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equiposMenosPerdidos = []
    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        if int(datos[4]) <= 3:
            equiposMenosPerdidos.append(equipo)

    entrada.close()
    return equiposMenosPerdidos


# 4. Buscar los equipos que tienen mal reportado el número de puntos
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equipos = []
    entrada.readline() # Titulo 1
    entrada.readline() # Titulo 2
    for linea in entrada:
        # linea = 'Atlas&16&2&5&9&10&24&-14&11'
        datos = linea.split("&")        # ["Veracruz", "16", ...]
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg*3 + je*1
        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos


def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline() # Titulo 1
    entrada.readline() # Titulo 2

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
    errores = buscarEquiposError("LigaMX.txt")
    print(errores)
    graficarPuntos("LigaMX.txt")
    orden = ordenarEpuipos("LigaMX.txt")
    print(orden)
    pEquipos = puntosEquipos("LigaMX.txt")
    print(pEquipos)
    menosPerdidos = menorPerdidos("LigaMX.txt")
    print(menosPerdidos)

main()