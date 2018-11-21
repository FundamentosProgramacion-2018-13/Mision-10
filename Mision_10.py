# Zoe Caballero Dominguez A01747247
# Varias funciones que utlizan los datos de la liga de BBVA Bancomer

#Librerias
import matplotlib.pyplot as plot


# 1. Ordena los nombres de los equipos alfabéticamente y los pone en mayúsculas
def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8" )
    entrada.readline() #Las lineas que no queremos procesar
    entrada.readline() #Titulos

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    entrada.close()

    return listaEquipos


#2. Crea un diccionario con los equipos y sus puntos correspondientes
def crearDiccionarioEquiposYPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Las lineas que no queremos procesar
    entrada.readline()  # Titulos

    diccionarioEquiposPuntos = {}

    for linea in entrada:
        datos = linea.split("&")
        diccionarioEquiposPuntos[datos[0]] = int(datos[8])

    entrada.close()

    return diccionarioEquiposPuntos


#3. Hace una lista de los equipos que han perdido 3 partidos o menos
def listarEquiposPartidosPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Las lineas que no queremos procesar
    entrada.readline()  # Titulos

    equiposPartidoPerdido =  []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        partidosPerdidos = int(datos [4])
        if partidosPerdidos <= 3:
            equiposPartidoPerdido.append(equipo)

    entrada.close()
    return equiposPartidoPerdido


#4. Encuentra los equipos que tienen error en los puntos reportados
def reportarErrorPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Las lineas que no queremos procesar
    entrada.readline()  # Titulos

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        juegosGanados = int(datos[2])
        juegosEmpatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntosCalculados = juegosGanados * 3 + juegosEmpatados * 1

        if puntosReportados != puntosCalculados:
            listaEquiposError.append(equipo)

    listaEquiposError.sort()
    entrada.close()
    return listaEquiposError


#5. Encuentra el equipo con menor diferencia de goles
def encontrarMenorDiferenciaGoles(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Las lineas que no queremos procesar
    entrada.readline()  # Titulos

    diccionarioEquiposPuntos = {}
    menor = 0

    for linea in entrada:
        datos = linea.split("&")
        diccionarioEquiposPuntos[datos[0]] = int(datos[7])
    for valor in diccionarioEquiposPuntos.values():
        if menor > valor:
            menor = valor
    for equipo, goles in diccionarioEquiposPuntos.items():
        if menor == goles:
            equipoMenor = equipo


    entrada.close()

    return equipoMenor


#6. Crea un archivo con los ultimos lugares de la tabla
def crearArchivoPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Las lineas que no queremos procesar
    entrada.readline()  # Titulos

    salida = open("Puntos.txt","w", encoding="UTF-8")

    diccionarioEquiposPuntos = {}
    listaPuntos = []
    listaEquiposUltimmos = []

    for linea in entrada:
        datos = linea.split("&")
        diccionarioEquiposPuntos[datos[0]] = int(datos[8])
    for valor in diccionarioEquiposPuntos.values():
        listaPuntos.append(valor)
    listaPuntos.sort()
    listaPuntosUltimos = listaPuntos[0:5]

    for equipo, puntos in diccionarioEquiposPuntos.items():
        for puntosUltimos in listaPuntosUltimos:
            if puntos == puntosUltimos and (equipo not in listaEquiposUltimmos):
                listaEquiposUltimmos.append(equipo)
                salida.write("%s&%d\n" % (equipo, puntos))

    entrada.close()
    salida.close()


#7. Grafica los puntos de los equipos
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Las lineas que no queremos procesar
    entrada.readline()  # Titulos

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))
    entrada.close()
    #Graficar
    plot.plot(listaEquipos, listaPuntos)
    plot.show()

    
def main():
    print("1:")
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print (ordenados)
    print("2:")
    diccionario = crearDiccionarioEquiposYPuntos("LigaMX.txt")
    print(diccionario)
    print("3:")
    equipos3Perdidos = listarEquiposPartidosPerdidos("LigaMX.txt")
    print(equipos3Perdidos)
    print("4:")
    error = reportarErrorPuntos("LigaMX.txt")
    print(error)
    print("5:")
    equipoMenorDiferencia = encontrarMenorDiferenciaGoles("LigaMX.txt")
    print(equipoMenorDiferencia)

    crearArchivoPuntos("LigaMX.txt")
    graficarPuntos("LigaMX.txt")



#Llamar a main
main()
