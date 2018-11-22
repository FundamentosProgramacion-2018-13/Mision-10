#Autor: Luis Armando Miranda Alcocer
# Mision 10
import matplotlib.pyplot as plot


# 1. Ordena alfabeticamente los equipos en mayúsculas
def equiposMayusculasAlfa(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    listaNombres=[]
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        mayus= linea.upper()
        datos = mayus.split("&")
        nombresEquipos= datos[0]
        listaNombres.append(nombresEquipos)

    listaNombres.sort()
    entrada.close()
    return listaNombres



# 4. Buscar equipos que tienen mal reportado el número de puntos
def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline() #Título 1 No hace nada
    entrada.readline() #Título 2 No hace nada
    for linea in entrada: #Empieza desde la tercera linea
        # linea = "Atlas&16&2&5&9&10&24&-14&11"
        datos = linea.split("&") #Separación por cada "&"   ["Atlas", "16" ...]
        equipo = datos[0]
        juegosGanados = int(datos[2])
        juegosEmpatados = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = juegosGanados*3 + juegosEmpatados*1  #CAda juego ganado aporta 3 puntos, y los empatados aporta 1
        if puntos != puntosReportados:
            equipos.append(equipo)
    entrada.close()
    return equipos #Debe ser la última linea de la función

# 7. Grafica equipos con sus respectivos puntos
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline() #Título 1 No hace nada
    entrada.readline() #Título 2 No hace nada

    listaEquipos=[]
    listaPuntos=[]

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()
    entrada.close()


def equiposConPuntos(nombreArchivo):
    entrada= open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()


def main():
    nombres= equiposMayusculasAlfa("LigaMX.txt")
    print("1. Equipos Ordenados: ", nombres)

    equipoPuntos = equiposConPuntos("LigaMX.txt")
    print("2. Equipos Ordenados: ", equipoPuntos)

    errores = buscarEquiposError("LigaMX.txt")
    print ("4. Errores: ", errores)

    graficarPuntos("LigaMX.txt")

main()