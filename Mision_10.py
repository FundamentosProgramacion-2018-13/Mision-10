# Autor: Humberto Carrillo Gómez
# Descripción: Diferentes funciones que se ejecutan con base en la tabla de posiciones de la Liga MX.

import matplotlib.pyplot as plot      # Importar la libreria

def reportarErorrPuntos(nombreArchivo):  # Regresa los equipos cuyos puntos están mal sumados
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()          # Título 1
    entrada.readline()          # Título 2

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jG = int(datos[2])
        jE = int(datos[3])
        pr = int(datos[8])
        pc = jG*3 + jE*1
        if pr != pc:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


def listarEquiposOrdenados(nombreArchivo):  # Regresa una lista con los equipos ordenados alfabéticamente.
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


def graficarPuntos(nombreArchivo):           # Regresa una gráfica de équipos vs puntos.


    entrada = open(nombreArchivo, "r", encoding= "UTF-8")
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


def reportarEquiposyPuntos(nombreArchivo):            # Regresa el nombre de los equipos y los puntos que llevan.

    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    listaEquiposyPuntos = []
    diccionarioPuntos = {}

    for linea in entrada:

        datos = linea.split("&")
        equipos = datos[0]
        puntos = int(datos[8])
        diccionarioPuntos[equipos] = puntos
    entrada.close()

    return diccionarioPuntos


def calcularPartidosPerdidos (nombreArchivo):   # Regresa los nombres de los equipos que han perdido 3 o menos partidos.

    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    listaMenor3= []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        partidosPerdidos = int(datos[4])
        if partidosPerdidos <= 3:
            listaMenor3.append(equipo)

    entrada.close()

    return listaMenor3


def calcularMenorDiferencia(nombreArchivo):           # Calcula el equipo que tenga la menor diferencia de goles.
    entrada = open(nombreArchivo, 'r', encoding='UTF-8')
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2
    equipoMenor = ''
    menorDif = 0

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        diferenciaGoles = int(datos[7])
        if diferenciaGoles < menorDif:
            menorDif = diferenciaGoles
            equipoMenor = datos[0]
    entrada.close()

    return equipoMenor


def generarArchivo(nombreArchivo):      # Genera un archivo con los 5 últimas posiciones de la liga.
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    #Archivo de salida:
    salida = open('Puntos.txt', 'w')

    entrada.readline()
    entrada.readline()
    diccionarioEquiposPuntos = {}
    listaPuntos = []
    for linea in entrada:
        datos = linea.split('&')
        equipo = datos[0]
        puntos = int(datos[8])
        listaPuntos.append(puntos)
        diccionarioEquiposPuntos[equipo] = puntos
        listaPuntos.sort()
    fondoTabla = listaPuntos[:5]
    equipoFondo = ''
    puntos = 0
    for k in range(len(fondoTabla)):                           # Escribir en el archivo 5 veces
        for llave, valor in diccionarioEquiposPuntos.items():   # Visitar equipos y puntos
            if fondoTabla[k] == valor:
                equipoFondo = llave
                puntos = valor
                del diccionarioEquiposPuntos[llave]       # Borrar la llave que en este caso es el nombre del equipo.
                break                                     # Esto evita que se repitan los nombres de los equipos
        salida.write("%s %d\n" % (equipoFondo, puntos))      # Escribir en el nuevo archivo

    salida.close()
    entrada.close()

    return


def main():
    ordenados = listarEquiposOrdenados("LigaMx.txt")
    print(ordenados)
    equiposyPuntos = reportarEquiposyPuntos("LigaMx.txt")
    print(equiposyPuntos)
    partidosPerdidos = calcularPartidosPerdidos('LigaMx.txt')
    print(partidosPerdidos)
    errores = reportarErorrPuntos("LigaMx.txt")
    print(errores)
    menorDiferencia = calcularMenorDiferencia('LigaMx.txt')
    print(menorDiferencia)
    generarArchivo('LigaMx.txt')
    graficarPuntos("LigaMx.txt")



main()