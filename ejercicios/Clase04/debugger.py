#### debugger.py
#
# E 4.1: Debugger
#
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''

    invertida = []
    i=len(lista)
   
    while i > 0:    # tomo el último elemento 
        i=i-1
        invertida.append(lista[i])  # .pop(i) no es necesario, solo quero leer
                                    # el valor i de la lista para cambiar su pos
    
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')
#
# E 4.2: Más debugger
#       (ver los comentarios a los bugs del principio de la clase 3 para ver que
#        es lo que pasaba)
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
