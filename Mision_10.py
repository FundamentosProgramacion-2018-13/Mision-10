#Zabdiel Valentín Garduño Vivanco
#Calcular diferentes datos de la LigaMX


import matplotlib.pyplot as plot
def nombresMayusculasOrdenados(nombreArchivo):#Ejercicio 01
    entrada=open(nombreArchivo,"r")
    equipos=[]
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo 2
    for linea in entrada:
        datos=linea.split("&")
        equipos.append(datos[0])
    equipos.sort()
    for x in range(0,len(equipos)):
        equipos[x]=equipos[x].upper()
    entrada.close()
    return equipos


def mostrarEquipoPuntos(nombreArchivo):#Ejercicio 02
    entrada=open(nombreArchivo,"r")
    equipos={}
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo 2

    for linea in entrada:
        datos=linea.split("&")
        equipos[datos[0]]=int(datos[8])

    entrada.close()
    return equipos


def partidosPerdidos(nombreArchivo):#Ejercicio 03
    entrada=open(nombreArchivo,"r")
    equipos=[]
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo 2

    for linea in entrada:
        datos=linea.split("&")
        if int(datos[4])<=3:
            equipos.append(datos[0])
    entrada.close()
    return equipos


def buscarEquiposError(nombreArchivo):#Problema 04
    entrada=open(nombreArchivo,"r")
    equipos=[]
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo 2

    for linea in entrada:
        #Linea=
        datos=linea.split("&")  #['Veracruz,'16,...]
        equipo=datos[0]
        jg=int(datos[2])
        je=int(datos[3])
        puntosReportados=int(datos[8])
        puntos=jg*3+je*1
        if puntos !=puntosReportados:
            equipos.append(equipo)

    entrada.close()
    return equipos


def menorDiferenciaGoles(nombreArchivo):#Problema 05
    entrada=open(nombreArchivo,"r")
    equipos={}
    a=None
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo 2
    for linea in entrada:
        datos=linea.split("&")
        equipos[datos[0]]=int(datos[7])
    for llave,valor in equipos.items():
        if valor==0:
            a=llave
    entrada.close()
    return a

def ultimosCincoLugares(nombreArchivo):#Ejercico 06
    entrada=open(nombreArchivo,"r")
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo
    salida=open("Puntos.txt","w")
    for linea in entrada: #Lee linea por linea
        datos01=linea.split("&")
        Equipo=datos01[0]
        Puntos=datos01[8]
        salida.write("%s,%s"%(Equipo,Puntos))
    entrada.close()
    salida.close()


def graficarPuntos(nombreArchivo):#Problema 07
    entrada=open(nombreArchivo,"r")
    equipos=[]
    entrada.readline() #Desecha titulo
    entrada.readline() #Desecha titulo 2
    listaEquipos=[]
    listaPuntos=[]

    for linea in entrada:
        datos=linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))
    plot.plot(listaEquipos,listaPuntos)
    plot.show()
    entrada.close()

