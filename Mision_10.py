import matplotlib.pyplot as plot

#1 Nombres en mayusculas
def mostrarNombresMayusculas(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    equipos = []

    entrada.readline()  # Bye linea 1
    entrada.readline()  # Bye linea 2

    for linea in entrada:
        linea = linea.upper()
        datos=linea.split("&")
        equipos.append(datos[0])

    entrada.close()
    return equipos

def mostarNombresYPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    equipos = {}

    entrada.readline()  # Bye linea 1
    entrada.readline()  # Bye linea 2

    for linea in entrada:
        datos = linea.split("&")
        equipos[datos[0]]=int(datos[8])


    entrada.close()
    return equipos


def mostrarEquiposBuenos(nombreArchivo):
    entrada = open(nombreArchivo, "r")
    equipos = []

    entrada.readline()  # Bye linea 1
    entrada.readline()  # Bye linea 2

    for linea in entrada:
        datos = linea.split("&")
        if datos[4]<=3:
            equipos.append(datos[0])

    entrada.close()
    return equipos


#4 Buscar equipos con error en puntos
def buscarError(nombreArchivo):
    entrada = open(nombreArchivo, "r")

    equipos =[]
    entrada.readline() #Bye linea 1
    entrada.readline() #Bye linea 2

    for linea in entrada:
        datos=linea.split("&")
        sumaPuntos = int(datos[2])*3 + int(datos[3])
        if sumaPuntos != int(datos[8]):
            equipos.append(datos[0])

    entrada.close()
    return equipos


#7 Gráfica
def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r")

    entrada.readline() #Bye linea 1
    entrada.readline() #Bye linea 2

    listaEquipos =[]
    listaPuntos =[]

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos, listaPuntos)
    plot.show()

    entrada.close()

def main():
    archivo="LigaMX.txt"
    print(mostrarNombresMayusculas(archivo))
    print(mostarNombresYPuntos(archivo))
    error = buscarError(archivo)
    print("Equipos con error:")
    if len(error)>0:
        for datos in error:
            print (datos)
    else:
        print("No hay")



    graficarPuntos(archivo)
main()