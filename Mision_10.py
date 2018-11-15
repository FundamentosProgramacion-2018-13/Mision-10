# Carlos Alberto Reyes Ortiz
#A01376349




def listarEquiposOrdenados(nombreArchivo):

    entrada = open(nombreArchivo, "r")
    entrada.readline()
    entrada.readline()

    listaEquipos = []

    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0].upper())

    listaEquipos.sort()

    return  listaEquipos

    entrada.close()




def main():
    ordenados = listarEquiposOrdenados("ligaMX.txt")
    print(ordenados)