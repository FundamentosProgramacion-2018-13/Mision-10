# Autor: Ivan Honc Ayón
# Descripción: Diferentes funciones que utilizan listas y diccionarios para realizar tareas.


def buscarEquiposError(liga):
    entrada = open(liga, "r", encoding="UTF-8")

    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        # linea = "Veracruz&16&2&4&10&16&36&-20&10"
        datos = linea.split("&")  # ["Veracruz", "16", ...]
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosReportados = int(datos[8])
        puntos = jg*3 + je*1
        if puntos != puntosReportados:
            equipos.append(equipo)

    entrada.close()

    return equipos


def graficarPuntos(liga):
    entrada = open(liga, "r", encoding="UTF-8")


def ordenarAlfabeticamente(liga):
    entrada = open(liga, "r", encoding="UTF-8")

    equiposAlfabeticamente = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    for linea in entrada:
        # linea = "Veracruz&16&2&4&10&16&36&-20&10"
        datos = linea.split("&")  # ["Veracruz", "16", ...]
        equipo = datos[0]
        equiposAlfabeticamente.append(equipo)
    equiposAlfabeticamente = sorted(equiposAlfabeticamente)

    entrada.close()

    return equiposAlfabeticamente


def mostrarEquiposYPuntos(liga):
    entrada = open(liga, "r", encoding="UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    puntajeEquipos = []
    for linea in entrada:
        datos = linea.split("&")
        puntajeEquipos.append((datos[0], int(datos[8])))

    entrada.close()

    return puntajeEquipos


def mostrarEquiposTresPerdidos(liga):
    entrada = open(liga, "r", encoding="UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    equiposTresPerdidos = []
    for linea in entrada:
        datos = linea.split("&")
        if int(datos[4]) <= 3:
            equiposTresPerdidos.append(datos[0])

    entrada.close()

    return equiposTresPerdidos


def mostrarEquipoMenorDiferenciaGoles(liga):
    entrada = open(liga, "r", encoding="UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    equipoMenorDiferenciaGoles = 200
    for linea in entrada:
        datos = linea.split("&")
        if int(datos[7]) < equipoMenorDiferenciaGoles:
            strEquipoMenorDiferenciaGoles = datos[0]

    entrada.close()

    return strEquipoMenorDiferenciaGoles


def crearArchivoUltimosequipos(liga):
    pass


def main():
    equiposAlfabeticamente = ordenarAlfabeticamente("LigaMX.txt")  # Función 1
    print(equiposAlfabeticamente)

    equiposPuntos = mostrarEquiposYPuntos("LigaMx.txt")  # Función 2
    print(equiposPuntos)

    equiposTresPerdidos = mostrarEquiposTresPerdidos("LigaMX.txt")  # Función 3
    print("Equipos con tres partidos perdidos o menos: ", equiposTresPerdidos)

    errores = buscarEquiposError("LigaMX.txt")  # Función 4
    print("Equipos con errores en su puntaje: ", errores)

    equipoMenorDiferenciaGoles = mostrarEquipoMenorDiferenciaGoles("LigaMX.txt")
    print("Equipo con menor diferencia de goles:", equipoMenorDiferenciaGoles)

    ultimosEquipos = crearArchivoUltimosequipos("LigaMX.txt")

    graficarPuntos("LigaMX.txt")  # Función 7

    
main()

