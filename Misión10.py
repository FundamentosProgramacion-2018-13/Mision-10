#Autor: Diana Marisol Medina Bravo

import matplotlib.pyplot as plot

def listarEquiposOrdenados(nombreArchivo):
    entrada=open(nombreArchivo,"r")
    entrada.readline()
    entrada.readline()

    listaEquipos=[]

    for linea in entrada:
        datos=linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    entrada.close()

    return listaEquipos

def reportarErrorPuntos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()  #Titulo 1
    entrada.readline()  #Titulo 2

    listaEquiposError = []

    for linea in entrada:
        datos=linea.split("&")
        equipo=datos[0]
        jg=int(datos[2])
        je=int(datos[3])
        pr=int(datos[8])
        pc= jg*3 + je*1

        if pr!=pc:
            listaEquiposError.append(equipo)

    entrada.close()
    return listaEquiposError

def reportarNombresYPuntaje(archivo):
    entrada = open(archivo, "r")
    entrada.readline()
    entrada.readline()

    listaNyP = []

    for linea in entrada:
        datos = linea.split("&")
        listaNyP.append(datos[0].upper())
        listaNyP.append(datos[8].upper())

    entrada.close()

    return listaNyP

def reportarEquipoPerdidos3oMenos(archivo):
    entrada = open(archivo, "r")
    entrada.readline()
    entrada.readline()

    lista = []

    for linea in entrada:
        datos = linea.split("&")
        perdido=int(datos[4])

        if perdido<=3:
            lista.append(datos[0])

        else:
            pass

    entrada.close()

    return lista

def menorDiferenciaGoles(nombre):
    entrada = open(nombre, "r")
    entrada.readline()
    entrada.readline()
    numero=0
    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        a=int(datos[7])
        if a 
    entrada.close()

def graficarPuntos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()
    entrada.readline()

    listaEquipos = []
    listaPuntos=[]

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    #Graficar
    plot.plot(listaEquipos, listaPuntos)
    plot.show()

def main():
    ordenados=listarEquiposOrdenados("ligaMX.txt")
    print(ordenados)

    error=reportarErrorPuntos("ligaMX.txt")
    print (error)

main()

