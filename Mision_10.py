# Autor: Luis Ricardo Chagala Cervantes.
#
import matplotlib.pyplot as plot


#1.
def equiposOrdenados (nombrearchivo):
    entrada = open(nombrearchivo, "r")

    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        datos = linea.split("&")
        equipos.append(datos[0])
    for x in range (0, len(equipos)):
        equipos[x] = equipos[x].upper()

    entrada.close()
    return equipos

#2
def equiposPuntos(nombrearchivo):
    entrada = open(nombrearchivo, "r")

    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        datos = linea.split("&")
        puntos = int(datos [8])
        equipos.append(datos[0])
        equipos = equipos, puntos
    for x in range(0, len(equipos)):
        equipos[x] = equipos[x].upper()

    entrada.close()
    return equipos

# 3.
def menosPartidosPerdidos(nombrearchivo):
    entrada = open(nombrearchivo, "r")

    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        pperdidos = int(datos[4])
        if pperdidos <= 3:
            equipos.append(equipo)

    entrada.close()

    return equipos

# 4. Buscar los equipos que tienen mal reportado el número de puntos.
def buscarEquiposError(nombrearchivo):
    entrada = open(nombrearchivo, "r")

    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        # Linea = 'Veracruz&16&2&4&10&16&36&-20&10'
        datos = linea.split("&")    # ["Veracruz, 16, ...]
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg*3 + je*1
        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos

#5
def menorGoles(nombrearchivo):
    entrada = open(nombrearchivo, "r")

    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2


# 6. Archivo Nuevo
def archivoNuevo(nombrearchivo):
    entrada = open(nombrearchivo, "r")
    salida = open("Puntos.txt", "w")

    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        datos = linea.split("&")
        equipos.append(datos[0])
    for x in range(0, len(equipos)):
        equipos[x] = equipos[x].upper()
        salida.write(equipos)

    salida.close()
    entrada.close()


# 7. Grafica
def graficarPuntos(nombrearchivo):
    entrada = open(nombrearchivo, "r")

    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    listaequipos = []
    listapuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaequipos.append(datos[0])
        listapuntos.append(int(datos[8]))

    plot.plot(listaequipos, listapuntos)
    plot.show()

    entrada.close()


def main():
    ordenado = equiposOrdenados("LigaMX.txt")
    print("1. ", ordenado)
    puntos = equiposPuntos("LigaMX.txt")
    print("2. ", puntos)
    perdidos = menosPartidosPerdidos("LigaMX.txt")
    print("3. ", perdidos)
    errores = buscarEquiposError("LigaMX.txt")
    print("4. ", errores)
    archivoNuevo("LigaMX.txt")
    graficarPuntos("LigaMX.txt")

main()