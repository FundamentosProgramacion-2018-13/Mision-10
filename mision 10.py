import matplotlib.pyplot as plot


def ordenarEquipos(nombreArchivo):
    archivo = open(nombreArchivo, "r", encoding="UTF-8")
    nombres = []
    archivo.readline()
    archivo.readline()

    for linea in archivo:
        datos = linea.upper()
        datos = datos.split("&")
        nombresLista = datos[0]
        nombres.append(nombresLista)
        nombres.sort()
    archivo.close()
    return (nombres)


def encontrarEquipos():
    archivo = open("LigaMX.txt", "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    for linea in archivo:
        linea = linea.rstrip()
        lista = linea.split("&")
        lista = lista[0:9:8]
        print(lista)
    archivo.close()


def listaPerdedores():
    archivo = open("LigaMX.txt", "r", encoding="UTF-8")
    global nuevalista
    archivo.readline()
    archivo.readline()

    for linea in archivo:
        linea = linea.rstrip()
        lista = linea.split("&")
        lista = lista[0:4]

        if int(lista[3]) <= 3:
            nuevalista = []
            nuevalista.append(lista[0])
            return (nuevalista)
    archivo.close()
    return (nuevalista)


def buscarEquiposError(nombreArchivo):
    archivo = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    archivo.readline()
    archivo.readline()

    for linea in archivo:

        datos = linea.split("&")
        equipo = datos[0]
        juegosGanados = int(datos[2])
        juegosEmpatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = juegosGanados * 3 + juegosEmpatados * 1

        if puntos != puntosReportados:
            equipos.append(equipo)
    archivo.close()
    return equipos


def encontrarMenorDiferencia():
    archivo = open("LigaMX.txt", "r", encoding="UTF-8")  # Se abre archivo en modo lectura
    global goles
    global equipo
    archivo.readline()  # Desecha el primer titulo (linea)
    archivo.readline()  # Desecha el segundo titulo (linea)
    diccionario = {}

    for linea in archivo:
        linea = linea.rstrip()
        lista = linea.split("&")
        diccionario[lista[0]] = lista[7]
    for valor in diccionario.values():

        if valor >= str(-1) and valor <= str(0):
            goles = valor

        for nombre, diferencia in diccionario.items():

            if goles == diferencia:
                equipo = nombre
    archivo.close()
    return (equipo)


def graficarPuntos(nombreArchivo):
    archivo = open(nombreArchivo, "r", encoding="UTF-8")  # Se abre archivo en modo lectura
    archivo.readline()
    archivo.readline()  # Se salta una linea
    listaEquipos = []
    listaPuntos = []

    for linea in archivo:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))
    plot.plot(listaEquipos, listaPuntos)
    plot.show()
    archivo.close()