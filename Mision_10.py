# Francisco Ariel Arenas Enciso
# A01369122
# Desarrollo de la misión (abrir y manipular archivos)

import matplotlib.pyplot as plot

'''
Ejercicio 1. Nombre de los equipos en mayusculas y ordenados alfabéticamente
'''
def ordenarEquipos(nombreArchivo):
    archivo = open(nombreArchivo, "r", encoding="UTF-8")

    nombres = []
    archivo.readline()
    archivo.readline()

    for linea in archivo:
        datos = linea.upper()
        datos = datos.split("&")
        nombresLista = datos[0]
        nombres.append(nombresLista)
        nombres.sort()

    archivo.close()

    return (nombres)


'''
Ejericio 2. Nombres de los equipos seguidos de sus puntos
'''
def encontrarEquipos():
    archivo = open("LigaMX.txt", "r", encoding="UTF-8")

    archivo.readline()
    archivo.readline()

    for linea in archivo:
        linea = linea.rstrip()
        lista = linea.split("&")
        lista = lista[0:9:8]

        print(lista)

    archivo.close()

'''
Ejercicio 3. Lista de los equipos que han perdido 3 partidos o menos
'''
def listaPerdedores():
    archivo = open("LigaMX.txt", "r", encoding="UTF-8")
    global nuevalista
    archivo.readline()
    archivo.readline()

    for linea in archivo:
        linea = linea.rstrip()
        lista = linea.split("&")
        lista = lista[0:4]
        if int(lista[3]) <= 3:
            nuevalista = []
            nuevalista.append(lista[0])
            return(nuevalista)

    archivo.close()
    return (nuevalista)


'''
Ejercicio 4. Buscar los equipos que tienen mal reportado el número de puntos
'''
def buscarEquiposError(nombreArchivo):
    archivo = open(nombreArchivo, "r", encoding="UTF-8")  # Se abre archivo en modo lectura

    equipos = []  # Se crea una lista vacía donde se almacenarán los equipos
    archivo.readline()  # Desecha el primer titulo (linea)
    archivo.readline()  # Desecha el segundo titulo (linea)

    for linea in archivo:  # Se visitan las lineas después de haber leído las dos lineas
        datos = linea.split("&")  # Se crea una lista para cada linea. Se pasa "&" para que sea el separador
        equipo = datos[0]
        juegosGanados = int(datos[2])  # Cantidad de juegos ganados
        juegosEmpatados = int(datos[3])  # Cantidad de juegos perdidos
        puntosReportados = int(datos[8])  # Cantidad de puntos según el archivo

        puntos = juegosGanados * 3 + juegosEmpatados * 1  # Se calculan los puntos de acuerdo a los datos del archivo

        if puntos != puntosReportados:  # Se comparan los puntos calculados con los del archivo
            equipos.append(equipo)  # Se añade a la lista el nombre del equipo que encontramos

    archivo.close()  # Se cierra el archivo

    return equipos  # Regresa la lista de los equipos


'''
Ejercicio 5. Equipo con la menor diferencia
'''
def encontrarMenorDiferencia():
    archivo = open("LigaMX.txt", "r", encoding="UTF-8")  # Se abre archivo en modo lectura
    global goles
    global equipo
    archivo.readline()  # Desecha el primer titulo (linea)
    archivo.readline()  # Desecha el segundo titulo (linea)


    diccionario = {}

    for linea in archivo:
        linea = linea.rstrip()
        lista = linea.split("&")
        diccionario[lista[0]] = lista[7]
    for valor in diccionario.values():
        if valor >= str(-1) and valor <= str(0):
            goles = valor
        for nombre, diferencia in diccionario.items():
            if goles == diferencia:
                equipo = nombre

    archivo.close()

    return (equipo)


'''
Ejercicio 6. Generar nuevo archivo (Puntos.txt) con nombre y los equipos en los últimos cinco lugares
del archivo
'''
def generarArchivo():
    pass
    ### DUDAS ###


'''
Ejercicio 7. Gráfica de puntos 
'''
def graficarPuntos(nombreArchivo):
    archivo = open(nombreArchivo, "r", encoding="UTF-8")  # Se abre archivo en modo lectura

    archivo.readline()  # Desecha el primer titulo (linea)
    archivo.readline()  # Desecha el segundo titulo (linea)

    listaEquipos = []  # Se crea una lista vacía de equipos (parámetro x)
    listaPuntos = []  # Se crea una lista vacía de puntos (parámetro y)

    for linea in archivo:  # Se visitan las lineas después de haber leído las dos lineas
        datos = linea.split("&")
        listaEquipos.append(datos[0])  # Se agregan los nombres de los qeuipos de la lista de datos
        listaPuntos.append(int(datos[8]))  # Se agregan los valores NÚMERICOS de la lista de datos a la de puntos

    plot.plot(listaEquipos, listaPuntos)  # Se crea la gráfica con los parámetros correspondientes (x, y)
    plot.show()  # Se muestra la gráfica creada

    archivo.close()  # Se cierra el archivo


'''
Función main()
'''
def main():
    print('''
    Misión 10. Abrir y manipular archivos 
    Francisco Ariel Arenas Enciso
    A01369122
    ------------------------------------------
    Primer ejercicio:
    ''')
    ejercicioUno = ordenarEquipos("LigaMX.txt")
    print(ejercicioUno)
    print('''
    ------------------------------------------
    Segundo ejercicio: 
    ''')
    encontrarEquipos()
    print('''
    ------------------------------------------
    Tercer ejercicio: 
    ''')
    listaPerdedores()
    print('''
    ------------------------------------------
    Cuarto ejercicio: 
    ''')
    ejercicioCuatro = buscarEquiposError("LigaMX.txt")
    print(ejercicioCuatro)
    print('''
    ------------------------------------------
    Quinto ejercicio: 
    ''')
    ejercicioCinco = encontrarMenorDiferencia()
    print(ejercicioCinco)
    print('''
    ------------------------------------------
    Sexto ejercicio: 
    ''')
    #ejercicioSeis = generarArchivo()
    #print(ejercicioSeis)
    print('''
    Tuve dudas :(
    
    ------------------------------------------
    Séptimo ejercicio: 
    ''')
    ejercicioSiete = graficarPuntos("LigaMX.txt")
    print(ejercicioSiete)
    print('''
    ------------------------------------------
    ''')


main()