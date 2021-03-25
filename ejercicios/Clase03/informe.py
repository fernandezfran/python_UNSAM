#### informe.py
#
# E 2.15: Lista de tuplas
#
# [edited] E 2.16: Lista de diccionarios
#
# [edited] E 2.17: Diccionarios como contenedores
#
# [edited - main] E 2.18: Balance
#
###############################    MODIFICACIÓN    ###############################
#
# E 3.9: función zip()
#
import csv

def leer_camion(nombre_archivo):
    """
    abre un archivo con el contenido de un camión, lo lee y devuelve la 
    información como una lista de diccionarios
    """

    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for nrow, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            camion.append(record)

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


camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')

compra, venta = 0.0, 0.0
for s in camion:
    ncajones = int(s['cajones'])
    precio_compra = float(s['precio']) 
    precio_venta  = float(precios[s['nombre']])

    compra += ncajones * precio_compra
    venta += ncajones * precio_venta

balance = venta - compra
gop = 'ganancia'
if (balance < 0): gop = 'perdida'

print(f'Costo del camión = ${compra:0.2f}')
print(f'Recaudación      = ${venta:0.2f}\n')
print(f'Balance          = ${balance:0.2f} (que equivale a un {100.0 * balance / compra:0.2f}% de {gop})')
