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
###############################    MODIFICACIÓN    ###############################
#
# E 3.13: Recolectar datos (función hacer_informe)
#
# E 3.14: Imprimir una tabla con formato
#
# E 3.15: Agregar encabezados
#
# E 3.16: Un desafío de formato
#
import csv

def leer_camion(nombre_archivo):
    """
    abre un archivo con el contenido de un camión, lo lee y devuelve la 
    información como una lista de diccionarios
    """

    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows    = csv.reader(f)
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


def hacer_informe(lista_cajones, precio_cajones):
    """
    realiza un balance con la lista de cajones que se recibe y el diccionario
    de sus precios
    """

    informe = []
    for s in lista_cajones:
        nombre  = s['nombre']
        cajones = int(s['cajones'])
        precio  = float(s['precio'])
        cambio  = float(precio_cajones[s['nombre']]) - float(s['precio'])

        # tupla con la información
        t_info = (nombre, cajones, precio, cambio)
        informe.append(t_info)

    return informe

camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:^10s} {headers[1]:^10s} {headers[2]:^10s} {headers[3]:^10s}')
print(f'{"-":-^10s} {"-":-^10s} {"-":-^10s} {"-":-^10s}')
for nombre, cajones, precio, cambio in informe:
    # Nested f-strings: 
    #     https://stackoverflow.com/questions/41215365/nested-f-strings
    print(f'{nombre:>10s} {cajones:>10d} {f"${precio:.2f}":>10s} {cambio:>10.2f}')
