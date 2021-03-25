#### costo_camion.py
#
# E 2.2: Lectura de un archivo de datos
#
# [edited] E 2.6: Transformar el script a una función
#
# [edited] E 2.8: Administración de errores
#
# [edited] E 2.9: Funciones de la biblioteca
#
##############################     MODIFICACIÓN     ##############################
#
# E 3.8: ejemplo práctico de enumerate()
#
# [edited] E 3.9: función zip()
#
import csv

def costo_camion(file_camion):
    file_camion = open(file_camion)
    rows = csv.reader(file_camion)
    headers = next(rows)

    costo = 0
    for nrow, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo += ncajones * precio
        except ValueError:
            # esto atrapa los errores de aplicar int() y float() arriba
            print(f'Fila {nrow}: No pude interpretar: {row}')

    file_camion.close()

    return costo

costo = costo_camion('../Data/fecha_camion.csv')
print("Costo total", costo)
