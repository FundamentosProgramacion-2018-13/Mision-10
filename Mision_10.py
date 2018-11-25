# Danhel Alejandro Mercado Velasco
# mision 10 equipos de football
# liga BBVA
import matplotlib.pyplot as plot


# Mostrar el nombre de los equipos ordenadamente
def listarEquiposOrdenados(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()
    listaEquipos = []
    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())
    listaEquipos.sort()
    entrada.close()
    return listaEquipos

# Mostrar lista de equipos que han perdido 3 partidos o menos
def listarEquiposPerdedores(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    lista = []
    for datos in entrada:
        fila = datos.split("&")
        Perdidas = int(fila[4])
        if Perdidas <= 3:
            lista.append(fila[0].upper())
    entrada.close()
    return lista


# Mostrar a los equipos con sus respectivos puntos
def listarEquiposPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()
    entrada.readline()
    listaPuntaje = []
    for linea in entrada:
        datos = linea.split("&")
        puntos = int(datos[8])
        equipos = datos[0].upper()
        dupla = equipos, puntos
        listaPuntaje.append(dupla)
    entrada.close()
    return listaPuntaje

# Motrar equipos con mala puntaución
def listarEquiposMalRepostados(nombreArchivo):
    entrada = open(nombreArchivo, "r")

    entrada.readline()
    entrada.readline()

    listaEquiposPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = (datos[0])
        jg = int(datos[2])
        je = int(datos[3])
        pr = int(datos[8])
        pc = jg * 3 + je * 1
        if pr != pc:
            listaEquiposPuntos.append(equipo)
    entrada.close()
    return listaEquiposPuntos

# Muestra grafica con respecto al archivo
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