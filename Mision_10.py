# Autor: Oscar Macias Rodríguez, A01376398
# Descripción: Ejercicios con archivos y listas.


import matplotlib.pyplot as plot


# 1. Mostrar los nombre de los equipos en mayúsculas ordenados alfabéticamente.
def ordenarNombresAlfabeticamente(nombrearchivo):
    entrada = open(nombrearchivo, "r", encoding="UTF-8")

    equipos = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        equipo = equipo.upper()
        equipos.append(equipo)

    equipos.sort()
    entrada.close()

    return equipos


# 2. Regresa el nombre de los equipos seguido de los puntos que llevan hasta el momento según el archivo.
def mostrarNombreYPuntos(nombrearchivo):
    entrada = open(nombrearchivo, "r", encoding="UTF-8")

    duplas = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        duplas.append("(")
        duplas.append(equipo)
        duplas.append(",")
        duplas.append(str(puntos))
        duplas.append("), ")

    wds = duplas
    glue = ""
    cadena = glue.join(wds)
    nuevaLista = [cadena]

    entrada.close()
    return nuevaLista


# 3. Muestra la lista de equipos que han perdido tres partidos o menos.
def mostrarEquiposPerdidos(nombrearchivo):
    entrada = open(nombrearchivo, "r", encoding="UTF-8")

    lista = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        perdidos = int(datos[4])

        if perdidos <= 3:
            lista.append(equipo)

    entrada.close()
    return lista


# 4. Buscar los equipos que tienen mal reportado el número de puntos.
def buscarEquiposError(nombrearchivo):
    entrada = open(nombrearchivo, "r", encoding="UTF-8")

    equipos = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg*3 + je*1
        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos


# 5. Mostrar el nombre del equipo con la menor diferencia de goles.
def mostrarEquipoMenorDiferencia(nombrearchivo):
    entrada = open(nombrearchivo, "r", encoding="UTF-8")

    lista = []
    nuevaLista = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        diferencia = int(datos[7])
        lista.append(diferencia)

        if diferencia == min(lista):
            nuevaLista.append(equipo)

    nuevaLista = nuevaLista[1]
    wds = nuevaLista
    x = str(min(lista))
    cadena = wds + ", " + x

    entrada.close()

    return cadena


# 6. Genera un nuevo archivo que contiene los nombres de los 5 equipos con los puntos más bajos.
def generarArchivo(nombrearchivo):
    entrada = open(nombrearchivo, "r", encoding="UTF-8")
    salida = open("Puntos.txt", "w")

    lista = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equipos = datos[0]
        puntos = int(datos[8])

        if puntos < 17:
            lista.append(equipos)
            lista.append(",")
            lista.append(str(puntos))
            lista.append("\n")

    wds = lista
    glue = ""
    cadena = glue.join(wds)

    salida.write(cadena)
    entrada.close()
    salida.close()


# 7. Muestra una gráfica de equipos vs. puntos de acuerdo con el archivo.txt.
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()
    entrada.readline()

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()

    entrada.close()


# Función principal donde se prueban las funciones anteriores.
def main():
    x = ordenarNombresAlfabeticamente("LigaMX.txt")
    print(x)

    y = mostrarNombreYPuntos("LigaMX.txt")
    print(y)

    z = mostrarEquiposPerdidos("LigaMX.txt")
    print(z)

    errores = buscarEquiposError("LigaMX.txt")
    print(errores)

    a = mostrarEquipoMenorDiferencia("LigaMX.txt")
    print(a)

    b = generarArchivo("LigaMX.txt")
    print(b)

    graficarPuntos("LigaMX.txt")

main()