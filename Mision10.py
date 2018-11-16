#Jesus Zabdiel Sánchez Chávez

#Mison10
import matplotlib.pyplot as plot


def nombresEquipos(nombreArchivo):
    archivo = open(nombreArchivo , "r")
    archivo.readline()
    archivo.readline()

    listaEquipos = []
    for linea in archivo:

        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()



    archivo.close()
    return listaEquipos

def puntosIncorrectos(nombreArchivo):
    archivo = open(nombreArchivo, "r")

    archivo.readline()
    archivo.readline()

    equiposIncorrectos = []

    for linea in archivo:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntos = int(datos[8])
        puntosReales = jg*3 + je

        if puntos != puntosReales:
            equiposIncorrectos.append(equipo)


    archivo.close()

    return equiposIncorrectos

def graficarPuntos (nombreArchivo):

    archivo = open(nombreArchivo, "r")

    archivo.readline()
    archivo.readline()

    listaPuntos = []
    listaEquipos = []

    for linea in archivo:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(datos[8])
    archivo.close()


    plot.plot(listaEquipos, listaPuntos)

    plot.show()


def puntosEquipos(nombreArchivo):

    archivo = open(nombreArchivo, "r")
    archivo.readline()
    archivo.readline()

    equiposPuntos = {}

    for linea in archivo:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int (datos [8])

        equiposPuntos[equipo] = puntos

    archivo.close()

    return equiposPuntos

def masDe3Perdiddos(nombreArchivo):

    archivo = open(nombreArchivo, "r")

    archivo.readline()
    archivo.readline()
    listaPerdedores = []

    for linea in archivo:
        datos = linea.split("&")
        if int(datos[4]) <=3:
            listaPerdedores.append(datos[0])
    archivo.close()
    return listaPerdedores

def diferenciaGoles(nombreArchivo):

    archivo = open(nombreArchivo, "r")

    archivo.readline()
    archivo.readline()

    diferenciaGoles = {}

    for linea in archivo:
        datos = linea.split("&")
        diferenciaGoles[datos[0]] = int(datos[7])

    goles = 0
    for x in diferenciaGoles.keys():
        if int (diferenciaGoles[x]) <= goles:
            goles = diferenciaGoles[x]
            equipo = x

    archivo.close()

    return equipo


def ultimosLugares(nombreArchivo):

    archivo = open(nombreArchivo, "r")
    puntos = open("Puntos.txt" , "w")

    archivo.readline()
    archivo.readline()

    posiciones = {}
    tablaPuntos= []

    for linea in archivo:
        datos = linea.split("&")
        posiciones[datos[0]] =int(datos[8])
        tablaPuntos.append(int(datos[8]))

    tablaPuntos.sort()
    ultimos = tablaPuntos[:5:]
    perdedores = []

    totalEquipos = 0
    for key, value in posiciones.items():
        if totalEquipos < 5:
            if value in ultimos:
                ultimo = key, value
                perdedores.append(ultimo)
                totalEquipos += 1
                puntos.write("%s \n" % str(ultimo))

    archivo.close()
    puntos.close()







def  main():
    listaEquipos = nombresEquipos("LigaMX.txt")
    print (listaEquipos)

    equiposIncorrectos = puntosIncorrectos("LigaMX.txt")
    print (equiposIncorrectos)

    graficarPuntos("LigaMX.txt")

    print (puntosEquipos("LigaMX.txt"))

    print (masDe3Perdiddos("LigaMX.txt"))

    print (diferenciaGoles("LigaMX.txt"))

    ultimosLugares("LigaMX.txt")








main()