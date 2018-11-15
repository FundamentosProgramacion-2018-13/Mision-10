#encoding: UTF-8
#Autor: Alek Fernando Howland Aguilar, A01747765
#Descripción: Misión final

import matplotlib.pyplot as plot #Importamos de libreria usamos as para cambiarlo a como lo usamos

def listarEquiposOrdenados(archivo):
    entrada = open(archivo, "r", encoding="UTF-8")

    entrada.readline()  #Saltarnops una linea que no procesamos
    entrada.readline()  #Saltarnops una linea que no procesamos

    listaEquipos= [] #Declaramos una lista vacia
    for linea in entrada:   #Leer las demas lineas que quedan
        datos = linea.split("&") #De cada linea que lee regresa una linea separada
        listaEquipos.append(datos[0].upper())   #Ingresa la primera linea que se divide y lo pasa a mayusculas
        listaEquipos.sort() #Ordena alfabeticamente


    entrada.close()

    return listaEquipos

def encontrarErrorPuntos(archivo):
    entrada = open(archivo, "r", encoding="UTF-8")

    entrada.readline()  # Saltarnops una linea que no procesamos
    entrada.readline()  # Saltarnops una linea que no procesamos

    listaEquiposError = []

    for linea in entrada:   #Leer las demas lineas que quedan
        datos = linea.split("&") #De cada linea que lee regresa una linea separada como lista
        equipo = datos[0]
        juegosGanados = int(datos[2])   #Poner int por que se lee como cadena
        juegosEmpatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntosCalculados =  juegosGanados*3 + juegosEmpatados*1 #Calculamos los puntos que gana cada equipo
        if puntosReportados != puntosCalculados:            #Condición para los equipos que sus puntos no coinciden
            listaEquiposError.append(equipo)        #Agrega a solo los que sus puntos no coinciden a una lista

    entrada.close()         #Cierra el archivo

    return listaEquiposError        #Regresa la lista con los equipos incorrectos de puntos


def graficarPuntos(archivo):
    entrada = open(archivo, "r", encoding="UTF-8")

    entrada.readline()  # Saltarnops una linea que no procesamos
    entrada.readline()  # Saltarnops una linea que no procesamos

    listaEquipos = []   #Lista que almacena los equipos
    listaPuntos = []       #Lista que almacena los puntos de cada equipo

    for linea in entrada:   #Leer las demas lineas que quedan
        datos = linea.split("&") #De cada linea que lee regresa una linea separada como lista
        listaEquipos.append(datos[0])   #Agregamos los equipos que se leen de cada linea
        listaPuntos.append(int(datos[8]))   #Agregamos los puntos en entero por que se lee como cadena

    #Graficar

    plot.plot(listaEquipos, listaPuntos)     #Primera el eje de las x que seran los equipos
                                                # Despues el  eje de las y con los puntos


    plot.show()     #Muestra lo que graficamos


def mostrarNombrePuntos(archivo):
    entrada = open(archivo, "r", encoding="UTF-8")

    entrada.readline()  # Saltarnops una linea que no procesamos
    entrada.readline()  # Saltarnops una linea que no procesamos
    equiposPuntos = {}

    for linea in entrada:   #Leer las demas lineas que quedan
        datos = linea.split("&") #De cada linea que lee regresa una linea separada como lista
        equiposPuntos[datos[0]] = int(datos[8]) # Se ingresa el nombre del diccionario y se ingresea:
                        #diccionario [llave que se añade] = int(datos[]n) se pone integro si es numero lo que se añade

    entrada.close()

    return equiposPuntos


def mostrarTresOMenos(archivo):
    entrada = open(archivo, "r", encoding="UTF-8")

    entrada.readline()  # Saltarnops una linea que no procesamos
    entrada.readline()  # Saltarnops una linea que no procesamos

    equiposPartidos = {}
    equipos = []

    for linea in entrada:   #Leer las demas lineas que quedan
        datos = linea.split("&") #De cada linea que lee regresa una linea separada como lista
        equiposPartidos[datos[0]] = int(datos[4])

    for equipo, perdidos in equiposPartidos.items():
        if perdidos <= 3:
            a = equipos, perdidos
            equipos.append(a)

    return equipos




    entrada.close()



def main():
    #equiposOrdenados = listarEquiposOrdenados("LigaMX.txt")     #Primera funcion
    #print(equiposOrdenados)
    #------------------------------------------------------------------------------
    #nombresPuntos = mostrarNombrePuntos("LigaMX.txt")           `#Segunda Función
    # print(nombresPuntos)
    #------------------------------------------------------------------------------
    tresOMenos = mostrarTresOMenos("LigaMx.txt")
    print(tresOMenos)

    #------------------------------------------------------------------------------
    #detectarError = encontrarErrorPuntos("LigaMX.txt")          #Cuarta función
    #print(detectarError)
    #-------------------------------------------------------------------------------
    #graficarPuntos("LigaMX.txt") #Septima función
    #-------------------------------------------------------------------------------



main()





