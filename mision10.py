import matplotlib.pyplot as plot

#4
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equipos=[]
    entrada.readline()#titulo
    entrada.readline() #titulo2

    for linea in entrada:
        datos =linea.split("&")#se separan
        equipo =datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg*3+je*1
        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos


def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # titulo
    entrada.readline()  # titulo2
    listaEquipos =[]
    listaPuntos =[]

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos,listaPuntos)
    plot.show()
    entrada.close()


def ordenarEquipos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # titulo
    entrada.readline()  # titulo2
    listaOrdenada = []

    for linea in entrada:
        datos = linea.split("&")
        listaOrdenada.append(datos[0].upper())
        listaOrdenada.sort()

    entrada.close()
    return listaOrdenada

def puntosEquipos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # titulo
    entrada.readline()  # titulo2
    listaPuntos = ()
    for linea in entrada:
        datos = linea.split("&")



def main():
    errores=buscarEquiposError("LigaMX.txt")
    print(errores)
    graficarPuntos("LigaMX.txt")
    print(ordenarEquipos("LigaMX.txt"))