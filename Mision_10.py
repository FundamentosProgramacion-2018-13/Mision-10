#Sebastian Macias Ibarra - A01376492
#Msion 10

#librerias
import matplotlib.pyplot as plot

#1. Muestra los nombres de los equipos en mayúsculas ordenados alfabeticamente
def ordenarNombresAlfabeticamente(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    listaNombres = []

    entrada.readline()  # Título 1
    entrada.readline()  # Título 2
    for linea in entrada:
        #linea = 'Necaxa&16&3&5&8&19&28&-9&14'
        datos = linea.split("&")  # ['Necaxa', '16', ...]
        nombresEquipo = datos[0]
        nombresEquipo = str.upper(nombresEquipo)
        listaNombres.append(nombresEquipo)
        listaNombres.sort()

    entrada.close()

    return listaNombres


#2.Regresa un diccionario con los nombres y los puntos actuales
def crearRelacionNombresYPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    listaNombresPuntos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        # linea = 'Necaxa&16&3&5&8&19&28&-9&14'
        datos = linea.split("&")
        nombreEquipo = datos[0]
        puntos = int(datos[8])
        listaNombresPuntos.append((nombreEquipo, puntos))

    entrada.close()

    return listaNombresPuntos


#3.Regresa una lista que contiene los equipos con 3 o menos partidos perdidos
def mostrarEquipos_MenosPartidosPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    listaEquipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        datos = linea.split("&")
        nombreEquipo = datos[0]
        jPerdidos = int(datos[4])

        if jPerdidos <= 3:
            listaEquipos.append(nombreEquipo)

    entrada.close()

    return listaEquipos

#4. Buscar en el archivo, quipos que tienen mal reportada su cantidad de puntos
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equipos = []
    entrada.readline()  #Título 1
    entrada.readline()  #Título 2

    #Realizamos un ciclo para visitar lso datos del archivo
    for linea in entrada:
        #linea = 'Necaxa&16&3&5&8&19&28&-9&14'
        datos = linea.split("&")  # ['Necaxa', '16', ...]
        nombreEquipo = datos[0]
        jGanados = int(datos[2])
        jEmpatados = int(datos[3])
        ptsReportados = int(datos[8])

        puntos = jGanados * 3 + jEmpatados  #Se multiplican los puntos de los partidos ganado por la cantidad y  luego se le suman los puntos de los juegos cempatados
        if puntos != ptsReportados:
            equipos.append(nombreEquipo)

    entrada.close()

    return equipos

'''Corregir'''
#5. Mostrar equipo con menor diferencia de goles
def mostrarEquipoMenorDiferenciaGoles(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    menorDiferencia = 1000
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        datos= linea.split("&")
        nombreEquipo = datos[0]
        diferencia = int(datos[7])
        if diferencia < 0:
            diferencia = diferencia * -1     #Cambiamos el valor a positivo, haciendo más sencilla la comparación

        if diferencia < menorDiferencia :
            menorDiferencia = diferencia
            equipo = nombreEquipo

    entrada.close()

    return equipo

'Incompleto'
#6. Genera un nuevo documento
def generarArchivoNuevo(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    salida = open("Puntos.txt" ,"w")

    listaEquipos = []
    listaUltimos = []

    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        datos = linea.split("&")
        nombreEquipo = datos[0]
        puntos = int(datos[8])
        listaEquipos.append((nombreEquipo, puntos))

    for valor in listaEquipos:
        menor = min(listaEquipos)
        if len(listaUltimos) < 5:
            listaUltimos.append(menor)
            listaEquipos.remove(menor)

    print(listaUltimos)



    listaUltimos.append(min(listaEquipos))


    entrada.close()
    salida.close()

#7. crea una gráfica de los equipos vs puntos
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos,listaPuntos)
    plot.show()


def main():
    #1.
    nombres = ordenarNombresAlfabeticamente("LigaMX.txt")
    print(nombres)

    #2.
    lista = crearRelacionNombresYPuntos("LigaMX.txt")
    print(lista)

    #3.
    listaEquipos =  mostrarEquipos_MenosPartidosPerdidos("LigaMX.txt")
    print(listaEquipos)

    #4.
    errores = buscarEquiposError("LigaMX.txt")
    print(errores)

    #5.
    diferencia = mostrarEquipoMenorDiferenciaGoles("LigaMX.txt")
    print(diferencia)


    #6.
    archivo = generarArchivoNuevo("LigaMX.txt")


    #7.
    graficarPuntos("LigaMX.txt")

main()