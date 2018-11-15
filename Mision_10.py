#Autor: Damián Iván García Ravelo
#A01376354

#Programa que evalua la liga mx

import matplotlib.pyplot as plot

def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()

    listaEquipos=[]
    listaPuntos=[]
    for linea in entrada:
        datos= linea.split("&") #separo los datos
        listaEquipos.append(datos[0]) #a la lista de equipos le agrego el nombre de cada equipo
        listaPuntos.append(int(datos[8])) #a la lista le doy los puntos

    #graficar
    plot.plot(listaEquipos,listaPuntos)
    #muestra grafica
    plot.show()


def reportarErroresPuntos(nombre):
    entrada=open(nombre,"r",encoding="UTF-8")
    #Elimino las 2 primeras lineas que no utilizo
    entrada.readline() #Título1
    entrada.readline() #Titulo2

    listaEquiposError = [] #Creo una nueva lista

    for linea in entrada:
        datos = linea.split("&")

        equipos=datos[0]
        jg = int(datos[2]) #juegos ganados
        je = int(datos[3]) #juegos empatados
        pr = int(datos[8]) #juegos perdidos

        pc= jg*3 + je*1

        if pr != pc:
            listaEquiposError.append(equipos)

    entrada.close()
    return listaEquiposError


def listarEquiposOrdenados(nombreArchivo):
    entrada=open(nombreArchivo,"r")
    #Elimino las 2 primeras lineas que no utilizo
    entrada.readline()
    entrada.readline()

    listaEquipos = [] #Creo una nueva lista

    for linea in entrada: #recorrer los datos en la lista
        datos = linea.split("&") #separa los valores ya que están "separados" por un &
        listaEquipos.append(datos[0].upper())  #A la nueva lista le agrega los datos en la posición 0 en mayúsculas

    listaEquipos.sort() #ordenas los datos alfabeticamente

    entrada.close()

    return listaEquipos




def main():
    ordenados=listarEquiposOrdenados("ligaMx.txt")
    print(ordenados)
    reporte=reportarErroresPuntos("ligaMX.txt")
    print(reporte)
    print(graficarPuntos("ligaMX.txt"))
main()
