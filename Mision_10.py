#Autor: Arturo Márquez Olivar. A01376086.
#Completa las funciones solicitadas en la misión 10.

import matplotlib.pyplot as plot

#1. Muestra los nombres de los equipos en mayúsculas alfabéticamente.
def ordenaAlfabeticamente(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # Desecha la línea 1.
    entrada.readline()  # Desecha la línea 2.

    equipos = []

    for linea in entrada:
        equipo = linea.split("&")
        equipos.append(equipo[0])
    entrada.close()

    for letras in range(len(equipos)):
        pass
    return equipos


#2. Muestra el nombre de los equipos y a lado muestra su puntaje actual.
def mostrarPuntajes(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Desecha la línea 1.
    entrada.readline()  # Desecha la línea 2.
    diccionario = {}

    for linea in entrada:
        datos = linea.split("&")
        diccionario[datos[0]] = int(datos[8])
    entrada.close()
    return diccionario


#3. Regresa una lista de los equipos que han perdido 3 partidos o menos.
def partidosPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Desecha la línea 1.
    entrada.readline()  # Desecha la línea 2.
    diccionario = {}
    equipos = []

    for linea in entrada:
        datos = linea.split("&")
        diccionario[datos[0]] = int(datos[4])
    entrada.close()
    for llave, valor in diccionario.items():
        if valor <= 3:
            equipos.append(llave)
    return equipos


#4. Buscar equipos con error de puntos.
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding = "UTF-8")
    equipos = [] #Lista donde se van a introducir los equipos que tengan error.

    entrada.readline() #Desecha la línea 1.
    entrada.readline() #Desecha la línea 2.

    for linea in entrada:
        #Línea = "Atlas&16&2&5&9&10&24&-14&11"
        datos = linea.split("&") #Mete a una lista cada palabra individual en cada índice.
        equipo = datos[0]
        ganados = int(datos[2])
        empatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = ganados*3 + empatados*1
        if puntos != puntosReportados:
            equipos.append(equipo)
    entrada.close()
    return str(equipos)


#5. Regresa el equipo con la menor diferencia de goleo.
def menorGoleo(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()
    entrada.readline()

    diccionario = {}

    for linea in entrada:
        datos = linea.split("&")
        diccionario[datos[0]] = int(datos[7])
    entrada.close()

    listaValores = []
    for valor in diccionario.values():
        listaValores.append(valor)
    menor = min(listaValores)

    for llave, valor in diccionario.items():
        if valor == menor:
            return str(llave)


#6. Genera un nuevo archivo que contiene el nombre y puntaje de los últimos 5 equipos del archivo leído.
def mostrarUltimosCinco(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    salida = open("Puntos.txt", "w", encoding = "UTF-8")
    for datosInutiles in range(1, 16):
        datosInutiles = entrada.readline()

    diccionario = {}
    for linea in entrada:
        datos = linea.split("&")
        diccionario[datos[0]] = int(datos[8])
    salida.write("Ejercicio 6.\nLos últimos 5 equipos del archivo y sus respectivas puntuaciones.\n")
    for llaves, datos in diccionario.items():
        salida.write("%s: %s\n" %(str(llaves), str(datos)))
    entrada.close()
    salida.close()


#7. Grafica los puntos obtenidos de los equipos.
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


#Función principal, llama a las otras funciones e imprime los datos.
def main():
    print("Ejercicio 1.")
    equipos = ordenaAlfabeticamente("LigaMX.txt")
    print(equipos)

    print("\nEjercicio 2.")
    print("En esta parte podemos ver los equipos, seguido de sus puntuaciones hasta el momento.")
    print(mostrarPuntajes("LigaMx.txt"))

    print("\nEjercicio 3.")
    print("Los equipos que han perdido 3 partidos o menos son: ", partidosPerdidos("LigaMx.txt"))

    print("\nEjercicio 4.")
    errores = buscarEquiposError("LigaMX.txt")
    print("Los equipos que tuvieron error en su puntaje fueron: ", errores)

    print("\nEjercicio 5.")
    menorGol = menorGoleo("LigaMX.txt")
    print("El equipo con menor diferencia de goleo es: ", menorGol)

    #Ejercicio 6.
    mostrarUltimosCinco("LigaMx.txt")

    #Ejercicio 7.
    graficarPuntos("LigaMX.txt")


#Llamada a la función principal.
main()