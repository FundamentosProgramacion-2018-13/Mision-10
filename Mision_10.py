# Autor: Jonathan Sanabria Rocha
# Descripcion : Completas los objetivos de la mision 10


import matplotlib.pyplot as plot


def listarEquipos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline() #no hace caso a las dos primeras lineas
    equipos = []
    for linea in entrada:
        letras = linea.split("&")
        equipos.append(letras[0].upper())
    equipos.sort()
    entrada.close()
    return equipos


def listarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    lista = []
    for linea in entrada:
        datos = linea.split("&")
        for linea in range(1, 4):
            juegos = int(datos[linea])
            lista.append(juegos)
    return lista



def juegosPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()  # No toma las dos primeras lineas
    listaEquipos = []
    informacion = {}
    for linea in entrada:
        juegos = linea.split("&")
        informacion[juegos[0]] = int(juegos[4])
    entrada.close()
    for numero, valor in informacion.items():
        if valor <= 3:
            listaEquipos.append(numero)
    return listaEquipos


def reportarError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline() #No tomas las dos primeras lineas
    lista = []
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        juegosGanados = int(datos[2])
        juegosEmpatados = int(datos[3])
        puntosRegistrados = int(datos[8])
        puntosObtenidos = juegosGanados*3 + juegosEmpatados
        if puntosRegistrados != puntosObtenidos:
            lista.append(equipo)
    entrada.close()
    return lista


def calcularDiferenciaGoles(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()  # No toma las dos primeras lineas
    diccionario = {}

    for linea in entrada:
        goles = linea.split("&")
        equipo = goles[0]
        diferencia = int(goles[7])
        diccionario[equipo] = diferencia
    valor = diccionario.items()
    maxDif = max(valor)
    return maxDif[0]


def mostrarCinco(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    salida = open("Puntos.txt", "w", encoding = "UTF-8")
    for datosNs in range(1, 16):
        datosNs = entrada.readline()
    diccionario = {}
    for linea in entrada:
        valores = linea.split("&")
        diccionario[valores[0]] = int(valores[8])
    salida.write("Los últimos 5 equipos son: \n")
    for equipo, puntos in diccionario.items():
        salida.write("%s: %s\n" %(str(equipo), str(puntos)))
    entrada.close()
    salida.close()


def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    lista = []
    listaPuntos = []
    for linea in entrada:
        valores = linea.split("&")
        lista.append(valores[0])
        listaPuntos.append(int(valores[8]))
    plot.plot(lista,listaPuntos)
    plot.show()



def main():
    print("1.")
    alfabeticamente = listarEquipos("LigaMX.txt")
    print(alfabeticamente)
    print("2.")
    puntos = listarPuntos("LigaMX.txt")
    print(puntos)
    print("3.")
    perdidos = juegosPerdidos("LigaMX.txt")
    print(perdidos)
    print("4.")
    error = reportarError("LigaMX.txt")
    print(error)
    print("5.")
    diferencia = calcularDiferenciaGoles("LigaMX.txt")
    print(diferencia)
    mostrarCinco("LigaMX.txt")
    graficarPuntos("LigaMx.txt")

    
main()




