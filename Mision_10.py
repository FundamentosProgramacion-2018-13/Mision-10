import matplotlib.pyplot as plot


#La funcion equiposOrdenar se encarga de hacer una lista con los nombres de os equipos en
def equiposOrdenar(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline()
    entrada.readline()
    for linea in entrada:
        datos = linea.split("&")
        nombre = datos[0].upper()
        equipos.append(nombre)
        equipos.sort()
    entrada.close()
    return equipos


#La funcion equiposInfo se encarga de regresar una lista con los datos de puntos y nombre del equipo.
def equiposInfo(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    dupla = []
    entrada.readline()
    entrada.readline()
    for linea in entrada:
        datos = linea.split("&")
        nombre = datos[0]
        puntos = int(datos[8])
        datos = (nombre,puntos)
        dupla.append(datos)


    entrada.close()
    return dupla



def equiposPartidosPerdidos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline()
    entrada.readline()
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        perdidos = int(datos[4])
        if perdidos <= 3:
            equipos.append(equipo)
    entrada.close()
    return equipos


def buscarEquiposError(nombreArchivo):
    entrada = open(nombreArchivo,"r",encoding="UTF-8")
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

def menorDiferencia(nombreArchivo):
    entrada = open(nombreArchivo, 'r', encoding='UTF-8')
    entrada.readline()
    entrada.readline()
    equipoDiferencia = []
    menor = 0
    for linea in entrada:
        datos = linea.split("&")
        goles = int(datos[7])
        equipo = datos[0]
        if menor > goles:
            menor = goles
            equipoDiferencia = equipo
    entrada.close()
    return equipoDiferencia

def generarArchivo(nombreArchivo):

    pass

def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    listaEquipos = []
    listaPuntos = []
    entrada.readline()
    entrada.readline()
    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))
    plot.plot(listaEquipos,listaPuntos)
    plot.grid(True, linestyle='--')
    plot.tick_params(labelcolor='b', labelsize='medium', width=3)
    plot.show()
    entrada.close()


def main():
    print(equiposPartidosPerdidos("LigaMX.txt"))
    print(menorDiferencia("LigaMX.txt"))


main()

