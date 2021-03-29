#### informe.py
#
# Este código se corre de la siguiente manera:
#
# $ python3 informe.py ../Data/camion.csv ../Data/precios.csv
#
# E 2.15: Lista de tuplas
#
# [edited] E 2.16: Lista de diccionarios
#
# [edited] E 2.17: Diccionarios como contenedores
#
# [edited - main] E 2.18: Balance
import csv
import sys

def leer_camion(nombre_archivo):
    """
    abre un archivo con el contenido de un camión, lo lee y devuelve la 
    información como una lista de diccionarios
    """

    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {'nombre': row[0], 'cajones': int(row[1]),
                    'precio': float(row[2])}
            camion.append(lote)

    return camion


def leer_precios(nombre_archivo):
    """ 
    a partir del conjunto de precios que se encuentra en `nombre_archivo` arma un
    diccionario donde las claves son los nombres de las frutas y verduras (por ej)
    y los valores son los precios por cajón
    """

    precios = {}

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError: # por si hay alguna linea del archivo vacía
                continue

    return precios


""" main """
#camion = leer_camion('../Data/camion.csv')
#precios = leer_precios('../Data/precios.csv')
camion = leer_camion(sys.argv[1])
precios = leer_precios(sys.argv[2])

compra, venta = 0.0, 0.0
for s in camion:
    compra += s['cajones'] * s['precio']
    venta += s['cajones'] * precios[s['nombre']]

balance = venta - compra
gop = 'ganancia'
if (balance < 0): gop = 'perdida'

print(f'Costo del camión = ${compra:0.2f}')
print(f'Recaudación      = ${venta:0.2f}\n')
print(f'Balance          = ${balance:0.2f} (que equivale a un {100.0 * balance / compra:0.2f}% de {gop})')
