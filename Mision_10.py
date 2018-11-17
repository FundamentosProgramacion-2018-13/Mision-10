#Autora: Mariana Caballero Cabrera  A01376544

# Programa que abre un archivo y extrae información de ese mismo


import matplotlib.pyplot as plot

def listarEquiposOrdenados (nombreArchivo):
    entrada = open (nombreArchivo,"r",encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    listaEquipos = []

    for linea in entrada:     # con esto proceso todas las demás lineas
        datos =linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    entrada.close()
    return listaEquipos


def reportarPuntosError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        ganados = int(datos[2])
        empatados = int(datos[3])
        puntosReportados = int (datos [8])
        puntosCalculados = (ganados*3)+(empatados*1)
        if puntosReportados!=puntosCalculados:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError


def grafica (nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        listaEquipos.append(equipo)
        listaPuntos.append(puntos)
    entrada.close()

    plot.plot(listaEquipos, listaPuntos)
    plot.title("Liga MX")
    plot.xlabel("Equipos")
    plot.ylabel("Puntos")

    plot.show()  # es necesario para que se muestre la gráfica


def puntosMostrar (nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    lista = []
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        lista.append(equipo.upper())
        lista.append(puntos)
    entrada.close()

    return lista

def equiposMenosPerdedores(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    lista = []
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        perdidos = int(datos[4])
        if perdidos<=3:
            lista.append(equipo)
    entrada.close()
    return lista

def peorEquipo (nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    diccionario= {}
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        diferencia = int(datos[7])
        diccionario[diferencia]=equipo
    listaPuntos = [diccionario.keys()]
    listaPuntos.sort()
    menorDiferencia = diccionario[0]
    equipoDiferencia = diccionario[menorDiferencia]

    return equipoDiferencia



    entrada.close()



def nuevoArchivo (nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    salida = open("Puntos.txt", "w")  # la "w" funciona como write
    entrada.readline()
    entrada.readline()
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])



    entrada.close()
    salida.close()


def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print(ordenados)

    error= reportarPuntosError("LigaMX.txt")
    print(error)

    puntos = puntosMostrar("LigaMX.txt")
    print(puntos)

    perdidos = equiposMenosPerdedores("LigaMX.txt")
    print(perdidos)

    equipo = peorEquipo("LigaMX.txt")
    print (equipo)


main()