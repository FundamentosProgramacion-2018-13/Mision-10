#Luis Mario Cervantes Ortiz

import matplotlib.pyplot as plot



def nombresAlfa(nombreArchivo): #falta mayuscula
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # abrir el archivo
    listaEquipos = []

    entrada.readline()
    entrada.readline()


    for linea in entrada:
        datos=linea.split("&")
        listaEquipos.sort()
        listaEquipos.append(datos[0])
    return listaEquipos

def definirPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equiposPun={}
    entrada.readline()
    entrada.readline()

    for linea in entrada:
        datos= linea.split("&")
        equiposPun[str(datos[0])]=int(datos[8])

    entrada.close()

    return  equiposPun


def equipoPerder(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # abrir el archivo
    equiposPer = []
    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2

    for linea in entrada:
        datos=linea.split("&")
        equipo=datos[0]
        jp= int(datos[4])

        if jp <= 3:
            equiposPer.append(equipo)

    return equiposPer




#Buscar los equipos que tienen masl reportado el número de puntos
def buscarEquiposError(nombreArchivo):
    entrada= open(nombreArchivo,"r",encoding="UTF-8") #abrir el archivo
    equipos=[]
    entrada.readline() #Titulo 1
    entrada.readline() #Titulo 2

    for linea in entrada:
        #linea = 'Veracruz&16&2&4&10&16&36&-20&10'
        datos = linea.split("&") # {"Veracruz", "16", ...]
        equipo= datos[0] # 0 = posicion inicial donde esta el equipo
        jg= int(datos[2]) #ganados
        je = int(datos[3]) #empatados
        puntosReportados= int(datos[8])
        puntos= jg*3 +je*1

        if puntos != puntosReportados:
            equipos.append(equipo)


    entrada.close()

    return equipos



def difGoles(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")  # abrir el archivo
    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2

    for linea in entrada:
        datos=linea.split("&")
        equipo=datos[0]
        difer=int(datos[7])
        if difer==0:
            return equipo


    entrada.close()


def puntosE():
    entrada = open("LigaMX.txt", "r", encoding="UTF-8")
    salida= open("Puntos.txt","a")
    entrada.readline()
    entrada.readline()


    for linea in entrada:
        datos = linea.split("&")
        equipo= datos[0] # 0 = posicion inicial donde esta el equipo
        jg= int(datos[2]) #ganados
        je = int(datos[3]) #empatados
        puntos= jg*3 +je*1
        if puntos <= 16:
            salida.write(equipo)

    entrada.close()
    salida.close()






def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo, "r", encoding="UTF-8")

    entrada.readline()  # Titulo 1
    entrada.readline()  # Titulo 2

    listaEquipos =[]
    listaPuntos =[]
    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))



    plot.plot(listaEquipos,listaPuntos)

    plot.show()

    entrada.close()




def main():

    errores=buscarEquiposError("LigaMX.txt")
    print(errores)
    grafica=graficarPuntos("LigaMX.txt")
    print (grafica)
    print(difGoles("LigaMX.txt"))

    print(nombresAlfa("LigaMX.txt"))
    print(equipoPerder("LigaMX.txt"))

    print(definirPuntos("LigaMX.txt"))
    print(puntosE())
main()