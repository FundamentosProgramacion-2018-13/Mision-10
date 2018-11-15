#Autor: Damián Iván García Ravelo
#A01376354

#Programa que evalua la liga mx

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

main()