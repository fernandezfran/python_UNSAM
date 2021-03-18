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
#### camion_commandline.py
#
# E 2.10: Ejecución desde la línea de comandos con parámetros
import sys
import csv

def costo_camion(file_camion):
    file_camion = open(file_camion)
    rows = csv.reader(file_camion)
    headers = next(rows)

    costo = 0
    for row in rows:
        columna = row
        try:
            costo += int(columna[1]) * float(columna[2])
        except ValueError:
            print(f'{columna[0]} tiene algún valor inválido')

    file_camion.close()

    return costo


if len(sys.argv) == 2:
    file_nombre = sys.argv[1]
else:
    file_nombre = '../Data/camion.csv'

costo = costo_camion(file_nombre)
print("Costo total", costo)
