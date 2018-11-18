#Autor: Michelle Sánchez Guerrero
#Descripción: Misión 10

import matplotlib.pyplot as plot

#1. Función que muestra los nombres de los quipos ordenados alfabéticamente.
def mostrarNombresAlfabeticamente(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    ordenAlfabetico = []

    entrada.readline()  # Ignora la primera línea
    entrada.readline()  # Ignora la segunda línea

    for linea in entrada:
        datos = linea.split("&")
        ordenAlfabetico.append(datos[0])

    ordenAlfabetico.sort()

    entrada.close()

    return ordenAlfabetico


#2. Función que muestra el nombre del equipo seguido de los puntos que llevan
def mostrarEquipoPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equiposPuntos = []

    entrada.readline()  # Ignora la primera línea
    entrada.readline()  # Ignora la segunda línea

    for linea in entrada:
        datos = linea.split("&")
        nombre = datos[0]
        puntos = int(datos[8])   #.rstrip
        equiposPuntos.append((nombre, puntos))

    entrada.close()

    return equiposPuntos


#3. Función que muestra los equipos que han perdido 3 partidos o menos.
def mostrarMenosPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equipos = []

    entrada.readline()  # Ignora la primera línea
    entrada.readline()  # Ignora la segunda línea

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jp = int(datos[4])

        if jp <= 3:
            equipos.append(equipo)

    return equipos

#4. Función que busca los equipos que tienen mal reportado el número de puntos.
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding= "UTF-8")

    equipos = []

    entrada.readline()      #Ignora la primera línea
    entrada.readline()      #Ignora la segunda línea

    for linea in entrada:
        #linea = Veracruz&16&2&4&10&16&36&-20&10
        datos = linea.split("&")     # ["Veracruz", "16", ...]
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg * 3 + je * 1

        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos

#5. Función que muestra el equipo que tiene la menor diferencia de goles
def mostrarEqMenorDiferencia(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding= "UTF-8")

    entrada.readline()
    entrada.readline()

    equipoMenor = ""
    diferencia = 0

    for linea in entrada:
        datos = linea.split("&")

        if int(datos[7]) < diferencia:
            diferencia = int(datos[7])
            equipoMenor = datos[0]

    entrada.close()

    return equipoMenor


#6. Función que genera un archivo con los 5 equipos que están en el último lugar
def generarArchivo(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    salida = open("Puntos.txt", "w")

    entrada.readline()
    entrada.readline()

    equiposPuntos = {}
    puntos = []

    for linea in entrada:
        datos = linea.split("&")

        equipo = datos[0]

        equiposPuntos[equipo] = int(datos[8])
        puntos.append(int(datos[8]))

    puntos.sort()

    peores = puntos[:5]

    for k in range(0,5):
        for llave, valor in equiposPuntos.items():
            if valor == peores[k]:
                del equiposPuntos[llave]
                break

        salida.write("%s %d\n" % (llave, valor))

    salida.close()


#7. Función que grafica los puntos
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # Ignora la primera línea
    entrada.readline()  # Ignora la segunda línea

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()

    entrada.close()
