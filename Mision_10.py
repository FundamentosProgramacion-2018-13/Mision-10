# Autor: Alex Serrano Durán
# Descripción: Este programa desempeña una variedad de funciones con base en una base de datos de la Liga MX
# Comentario extra: Arriba la Máquina

import matplotlib.pyplot as plot

# 1. Regresa una lista de los equipos ordenados alfabéticamente y en mayúsculas
def ordenarAlfabetico(nombreArchivo):
    entrada = open(nombreArchivo)
    equiposOrdenados = []

    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        equiposOrdenados.append(datos[0].upper())

    equiposOrdenados.sort()

    entrada.close()

    return equiposOrdenados


# 2. Crea una lista con tuplas que incluyen el nombre del equipo junto con los puntos obtenidos en el torneo
def mostrarEquiposPuntos(nombreArchivo):
    entrada = open(nombreArchivo)
    listaTuplas = []

    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        tupla = (datos[0], int(datos[8]))
        listaTuplas.append(tupla)

    entrada.close()

    return listaTuplas


# 3. Crea una lista con los equipos que han perdido menos de 3 partidos
def mostrarMenosPerdedores(nombreArchivo):
    entrada = open(nombreArchivo)
    listaMenosPerdedores = []

    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split("&")
        if int(datos[4]) < 3:                                # Revisa si el número de perdidos es menor a 3
            listaMenosPerdedores.append(datos[0])       # Si hay menos de 3 derrotas, agrega el equipo a la lista

    entrada.close()

    return listaMenosPerdedores


# 4. Buscar los equipos que tienen mal reportado los puntos obtenidos
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo)
    equipos = []

    entrada.readline()      # lee y desecha la primer línea
    entrada.readline()      # lee y desecha la segunda línea

    for linea in entrada:
        datos = linea.split("&")

        equipo = datos[0]
        ganados = int(datos[2])
        empatados = int(datos[3])
        puntosReportados = int(datos[8])

        puntosReales = ganados*3 + empatados
        if puntosReales != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos


# 5. Muestra el equipo con la menor diferencia de goles.
def mostrarMenorDiferencia(nombreArchivo):
    entrada = open(nombreArchivo)

    entrada.readline()
    entrada.readline()

    diccionarioEquipos = {}
    listaDiferencias = []

    for linea in entrada:
        datos = linea.split("&")
        diccionarioEquipos[datos[0]] = int(datos[7])                # Llena el diccionario con equipo + diferencia
        listaDiferencias.append(int(datos[7]))                      # Hace una lista con solo las diferencias

    listaDiferencias.sort()
    diferenciaMenor = listaDiferencias[0]                           # Ordena la lista de diferencias y guarda la menor

    for equipo, diferencia in diccionarioEquipos.items():       # Visita todos los valores del diccionario y regresa el
        if diferencia == diferenciaMenor:                       # equipo asociado a la menor diferencia
            entrada.close()
            return equipo

# Comentario: En este ejercicio no supe bien a lo que se refería con "menor"; si al equipo con la peor diferencia o
# al equipo con la diferencia absoluta más cercana a 0 (o 0). Decidí hacerlo con la definición futbolística de que la
# menor diferencia es la del equipo que peor le ha ido.


# 6. Crea un nuevo archivo con los últimos 5 lugares de la tabla así como sus puntos obtenidos.

def crearArchivoPeores(nombreArchivo):
    entrada = open(nombreArchivo)

    entrada.readline()
    entrada.readline()

    diccionarioEquipos = {}
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        diccionarioEquipos[datos[0]] = int(datos[8])
        listaPuntos.append(int(datos[8]))


    listaPuntos.sort()
    listaMenoresPuntos = listaPuntos[:5]


    for dato in listaMenoresPuntos:                     # Remueve duplicados para no escribir un equipo dos veces
        while listaMenoresPuntos.count(dato) >= 2:
            listaMenoresPuntos.remove(dato)


    salida = open("Puntos.txt", "w")                    # Escritura
    for equipo, puntos in diccionarioEquipos.items():
        for dato in listaMenoresPuntos:
            if puntos == dato:
                salida.write(equipo)
                salida.write(" ")
                salida.write(str(puntos))
                salida.write("\n")

    entrada.close()
    salida.close()


# 7. Grafica los puntos obtenidos por cada equipo.
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")

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
