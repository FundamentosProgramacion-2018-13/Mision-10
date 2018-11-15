#Javier Alexandro Vargas Sánchez A01377718
#Misión 10
import matplotlib.pyplot as plot

def graficarPuntos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    listaEquipos = []
    listaPuntos = []
    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

#graficar
    plot.plot(listaEquipos, listaPuntos)

    plot.show()


def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos [0]
        jg = int(datos [2])  #juegos ganados
        je = int(datos [3])  #juegos empatados
        pr = int(datos [8])  #puntos reunidos
        pc = jg * 3 + je *1
        if pr != pc:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError

def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()
    entrada.close()
    return listaEquipos

def main():
    ordenados = listarEquiposOrdenados("LigaMX.txt")
    print(ordenados)
    errores = reportarErrorPuntos("LigaMX.txt")
    print(errores)
    graficarPuntos("LigaMX.txt")



main()