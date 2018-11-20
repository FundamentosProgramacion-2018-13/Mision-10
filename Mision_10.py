import matplotlib.pyplot as plot

def ordenarAlabeticamente(nombreArchivo):
    #en la lista nombres esquipos se agregan todos los nombres y despues se ordenan con la funcipon sort
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    entrada.readline()  # Título 1
    entrada.readline()   # Título 2
    nombresEquipos=[]
    for linea in entrada:
        datos=linea.split("&")
        nombresEquipos.append(datos[0].upper())
    nombresEquipos.sort()
    entrada.close()
    return nombresEquipos


def mostrarNombrePuntos(nombreArchivo):
    #a la lista nomPuntos se le agregan las tuplas con el nombre y los puntos
    entrada = open(nombreArchivo, "r")
    nomPuntos=[]
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2
    for linea in entrada:
        datos=linea.split("&")
        agregar=datos[0],datos[8][0:2]
        nomPuntos.append(agregar)
    entrada.close()
    return nomPuntos

def mostarPerdidiosMenorDe3 (nombreArchivo):
    #en listaEquipos se agregan solo los equipos que han peridios 3 o menos
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    listaEquipos=[]
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2
    for linea in entrada:
        datos=linea.split("&")
        numPerdidos=int(datos[4])
        if numPerdidos<=3:
            listaEquipos.append(datos[0])
    entrada.close()
    return listaEquipos


def buscarEquiposError (nombreArchivo):
    entrada= open (nombreArchivo,"r",encoding="UTF-8")
    equipos=[]
    entrada.readline() # Título 1
    entrada.readline()  # Título 2
    for linea in entrada:
        #linea= Veracruz&16&2&4&10&16&36&-20&10
        datos= linea.split("&")  #["Veracruz", "16",....]
        equipo=datos[0]
        jg=int(datos[2])
        je=int(datos[3])
        puntosReportados= int(datos[8])
        puntos= jg*3 + je*1
        if puntos != puntosReportados:
            equipos.append(equipo)
    entrada.close()
    return equipos


def mostrarMenorDiferenciaGoles(nombreArchivo):
    #todas las diferencias se guradan en un diccionario, se obtiene el valor menor y se regresa su llave
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    diferencias={}
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2
    for linea in entrada:
        datos=linea.split("&")
        diferencias[datos[0]]=int(datos[7])
    menor=min(diferencias.values())
    for llave in diferencias:
        if diferencias[llave]==menor:
            entrada.close()
            return llave

def crearNuevoArchivoUltimos5(nombreArchivo):
    #todos los equipos y sus puntos se agregan como tuplas en una lista, se ordenan conforme a los puntos y se mandan al nuevo archivo los ultimos 5
    entrada= open(nombreArchivo, "r", encoding="UTF-8")
    salida= open("Puntos.txt","w",encoding="UTF-8")
    nomPuntos=[]
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2
    for linea in entrada:
        datos = linea.split("&")
        agregar = datos[0] , int(datos[8][0:2])
        nomPuntos.append(agregar)
    nomPuntos.sort(key=lambda x: x[1])
    for k in range(13,18):
        tupla=str(nomPuntos[k])
        salida.write("%s \n"%(tupla))
    salida.close()
    entrada.close()


def graficarPuntos(nombreArchivo):
    #realiza la gráfica utilizando los datos de nombre de equipo y puntos
    entrada = open(nombreArchivo, "r", encoding="UTF-8")
    equipos = []
    entrada.readline()  # Título 1
    entrada.readline()  # Título 2

    listaEquipos=[]
    listaPuntos=[]

    for linea in entrada:
        datos=linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos,listaPuntos)
    plot.show()
    entrada.close()


def main():

   print(crearNuevoArchivoUltimos5("LigaMX.txt"))

main()
