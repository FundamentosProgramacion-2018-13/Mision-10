# Nombre: Saúl Figueroa Conde.
# Matrícula: A01747306.
# Grupo 02.
# Descripción: Este programa presenta las soluciones a los problemas de la Mision10.
#----------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plot


# 1. Se declara la función ordenarAlfabeticamente, que recibe como parámetro el nombre del archivo de texto. Esta
# función regresa los nombre de los equipos en mayúsculas, ordenados alfabéticamente.
def ordenarAlfabeticamente(nombreArchivo):
    listaEquipos = []
    file = open(nombreArchivo, 'r', encoding='UTF-8')

    file.readline()
    file.readline()

    for line in file:
        elEquipo = line.split('&')
        listaEquipos.append(elEquipo[0].upper())

    listaEquipos.sort()

    file.close()

    return listaEquipos


# 2. Se declara la función equiposYPuntos que recibe como parámetro el nombre del archivo de texto que se va a leer.
# Esta función regresa el nombre de los equipos, seguido de los puntos que llevan hasta el momento(en un diccionario).
def equiposYPuntos(nombreArchivo):
    diccionarioEquipos = {}
    file = open(nombreArchivo, 'r', encoding='UTF-8')

    file.readline()
    file.readline()

    for line in file:
        dato = line.split('&')
        diccionarioEquipos['{}'.format(dato[0])] = ('{}'.format(int(dato[8])))

    file.close()

    return diccionarioEquipos


# 3. Se declara la función determinarDerrotas, que recibe como parámetro el nombre del archivo que se va a leer. Esta
# función regresa una lista con el nombre de los equipos solicitados por este problema.
def determinarDerrotas(nombreArchivo):
    listaEquipos = []
    file = open(nombreArchivo, 'r', encoding='UTF-8')

    file.readline()
    file.readline()

    for line in file:
        dato = line.split('&')
        if int(dato[4]) <= 3:
            listaEquipos.append(dato[0])

    file.close()

    return listaEquipos


# 4. Se declara la función buscarEquiposError que recibe como parámetro el nombre del archivo de texto que se lee.
# La función se encarga de buscar los equipos que tienen mal reportado el número de puntos. Regresa una lista.
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, 'r', encoding='UTF-8')

    equipos = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        # linea = Veracruz&16&2&4&10&16&36&-20&10
        datos = linea.split('&') # 'Veracruz' '16' ...
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg*3 + je*1

        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos


# 5. Se declara la función buscarDiferenciaGoles, que recibe como parámetro el nombre del archivo que lee la función.
# La función regresa una cadena con el nombre del equipo con menor diferencia de goles.
def buscarDiferenciaGoles(nombreArchivo):
    entrada = open(nombreArchivo, 'r', encoding='UTF-8')
    listaGoles = []
    listaTeams = []
    listaTeams2 = []

    equipos = []
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos = linea.split('&')
        listaTeams.append(datos[0])
        listaTeams2.append(abs(int(datos[7])))
        listaGoles.append(abs(int(datos[7])))

    listaGoles.sort()
    resultado = int(listaGoles[0])
    resultadoEquipo = ''
    n = len(listaTeams)

    for i in range(0, n):
        if resultado == listaTeams2[i]:
            resultadoEquipo = listaTeams[i]

    entrada.close()
    return resultadoEquipo


# 6. Se declara la función generarArchivo, que recibe como parámetro el nombre del archivo que se leera. Esta función
# genera un nuevo archivo 'Puntos.txt' que contiene el nombre y los puntos de los equipos que se encuentran en los
# últimos 5 lugares de la tabla de acuerdo con el archivo.
def generarArchivo(nombreArchivo):
    listaEquipos = []
    listaPuntos = []
    listaMenoresPuntajes = []
    listaPuntosCopy = []
    diccionarioResultados = {}

    file = open(nombreArchivo, 'r')

    file.readline()
    file.readline()

    for linea in file:
        dato = linea.split('&')
        listaEquipos.append(dato[0])
        listaPuntos.append(int(dato[8]))

    listaPuntosCopy = listaPuntos.copy()
    listaPuntosCopy.sort()

    for i in range(0, 5):
        listaMenoresPuntajes.append(listaPuntosCopy[i])

    m = len(listaEquipos)
    q = len(listaMenoresPuntajes)
    listaDebbugJ = []
    listaIndicadorZ = []

    for j in range(0, m):
        for z in range(0, q):
            if listaPuntos[j] == int(listaMenoresPuntajes[z]):
                diccionarioResultados['{}'.format(listaEquipos[j])] = '{}'.format(listaPuntos[j])
                listaIndicadorZ.append(listaMenoresPuntajes[z])
                listaMenoresPuntajes[z] = -1
                listaDebbugJ.append(j)

    s = len(listaDebbugJ)
    if len(diccionarioResultados) < 5:
        for again in range(0, s):
            diccionarioResultados['{}'.format(listaEquipos[again])] = '{}'.format(listaIndicadorZ[again])

    file.close()

    endFile = open('Puntos.txt', 'w')

    for equipoMenor in diccionarioResultados:
        endFile.write('{},{}\n'.format(equipoMenor, diccionarioResultados[equipoMenor]))

    endFile.close()


# 7. Se declara la función graficarPuntos, que recibe como parámetro el nombre del archivo de texto que se va a leer.
# Esta función muestra una gráfica de equipos vs. puntos de acuerdo con el archivo. No regresa nada.
def graficarPuntos(archivoEntrada):
    entrada = open(archivoEntrada, 'r')

    entrada.readline()
    entrada.readline()

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split('&')
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()

    entrada.close()


# Se declara la función main que se encarga de probar la solución a cada problema.
def main():
    print("Ejercicio 1: ")
    orden = ordenarAlfabeticamente('LigaMX.txt')
    print(orden)
    print('')
    print("Ejercicio 2: ")
    puntos = equiposYPuntos('LigaMX.txt')
    print(puntos)
    print('')
    print("Ejercicio 3: ")
    derrotas = determinarDerrotas('LigaMX.txt')
    print(derrotas)
    print('')
    print("Ejercicio 4: ")
    errores = buscarEquiposError('LigaMX.txt')
    print(errores)
    print('')
    print("Ejercicio 5: ")
    goles = buscarDiferenciaGoles('LigaMX.txt')
    print(goles)
    print('')
    print("Ejercicio 6 [el archivo ha sido generado]: ")
    generarArchivo('LigaMX.txt')
    print('')
    print("Ejercicio 7 [se ha dibujado la gráfica]: ")
    graficarPuntos('LigaMX.txt')
    print('')
    print("Gracias por haber usado el programa.")


# Se llama a la función main para que empiece a correr el programa.
main()