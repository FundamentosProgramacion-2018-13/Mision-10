# Luis Jonathan Rosas Ramos A01377942
# Mision 10
# Analisis de un texto, con pyhton

import matplotlib.pyplot as plot

#Mostrar nombres de los equipos en mayusuculas y ordenados
def listarEquiposOrdenados(nombreArchivo): #mandar el archivo
    entrada = open(nombreArchivo,"r") #Leer el archivo mandado en lectura
    entrada.readline()  #Elminar linea uno
    entrada.readline()  #Eliminar linea dos
    listaEquipos = []   #Generar una lista para guardar los equipos
    for linea in entrada:   #Checar cada linea
        datos = linea.split("&")    #visitar los datos con la separacion "$"
        listaEquipos.append(datos[0].upper()) #meter a la lista todos los equipos (indice 0 de la lista), todos en mayusuclas
    listaEquipos.sort() #Ordenar la lista
    entrada.close() #Cerrar el archivo
    return listaEquipos

#Mostrar nombres de los equipos y puntos obtenidos
def nombresYpuntos(nombreArchivo):
    entrada = open(nombreArchivo,"r")
    entrada.readline()
    entrada.readline()
    listaEquipo = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        puntos = int(datos[8])
        listaEquipo.append(equipo)
        listaEquipo.append(puntos)
    entrada.close()
    return listaEquipo

#mostrar equipos que han perdido tres o menos
def equiposJuegosPerdidos(nombreArchivo):
    entrada =open(nombreArchivo,"r")
    entrada.readline()
    entrada.readline()
    equiposPerdiendo = []
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        juegosPerdidos = int(datos[4])
        if juegosPerdidos <= 3:
            equiposPerdiendo.append(equipo)
    entrada.close()
    return equiposPerdiendo

#mostrar equipos con puntos mal reportados
def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r")  # Leer el archivo mandado en lectura
    entrada.readline()  # Elminar linea uno
    entrada.readline()  # Eliminar linea dos
    listaEquiposError = []  # Generar una lista para guardar los equipos con error

    for linea in entrada:  # Checar cada linea
        datos = linea.split("&")  # visitar los datos con la separacion "$"
        equipo = datos[0]
        jg = int(datos[2]) #en el archivo se lee el dato, no la cadena
        je =int(datos[3])
        pr = int(datos[8])
        pc = jg*3 + je
        if pr != pc:
            listaEquiposError.append((equipo))

    entrada.close() #Cerrar archivo
    return listaEquiposError

#Mostar el equipo con la menor diferencia de goles
def menorDiferencia(nombre):
    entrada = open(nombre,"r")
    entrada.readline()
    entrada.readline()
    listaPeorEquipo = []

    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        diferenciaGoles = int(datos[7])
        acumulador = 0
        if acumulador >= diferenciaGoles:
            acumulador = diferenciaGoles
            listaPeorEquipo.appned(equipo)
    entrada.close()
    return listaPeorEquipo

def graficarPuntos(nombre):
    entrada = open(nombre,"r")
    entrada.readline()
    entrada.readline()
    listaEquipos = []
    listaPuntos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    #graficar
    plot.plot(listaEquipos,listaPuntos)
    plot.show()


def main():
    ordenados = listarEquiposOrdenados("LigaMx.txt")
    print(ordenados)
    equipoYerrores = nombresYpuntos("LigaMx.txt")
    print(equipoYerrores)
    equiposPerdiendo = equiposJuegosPerdidos("LigaMx.txt")
    print(equiposPerdiendo)
    errores = reportarErrorPuntos("LigaMx.txt")
    print(errores)
    peorEquipo = menorDiferencia("LigaMx.text")
    print(peorEquipo)
    graficarPuntos("LigaMx.txt")

main()
