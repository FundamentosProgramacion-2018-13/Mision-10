# Jose Luis Mata Lomelí
# Mision 10: Liga MX

#Librería
import matplotlib.pyplot as plot


# Problema 1: Mostrar los nombres de los equipos en mayusculas y ordenados alfabeticamente (Lista)
def mostrarMayusculas(nombreArchivo):

    #Abrir Archivo
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    lista = []  #Lista vacia

    #Leer datos inecesarios
    entrada.readline()
    entrada.readline()

    #Para cada linea en el documento
    for linea in entrada:

        #Cambiar "&" por una coma
        dato = linea.split("&")

        # El nombre de los equipos son la posicion de los datos en MAYUSCULAS
        equipos = dato[0].upper()

        # Agregar a la lista vacia los equipos del documento en mayuscula
        lista.append(equipos)

    #Cerrar Archivo
    entrada.close()

    #Ordenar la lista de manera Alfabetica
    return (sorted(lista))


# Problema 2: Mostrar el nombre de los equipos seguido de de los puntos que llevan hasta el momento (lista de duplas o diccionario)
def mostrarEquipoPuntos():

    #Diccionario
    duplas = {"Atlas":11, "Veracruz":10, "Necaxa":14,"LobosBUAP":16,"Tijuana":16, "Guadalajara":20 , "León":18 , "Puebla":19 , "Pachuca":23 , "Querétaro":23 , "Morelia":25 , "Tigres":24 , "América":30 , "Montererrey":27 , "Pumas UNAM":29 , "Santos":29 , "Toluca":26 , "Cruz Azul":33 }
    return duplas

# Problema 3: Mostrar la lista de los euipos que han perdido 3 partidos o menos (lista)
def partidosPerdidos(nombreArchivo):

    #Abrir Archivo
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equipos = []    #Lista vacía

    #Ignorar las primeras lineas
    entrada.readline()  #Titulo 1
    entrada.readline()  #Titulo 2

    #Para cada linea en el archivo
    for linea in entrada:

        #Cambiar "&" por una coma
        datos = linea.split("&")

        #Posicion de los datos a usar
        equipo = datos[0]
        pperdidos = int(datos[4])

        # Si la cantidad de partidos perdidos es menor o igual a 3
        if pperdidos <= 3:
            #Agrega el nombre del equipo a la lista vacia
            equipos.append(equipo)

    #Cerrar Archivo
    entrada.close()

    #Regresa la lista con los nombres del equipo
    return equipos


# Problema 4: Buscar en el archivo los nombres de los equipos que tienen mal reportado la cantidad de puntos
def buscarEquiposError(nombreArchivo):

    #Abrir archivo en modo lectura
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    equipos = []    #Lista vacia

    entrada.readline()  #Titulo 1
    entrada.readline()  #Titulo 2

    #Para visitar cada linea del archivo
    for linea in entrada:

        #Para que separe los datos para sacar el & por comas...
        datos = linea.split("&")    #Lista modificada de cada equipo

        # Posicion de los datos buscados
        equipo = datos[0]
        jganados = int(datos[2])
        jempatados = int(datos[3])
        puntosReportados = int(datos[8])

        #Calculo
        puntos = jganados*3 + jempatados*1

        #Si los puntos calculados NO son los puntos reportados...
        if puntos != puntosReportados:
            equipos.append(equipo)  #Agregarlo a la lista vacia

    #Cerrar archivo
    entrada.close()

    #Regresar la lista
    return equipos

# Problema 5: Mostrar el nombre del equipo con la menor diferencia de goles (cadena)
def diferenciaGoleo(nombreArchivo):

    #Abrir archivo en modo lectura
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    lista = []    #Lista vacia

    entrada.readline()  #Titulo 1
    entrada.readline()  #Titulo 2

    #Para visitar cada linea del archivo
    for linea in entrada:

        #Para que separe los datos para sacar el & por comas...
        datos = linea.split("&")    #Lista modificada de cada equipo

        #Posicion de los datos:
        equipo = datos[0]
        g_favor = int(datos[5])
        g_contra = int(datos[6])

        #Calcular la diferencia de goles
        diferencia = g_favor - g_contra

        #Si la diferencia es igual a 0
        if diferencia == 0:
            #Añadir a la lista
            lista.append(equipo)
        else:   #Sino

            #Si la diferencia es menor a 1 y mayor a -1
            if diferencia <= 1 and diferencia >= -1:
                lista.append(equipo) #Agregar a la lista

    #Cerrar archivo
    entrada.close()

    #Cerrar lista
    return lista


# Problema 6: Generar un nuevo archivo que contenga los nombres y los puntos de los equipos que se encuentran en los ultimos 5 lugares de la tabla (solo archivo nuevo)

#Problema 7: Graficar Datos de la Ligua (grafica)
def graficarPuntos(nombreArchivo):

    # Abrir archivo en modo lectura
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    #No me interesa leer...
    entrada.readline()  # Titulo 1: Ligua BBVA Bancomer
    entrada.readline()  # Titulo 2: Equipo, Puntos, ...

    # x = lista de Equipo
    # y = lista de Puntos
    listaEquipo = []
    listaPuntos = []


    # Para visitar cada linea del archivo
    for linea in entrada:

        # Cambiar & por una coma
        datos = linea.split("&")

        #Agregar los datos para cada lista vacía
        listaEquipo.append(datos[0])
        listaPuntos.append(int(datos[8]))

    #Graficar y mostrar
    plot.plot(listaEquipo, listaPuntos)
    plot.show()

    #Cerrar Archivo
    entrada.close()

##################################################################################

def main():

    #1
    print("1ra Parte")
    print(mostrarMayusculas("LigaMX"))

    # 2
    print("2da Parte")
    equipos_y_puntos = mostrarEquipoPuntos()
    print(equipos_y_puntos)

    #3
    print("3ra Parte")
    equipos_pperdidos = partidosPerdidos("LigaMX")
    print(equipos_pperdidos)

    #4
    print("4ta Parte")
    errores = buscarEquiposError("LigaMX")
    print(errores)

    #5
    print("5to Parte")
    diferencia = diferenciaGoleo("LigaMx")
    print(diferencia)

    #6

    #7
    print("7ma Parte")
    graficarPuntos("LigaMX")

main()