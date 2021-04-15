#### fileparse.py
#
# E 6.6: Parsear un archivo CSV
#
# E 6.7: Selector de columnas
#
# E 6.8: Conversión de tipo
#
# E 6.9: Trabajando sin encabezados
#
import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.

    Se puede seleccionar sólo un subconjunto de columnas, determinando el 
    parámetrro select, que debe ser una lista de nombres de las columnas a 
    considerar.

    Se puede especificar el tipo de datos que hay en las columnas a través de la
    lista de funciones types, que debe estar ordenada según el orden de las
    columnas que se desea leer.

    A través de la variables has_headers, se puede trabajar tanto con archivos que
    tienen encabezados (default) como los que no.
    """
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        indices = []
        if has_headers: 
            # Lee los encabezados
            headers   = next(rows)

            # Si se indicó un selector de columnas, buscar los índices de las 
            # columnas especificadas. En ese caso, achicar el conjunto de
            # encabezados para los diccionarios.
            if select:
                indices = [headers.index(nombre_columna) for
                                                         nombre_columna in select]
                headers = select
        
        registros = []
        for row in rows:
            if not row: continue # saltea fila sin dato

            # filtrar la fila que si se especificaron columnas
            if indices: row = [row[index] for index in indices]

            # convierte el tipo de los datos
            if types: row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                # armar el diccionario
                registro = dict(zip(headers, row))
            else:
                # armar tupla
                registro = tuple(row)
            
            registros.append(registro)

    return registros
