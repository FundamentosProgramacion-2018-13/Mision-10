#Diego Armando Ayala Hernadez
#a013767247#

import matplotlib.pyplot as plot
def listarEquiposOrdenados(nombreArchivo):
    entrada=open(nombreArchivo, "r")
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
    entrada.readline()
    entrada.readline()
    listaEquiposError=[]

    for linea in entrada:
        datos=linea.split("&")
        equipo=datos[0]
        jg=int(datos[2])
        je=int(datos[3])
        pr=int(datos[8])
        pc=jg*3+je
        if pr!=pc:
            listaEquiposError.append((equipo))
    entrada.close()
    return listaEquiposError


def graficarPuntos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()
    entrada.readline()
    listaEquipos=[]
    listaPuntos=[]
    for linea in entrada:
        datos=linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))
    plot.plot(listaEquipos,listaPuntos)
    plot.show()

def nombreypuntos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()
    entrada.readline()
    listanueva=[]
    for linea in entrada:
        datos=linea.split("&")
        listanueva.append(datos[0])
        listanueva.append(int(datos[8]))

    entrada.close()
    return listanueva

def partidosperdidos(nombre):
    entrada = open(nombre, "r")
    entrada.readline()
    entrada.readline()
    listanueva = []
    for linea in entrada:
        datos = linea.split("&")
        perdidos=int(datos[4])
        equipo=datos[0]
        if perdidos<=3:
            listanueva.append(equipo)

    entrada.close()
    return listanueva
def menorcantidad(nombre):
    entrada = open(nombre, "r")
    entrada.readline()
    entrada.readline()
    

    valor1=0
    equipo1=""
    for linea in entrada:
        datos = linea.split("&")
        valor=int(datos[7])
        equipo=datos[0]
        if valor>valor1:
            valor1=valor
            equipo1=equipo

    return equipo1
def main():
    ordenados= listarEquiposOrdenados("liga10.txt")
    print(ordenados)
    errores=reportarErrorPuntos("liga10.txt")
    print(errores)

    print(nombreypuntos("liga10.txt"))
    print((partidosperdidos("liga10.txt")))
    print(menorcantidad("liga10.txt"))
    graficarPuntos("liga10.txt")
main()
