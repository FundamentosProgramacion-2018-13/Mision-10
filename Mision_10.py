#Autor: Oscar Alejandro Torres Maya
#Descripcion: Mision 10, practica de lectura de archivos

#Libreria para grafica
import matplotlib.pyplot as plot

#Muestra el nombre de los equipos
def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8") #"R" ES PARA LEER
    entrada.readline() #LEES PRIMERA LINEA
    entrada.readline() #LEES SEGUNDA LINEA

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper()) #COPIA DE DATOS EN MAYUSCULAS

    listaEquipos.sort()

    entrada.close()
    return listaEquipos


#Muestra los equipos con sus puntos
def puntosEquipos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # "R" ES PARA LEER
    entrada.readline()  # LEES PRIMERA LINEA
    entrada.readline()  # LEES SEGUNDA LINEA

    diccionario = {}

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        diccionario[equipo] = puntos

    return diccionario


#Muestra los equipos que han perdido 3 partidos o menos
def equiposPerdiendo(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # "R" ES PARA LEER
    entrada.readline()  # LEES PRIMERA LINEA
    entrada.readline()  # LEES SEGUNDA LINEA

    listaPerdidos = []

    for linea in entrada:
        datos = linea.split("&")
        perdidos = int(datos[4])
        equipo = datos[0]
        if perdidos <= 3:
            listaPerdidos.append(equipo)

    return listaPerdidos


#Muestra los equipos que tienen error en los puntos
def reportarErrorPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # "R" ES PARA LEER
    entrada.readline()  # LEES PRIMERA LINEA
    entrada.readline()  # LEES SEGUNDA LINEA

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        juegosGanados = int(datos[2])
        juegosEmpatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntosCalculados = juegosGanados*3 + juegosEmpatados*1
        if puntosReportados != puntosCalculados:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


#Muestra el equipo con menor diferencia de goles
def calcularDiferencia(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # "R" ES PARA LEER
    entrada.readline()  # LEES PRIMERA LINEA
    entrada.readline()  # LEES SEGUNDA LINEA

    diccionario = {}

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        diferencia = int(datos[7])
        diccionario[equipo] = diferencia

    llaves = diccionario.items()
    maximaDiferencia = max(llaves)
    return maximaDiferencia[0]


#Grafica los equipos vs los puntos
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # "R" ES PARA LEER
    entrada.readline()  # LEES PRIMERA LINEA
    entrada.readline()  # LEES SEGUNDA LINEA

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    #GRAFICAR
    plot.plot(listaEquipos,listaPuntos)
    plot.show()


def main():
    ordenados = (listarEquiposOrdenados("LigaMX.txt"))
    print(ordenados)
    puntos = puntosEquipos("LigaMX.txt")
    print(puntos)
    perdiendo = equiposPerdiendo("LigaMX.txt")
    print(perdiendo)
    errores = reportarErrorPuntos("LigaMX.txt")
    print(errores)
    diferencia = calcularDiferencia("LigaMX.txt")
    print(diferencia)
    graficar = graficarPuntos("LigaMX.txt")
    print(graficar)

main()