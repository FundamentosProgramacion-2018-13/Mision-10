# Carlos Alberto Reyes Ortiz
#A01376349

import matplotlib.pyplot as plot


def listarEquiposOrdenados(nombreArchivo):

    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    return  listaEquipos

    entrada.close()



def reportarErrorPuntos(nombreArchivo):

    entrada = open(nombreArchivo, "r")
    entrada.readline()   #Son los titulos, no los queremos
    entrada.readline()

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        pr = int(datos[8])
        pc = jg*3 + je

        if pr != pc:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError



def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()  # Son los titulos, no los queremos
    entrada.readline()

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[10])
        listaPuntos.append(int(datos[8]))

        plot.plot(listaEquipos,listaPuntos)

        plot.show()




def main():
    ordenados = listarEquiposOrdenados("ligaMX.txt")
    print(ordenados)



main()
