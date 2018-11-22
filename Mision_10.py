#Autor: Víctor Manuel Rodríguez Loyola
#Misión 10

import matplotlib.pyplot as plot

def mostrarNombresaAlfaMayusculas(): #Ordena los nombres de los equipos alfabéticamente y los coloca en mayúsculas
    entrada= open("LigaMX.txt", "r", encoding="UTF-8")
    equipos=[]
    entrada.readline() #Ignorar las primeras líneas del documento
    entrada.readline()
    for linea in entrada:
        separacion=linea.split("&")
        equipos.append(separacion[0].upper())
    entrada.close()
    equipos.sort() #Ordenar los nombres de los equipos
    return equipos


def mostrarEquiposyPuntos(): #Muestra sólo los nombres de los equipos y sus correspondientes puntos
    puntos= {}
    entrada = open("LigaMX.txt", "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    for lineas in entrada:
        linea=lineas[:-1]
        separacion = linea.split("&")
        puntos[separacion[0]]=separacion[len(separacion)-1]
    entrada.close()
    return puntos


def mostrarPartidosPerdidos(): #Devuelve sólo los nombres de los equipos que han perdido 3 partidos o menos
    equiposPerdido3= []
    entrada = open("LigaMX.txt", "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    for lineas in entrada:
        separacion= lineas.split("&")
        perdidos= int(separacion[4])
        if perdidos<=3:
            equiposPerdido3.append(separacion[0])
    entrada.close()
    return equiposPerdido3


def encontrarErroresPuntos(): #Devuelve los nombres de los equipos que tienen un error en el cálculo de sus puntos
    equiposConError= []
    entrada = open("LigaMX.txt", "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    for lineas in entrada:
        separacion = lineas.split("&")
        ganados= int(separacion[2])*3
        empatados= int(separacion[3])
        puntos= int(separacion[8])
        if ganados+empatados!=puntos:
            equiposConError.append(separacion[0])

    entrada.close()
    return equiposConError


def mostrarMenorDiferenciaGoleo(): #Devuelve el nombre del equipo que tiene una menor diferencia de goles
    equipo=""
    equipoMenorDiferencia=0
    entrada = open("LigaMX.txt", "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    for lineas in entrada:
        separacion = lineas.split("&")
        diferencia= int(separacion[7])
        if diferencia< equipoMenorDiferencia:
            equipoMenorDiferencia= diferencia
            equipo= separacion[0]

    entrada.close()
    return equipo

def mostrarUltimosLugares(): #Devuelve los nombres de los últimos 5 equipos y sus puntos
    entrada = open("LigaMX.txt", "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    lugares = 1
    salida = open("Puntos.txt", "w", encoding="UTF-8")
    for lineas in entrada:
        separacion = lineas.split("&")
        while lugares <13:
            entrada.readline()
            lugares+=1
        salida.writelines("%s,%s"%(separacion[0],separacion[8]))
    entrada.close()
    salida.close()

def graficarEquiposPuntos(): #Hace una gráfica de equipos vs puntos de acuerdo al archivo
    entrada = open("LigaMX.txt", "r", encoding="UTF-8")
    equipos= []
    puntos= []
    entrada.readline()
    entrada.readline()
    for lineas in entrada:
        separacion = lineas.split("&")
        equipos.append(separacion[0])
        puntos.append(separacion[8])
    plot.plot(equipos, puntos)
    plot.title("Liga BBVA Bancomer")
    plot.xlabel("Equipos")
    plot.ylabel("Puntos")
    plot.show()
    entrada.close()




