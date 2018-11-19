# Rubén Villalpando Bremont
# Misión 10

import matplotlib.pyplot as plt

def ordenarNombres(entrada):
    archivo = open(entrada, "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    nuevaLista = []
    for datos in archivo:
        fila = datos.split("&")
        nuevaLista.append(fila[0])
    nuevaLista.sort()
    archivo.close()
    return nuevaLista


def mostrarPuntos(entrada):
    archivo = open(entrada, "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    nuevaLista = []
    for datos in archivo:
        fila = datos.split("&")
        nuevaLista.append((fila[0], int(fila[8])))
    archivo.close()
    return nuevaLista


def mostrarEquiposPerdidos(entrada):
    archivo = open(entrada, "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    nuevaLista = []
    for datos in archivo:
        fila = datos.split("&")
        Perdidas = int(fila[4])
        if Perdidas <= 3:
            nuevaLista.append(fila[0])
    archivo.close()
    return nuevaLista


def encontrarMalReportados(entrada):
    archivo = open(entrada, "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    malReportados = []
    for datos in archivo:
        fila = datos.split("&")
        ganadas = int(fila[2])
        empatadas = int(fila[3])
        puntos = ganadas*3 + empatadas
        if puntos != int(fila[8]):
            malReportados.append(fila[0])
    archivo.close()
    return malReportados


def equipoMenorDiferencia(entrada):
    archivo = open(entrada, "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    menorDiferencia = 100000000000000
    equipoConMenor = ""
    for datos in archivo:
        fila = datos.split("&")
        difGoles = abs(int(fila[7]))
        if difGoles < menorDiferencia:
            equipoConMenor = fila[0]
            menorDiferencia = difGoles
    archivo.close()
    return equipoConMenor


def crearArchivo(entrada):
    archivo = open(entrada, "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    cosasAEscribir = []
    lugares = []
    for datos in archivo:
        fila = datos.split("&")
        lugares.append((fila[0], int(fila[8])))
    lugares.sort(key=lambda  tup:tup[1])
    for x in range(5):
        cosasAEscribir.append(lugares[x][0] + " " + str(lugares[x][1]) + "\n")
    newFile = open("Puntos.txt", "w")

    for x in cosasAEscribir:
        newFile.write(x)
    archivo.close()
    newFile.close()



def graficarPuntos(entrada):
    archivo = open(entrada, "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    puntos =  []
    equipos = []
    for datos in archivo:
        fila = datos.split("&")
        equipo = fila[0]
        punto = fila[8]
        puntos.append(int(punto))
        equipos.append(equipo)
    print(equipos)
    print(puntos)
    plt.plot(equipos, puntos)
    plt.show()



def main():
    entrada = "LigaMX.txt"
    print(ordenarNombres(entrada))
    print(mostrarPuntos(entrada))
    print(mostrarEquiposPerdidos(entrada))
    print(encontrarMalReportados(entrada))
    print(equipoMenorDiferencia(entrada))
    crearArchivo(entrada)
    graficarPuntos(entrada)


main()