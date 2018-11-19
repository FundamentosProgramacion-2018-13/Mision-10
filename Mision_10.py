# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripción: Misión final

import matplotlib.pyplot as plot


def listarEquiposOrdenados(tabla):
    Equipos = []
    for linea in tabla:
        datos = linea.split("&")
        Equipos.append(datos[0].upper())
        Equipos.sort()
    return Equipos


def mostrarNombrePuntos(tabla):
    equiposPuntos = []
    for linea in tabla:
        datos = linea.split("&")
        equiposPuntos.append((datos[0], int(datos[8])))
    return equiposPuntos


def mostrarTresOMenos(tabla):
    equipos = []
    for linea in tabla:
        datos = linea.split("&")
        if int(datos[4]) <= 3:
            equipos.append(datos[0])
    return equipos


def encontrarErrorPuntos(tabla):
    equipos = []
    for linea in tabla:
        datos = linea.split("&")
        puntosCalculados = (int(datos[2])*3) + int(datos[3])
        if int(datos[8]) != puntosCalculados:
            equipos.append(datos[0])
    return equipos


def menorDiferenciaGoles(tabla):
    menorDiferencia, Equipo = 1000, ""
    for linea in tabla:
        datos = linea.split("&")
        if abs(int(datos[7])) < menorDiferencia:
            menorDiferencia, Equipo = int(datos[7]), datos[0]
    return Equipo


def nuevoArchivo(tabla):
    archivo = open("Puntos.txt", "w", encoding="UTF-8")
    menosPuntos = []
    for linea in tabla:
        datos = linea.split("&")
        if len(menosPuntos) < 5:
            menosPuntos.append((datos[0], int(datos[8])))
        else:
            nombre, puntos = datos[0], int(datos[8])
            for equipo in menosPuntos:
                nom, pun = equipo
                if puntos < pun:
                    menosPuntos.remove(equipo)
                    menosPuntos.append((nombre, puntos))
                    break
    for n in menosPuntos:
        archivo.write(str(n) + "\n")
    archivo.close()


def graficarPuntos(tabla):
    Datos = []
    for linea in tabla:
        datos = linea.split("&")
        Datos.append((datos[0], datos[8]))

    plot.plot(Datos)
    plot.show()


def main():
    archivo = open("LigaMX.txt", "r", encoding="UTF-8")
    archivo.readline()
    archivo.readline()
    tabla = []
    for linea in archivo:
        tabla.append(linea)
    archivo.close()
    print(listarEquiposOrdenados(tabla))
    print(mostrarNombrePuntos(tabla))
    print(mostrarTresOMenos(tabla))
    print(encontrarErrorPuntos(tabla))
    print("Menor diferencia: " + menorDiferenciaGoles(tabla))
    nuevoArchivo(tabla)
    graficarPuntos(tabla)


main()
