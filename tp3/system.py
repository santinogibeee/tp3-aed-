from soporte import *
import random
import os.path

def leerarchivo():
    # Verificacion de que el archivo existe:
    tratamientos = []
    archivo = "new.csv"
    if not os.path.exists(archivo):
        print("El archivo existe!")
        return
    m = open(archivo, "rt")
    m.readline()

    for linea in m:
        if linea[-1] == "\n":
            linea = linea[:-1]
        t = procesarlinea(linea)

        # CUIDADO!
        tratamientos.append(t)





    m.close()
    return tratamientos



def principal():
    # Procesar archivo csv
    tratamientos = leerarchivo()
    print("r1.1: ", len(tratamientos))
    print("r1.2: ")

if __name__ == "__main__":
    principal()