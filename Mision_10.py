#Alberto Contreras Torres
#Mision 10

import matplotlib.pyplot as plot


# 5. Mostrar el nombre del equipo con la menor diferencia de goles. (regresa una cadena)  VERACRUZ
def menorDiferenciaGoles(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()

    contador = 0
    for linea in entrada:
        datos = linea.split("&")
        diferenciaGoleo = int(datos[7])
        equipos = datos[0].upper




    entrada.close()



# 2. Mostrar nombre de los equipos segudio de los puntos
def puntajeEquipos(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()  # Consumir linea 1
    entrada.readline()  # Consumir linea 2

    listaPuntaje = []

    for linea in entrada:
        datos = linea.split("&")
        puntos = int(datos[8])
        equipos = datos[0].upper()
        dupla = equipos, puntos
        listaPuntaje.append(dupla)

    entrada.close()
    return listaPuntaje

# 3. Mostrar lista de equipos que han perdido 3 partidos o menos
def equiposPerdedores(nombre):  #America, UNAM, Santos, Cruz Azul
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()  # Consumir linea 1
    entrada.readline()  # Consumir linea 2

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        equipos = datos[0]
        juegosPerdidos = int(datos[4])
        if juegosPerdidos <=  3:
            listaEquipos.append(equipos)

    entrada.close()
    return listaEquipos



# 4. Nombre de equipos con puntuación mal reportadas
def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r", encoding = "UTF-8")
    entrada.readline()  # Consumir linea 1
    entrada.readline()  # Consumir linea 2

    listaEquiposError = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos [0]
        jG = int (datos[2])
        jE = int (datos[3])
        pR = int (datos[8])
        pC = jG * 3 + jE * 1
        if pR != pC:
            listaEquiposError.append(equipo)

    entrada.close()

    return listaEquiposError


# 1. Nombre de equipos en mayusculas
def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding = "UTF-8")
    entrada.readline()   #Consumir linea 1
    entrada.readline()   #Consumir linea 2

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")   #Regresa linea con datos separados en cadenas
        listaEquipos.append(datos[0].upper())  # CONVIERTE A MAYUSCULAS LA FUNCIÓN

    listaEquipos.sort()  #ordenar alfabeticamente los equipos


    entrada.close()

    return listaEquipos


# 7. Muestra gráficas de equipos vs puntos de acuerdo con el archivo
def graficar(nombre):
    entrada = open(nombre, "r", encoding="UTF-8")
    entrada.readline()  # Consumir linea 1
    entrada.readline()  # Consumir linea 2

    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    #GRAFICAR
    plot.plot(listaEquipos, listaPuntos)

    plot.show()
    entrada.close()

def main():
    ordenados = listarEquiposOrdenados("ligaMX.txt")
    print(ordenados)

    print('-------------------------------------------------------------')

    errores = reportarErrorPuntos("ligaMX.txt")
    print(errores)

    print('-------------------------------------------------------------')

    grafica = graficar("ligaMX.txt")
    print(grafica)

    print('-------------------------------------------------------------')

    puntos = puntajeEquipos("ligaMX.txt")
    print(puntos)

    print('-------------------------------------------------------------')

    equiposP = equiposPerdedores("ligaMX.txt")
    print(equiposP)

    print('-------------------------------------------------------------')

    menor = menorDiferenciaGoles("ligaMX.txt")
    print(menor)

main()