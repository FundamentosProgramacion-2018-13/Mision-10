# Autor: Luis Humberto Burgueño Paz
# Ejercicios con Archivos

import matplotlib.pyplot as plot


# Ordena los equipos por nombre alfabéticamente
def ordenarEquipos(nombreArchivo):
   entrada = open(nombreArchivo, "r")
   equipos = []
   entrada.readline()  # Título 1
   entrada.readline()  # Título 2
   for linea in entrada:
       # linea: 'Veracruz&16&2&4&10&16&36&-20&10'
       datos = linea.split("&")  # ["Veracruz", "16", ...]
       equipo = datos[0]
       equipos.append(equipo)
   equipos.sort()
   entrada.close()
   return equipos


# Regresa un diccionario con cada equipo y sus respectivos puntos
def regresarPuntosEquipos(nombreArchivo):
   entrada = open(nombreArchivo, "r")
   equipos = []
   puntos = []
   puntosEquipos = {}
   entrada.readline()  # Título 1
   entrada.readline()  # Título 2
   for linea in entrada:
       # linea: 'Veracruz&16&2&4&10&16&36&-20&10'
       datos = linea.split("&")  # ["Veracruz", "16", ...]
       equipo = datos[0]
       punto = int(datos[8])
       equipos.append(equipo)
       puntos.append(punto)
   for x in range(len(equipos)):
       puntosEquipos[equipos[x]] = puntos[x]
   entrada.close()
   return puntosEquipos


# Regresa una lista con los equipos que han perdido tres o menos partidos.
def mostrarPerdidosTres(nombreArchivo):
   entrada = open(nombreArchivo, "r")
   equipos = []
   entrada.readline()  # Título 1
   entrada.readline()  # Título 2
   for linea in entrada:
       # linea: 'Veracruz&16&2&4&10&16&36&-20&10'
       datos = linea.split("&")  # ["Veracruz", "16", ...]
       equipo = datos[0]
       juegosPerdidos = int(datos[4])
       if juegosPerdidos <= 3:
           equipos.append(equipo)
   entrada.close()
   return equipos


# Regresa una lista con los equipos que tienen suma de puntos incorrecta.
def buscarEquiposError(nombreArchivo):
   entrada = open(nombreArchivo, "r")
   equipos = []
   entrada.readline()  # Título 1
   entrada.readline()  # Título 2
   for linea in entrada:
       # linea: 'Veracruz&16&2&4&10&16&36&-20&10'
       datos = linea.split("&") # ["Veracruz", "16", ...]
       equipo= datos[0]
       juegosGanados = int(datos[2])
       juegosEmpatados = int(datos[3])
       puntosReportados = int(datos[8])
       puntos = juegosGanados*3 + juegosEmpatados*1
       if puntos != puntosReportados:
           equipos.append(equipo)

   entrada.close()

   return equipos

# Muestra el equipo con la menor diferencia de goles.
def mostrarMenorDiferencia(nombreArchivo):
   entrada = open(nombreArchivo, "r")
   diferenciasGoles = {}
   entrada.readline()  # Título 1
   entrada.readline()  # Título 2
   for linea in entrada:
       # linea: 'Veracruz&16&2&4&10&16&36&-20&10'
       datos = linea.split("&")  # ["Veracruz", "16", ...]
       equipo = datos[0]
       diferenciaGoles = int(datos[-2])
       diferenciasGoles[diferenciaGoles] = equipo
   menorDiferencia = min(diferenciasGoles.keys())
   if menorDiferencia in diferenciasGoles:
    entrada.close()
    return diferenciasGoles[menorDiferencia]


# Genera un archivo que contiene los equipos con la menor cantidad de puntos junto con su puntaje.
def generarArchivosPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    salida = open("Puntos.txt", "w")
    equipos = []
    puntos = []
    puntosEquipos = {}
    menosPuntos = {}
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2
    for linea in entrada:
        # linea: 'Veracruz&16&2&4&10&16&36&-20&10'
        datos = linea.split("&")  # ["Veracruz", "16", ...]
        equipo = datos[0]
        punto = int(datos[8])
        equipos.append(equipo)
        puntos.append(punto)
    for x in range(len(equipos)):
        puntosEquipos[puntos[x]] = equipos[x]
    for x in range(5):
        menoresPuntos = min(puntosEquipos.keys())
        equiposMenores = puntosEquipos[menoresPuntos]
        menosPuntos[equiposMenores] = menoresPuntos
        del puntosEquipos[menoresPuntos]
    for llave in menosPuntos:
        salida.write("%s,%d\n" % (llave, menosPuntos[llave]))
    entrada.close()
    salida.close()





# Realiza una gráfica de los puntos de los equipos.
def graficarPuntos(nombreArchivo):
   entrada = open(nombreArchivo, "r")
   entrada.readline()  # Título 1
   entrada.readline()  # Título 2

   listaEquipos = []
   listaPuntos = []

   for linea in entrada:
       datos = linea.split("&")
       listaEquipos.append(datos[0])
       listaPuntos.append(int(datos[8]))

   plot.plot(listaEquipos, listaPuntos)
   plot.show()

   entrada.close()


# Función Rpincipal. Llama a las otras funciones.
def main():
   equiposOrdenados = ordenarEquipos("LigaMX.txt")
   print(equiposOrdenados)
   puntosEquipos = regresarPuntosEquipos("LigaMX.txt")
   print(puntosEquipos)
   equiposPerdidoTres = mostrarPerdidosTres("LigaMX.txt")
   print(equiposPerdidoTres)
   errores = buscarEquiposError("LigaMX.txt")
   print(errores)
   menorDiferencia = mostrarMenorDiferencia("LigaMX.txt")
   print(menorDiferencia)
   generarArchivosPuntos("LigaMX.txt")
   graficarPuntos("LigaMX.txt")


main()

