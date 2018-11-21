# encoding = UTF-8
# Autor: Silvia Ferman
# Mision 10

import matplotlib.pyplot as plot          # libreria para graficar


# Funcion que muestra los nombres de los equipos en mayuscula y orden alfabetico
def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()                      # titulo
    entrada.readline()                      # titulo

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()
    entrada.close()
    return listaEquipos


# Funcion que muestra el equipo y sus puntos que llevan hasta el momento
def mostrarEquiposPuntos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()                     # titulo
    entrada.readline()                     # titulo

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaEquipos.append(int(datos[8]))

    entrada.close()
    return listaEquipos


# Funcion que muestra los equipos que han perdido 3 o menos partidos
def mostrarEquiposPerdedores(nombre):
    entrada = open(nombre, "r")
    entrada.readline()                     # titulo
    entrada.readline()                     # titulo

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        perdidos = int(datos[4])
        if perdidos <= 3:
            listaEquipos.append(equipo)

    entrada.close()
    return listaEquipos


# Funcion que muestra los nombres de los equipos que tienen ERROR en su puntaje
def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()                    # titulo
    entrada.readline()                    # titulo

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jganados = int(datos[2])
        jempatados = int(datos[3])
        puntos = int(datos[8])             # los puntos que se reportaron
        pcalculados = jganados * 3 + jempatados * 1
        if puntos != pcalculados:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


# Funcion que muestra al equipo con la menor diferencia de goles
def mostrarDiferenciaGoles(nombre):
    entrada = open(nombre, "r")
    entrada.readline()                     # titulo
    entrada.readline()                     # titulo

    listaGoles = []

    for linea in entrada:
        datos = linea.split("&")
        listaGoles[datos[0]] = int(datos[7]) 

     for valor in listaGoles.items():    
         if diferencia > valor:     
             diferencia = valor    
    
    for equipo, goles in listaGoles.items():
        if diferencia == goles
            resultado = equipo
            
    entrada.close()
    return resultado


# Funcion que muestra una grafica EQUIPOS vs. PUNTOS (solo la dibuja, NO regresa datos)
def graficarPuntos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()
    entrada.readline()

    listaEquipos= []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    # graficar
    plot.plot(listaEquipos, listaPuntos)

    plot.title("Equipos vs. Puntos")
    plot.xlabel("EQUIPOS")
    plot.ylabel("PUNTOS")

    plot.show()


def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print(ordenados)
    puntaje = mostrarEquiposPuntos("LigaMX.txt")
    print(puntaje)
    perdedores = mostrarEquiposPerdedores("LigaMX.txt")
    print(perdedores)
    errores = reportarErrorPuntos("LigaMX.txt")
    print(errores)
    goles = mostrarDiferenciaGoles("LigaMX.txt")
    print(goles)
    graficar = graficarPuntos("LigaMX.txt")
    print(graficar)





main()
