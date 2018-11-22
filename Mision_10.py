#Marco González Elizalde
#Mision 10
import matplotlib.pyplot as plot


def ordenarAlfabeticamente(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Lee las primeras dos lineas para desecharlas al procesar las restantes
    entrada.readline()
    equipos = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0].upper()
        equipos.append(equipo)
    #Incompleto


def mostrarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Lee las primeras dos lineas para desecharlas al procesar las restantes
    entrada.readline()
    equipos = {}

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = datos[8]


def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline()  #Lee las primeras dos lineas para desecharlas al procesar las restantes
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntosReales = jg*3 + je
        if puntosReales != puntosReportados:
            equipos.append(equipo)
    entrada.close()
    return equipos


def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Lee las primeras dos lineas para desecharlas al procesar las restantes
    entrada.readline()

    equipos = []
    puntos = []

    for linea in entrada:
        datos = linea.split("&")
        equipos.append(datos[0])
        puntos.append(int(datos[8]))

    plot.plot(equipos, puntos)
    plot.show()

    entrada.close()


def main():
    ordenarAlfabeticamente("LigaMX.txt")
    buscarEquiposError("LigaMX.txt")
    graficarPuntos("LigaMX.txt")
    mostrarPuntos("LigaMX.txt")

main()
#No pude completar todos los puntos
