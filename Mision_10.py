# Autor: Roberto Emmanuel González Muñoz
# Resuelve el siguiente programa en python que use funciones.

import matplotlib.pyplot as plot


#  Mostrar los nombres de los equipos en mayúsculas ordenados alfabéticamente.
def mostrarNombresMayus(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    listaEquipos = []
    entrada.readline()  # Ignora primer Título
    entrada.readline()  # Ignora segundo Título

    for linea in entrada:
        datos = linea.split("&")
        equipo = str(datos[0])
        equipo = equipo.upper()
        listaEquipos.append(equipo)
    listaEquipos.sort()
    entrada.close()
    return listaEquipos




#  Mostrar el nombre de los equipos seguido de los puntos que llevan hasta el momento de acuerdo con el archivo.
def mostrarNombreyPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline()  # Ignora primer Título
    entrada.readline()  # Ignora segundo Título

    for linea in entrada:
        datos = linea.split("&")
        equipoypuntos = datos[0], int(datos[8])
        equipos.append(equipoypuntos)
    entrada.close()
    return equipos


#  Mostrar la lista de los equipos que han perdido 3 partidos o menos.
def mostrarLista3Perdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline()  # Ignora primer Título
    entrada.readline()  # Ignora segundo Título
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        perdidos = int(datos[4])
        if perdidos <= 3:
            equipos.append(equipo)
    entrada.close()
    return equipos



# Buscar en el archivo los nombres de los equipos que tienen mal reportado la cantidad de puntos.
# Un juego ganado aporta 3 puntos, un juego empatado aporta 1 punto y un juego perdido no aporta puntos.
def buscarequiposPuntosIncorrectos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline()  # Ignora primer Título
    entrada.readline()  # Ignora segundo Título

    for linea in entrada:
        datos = linea.split("&")    # Genera nueva lista apartir de la linea.
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg*3 + je*1
        if puntos != puntosReportados:
            equipos.append(equipo)
    entrada.close()
    return equipos


#  Mostrar el nombre del equipo con la menor diferencia de goles.
def mostrarEquipoMenorDiferenciaGol(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = {}
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        diferencia = int(datos[7])
        equipos[diferencia] = equipo
    minimum = min(equipos.keys())
    entrada.close()
    return equipos[minimum]


# Generar un nuevo archivo (Puntos.txt) que contiene el nombre y los puntos de los equipos
# que se encuentran en los últimos 5 lugares de la tabla de acuerdo con el archivo.
def generarArchivo5lugares(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    salida = open("Puntos.txt", "w", encoding="UTF-8")
    equipos = {}
    ultimos = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        equipos[puntos] = equipo

    for k in range(0, 5):
        minimum = min(equipos.keys())
        minequipo = equipos[minimum], minimum
        ultimos.append(minequipo)
        del equipos[minimum]
    salida.write(str(ultimos))
    entrada.close()
    salida.close()


#  Muestra una gráfica de equipos vs. puntos de acuerdo con el archivo.
def graficarEquipovsPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # Ignora primer Título
    entrada.readline()  # Ignora segundo Título

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos,listaPuntos)
    plot.show()

    entrada.close()


def main():
    a = mostrarNombresMayus("LigaMX.txt")
    b = mostrarNombreyPuntos("LigaMX.txt")
    c = mostrarLista3Perdidos("LigaMX.txt")
    d = buscarequiposPuntosIncorrectos("LigaMX.txt")
    e = mostrarEquipoMenorDiferenciaGol("LigaMX.txt")
    generarArchivo5lugares("LigaMX.txt")
    graficarEquipovsPuntos("LigaMX.txt")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


main()