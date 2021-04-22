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
###############################    MODIFICACIÓN    ###############################
#
# E 6.4: Estructurar un programa como una colecciónde funciones
#
# E 6.5: Crear una función de alto nivel para la ejecución del programa
#
# E 6.11: Usemos el módulo fileparse
#
import csv
import fileparse as fp

def leer_camion(nombre_archivo):
    """
    abre un archivo con el contenido de un camión, lo lee y devuelve la 
    información como una lista de diccionarios
    """

    camion = fp.parse_csv(nombre_archivo, select=['nombre', 'cajones', 'precio'],
                          types=[str, int, float])

    return camion


def leer_precios(nombre_archivo):
    """ 
    a partir del conjunto de precios que se encuentra en `nombre_archivo` arma un
    diccionario donde las claves son los nombres de las frutas y verduras (por ej)
    y los valores son los precios por cajón
    """

    precios = fp.parse_csv(nombre_archivo, types=[str, float], has_headers=False)

    return dict(precios)


def hacer_informe(lista_cajones, precio_cajones):
    """
    realiza un balance con la lista de cajones que se recibe y el diccionario
    de sus precios
    """

    informe = []
    for s in lista_cajones:
        nombre  = s['nombre']
        cajones = s['cajones']
        precio  = s['precio']
        cambio  = precio_cajones[s['nombre']] - s['precio']

        # tupla con la información
        t_info = (nombre, cajones, precio, cambio)
        informe.append(t_info)

    return informe


def imprimir_informe(informe):
    """
    imprime un informe (no devuelve ningún valor, sólo imprime a pantalla)
    """
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:^10s} {headers[1]:^10s} {headers[2]:^10s}' 
          f'{headers[3]:^10s}')
    print(f'{"-":-^10s} {"-":-^10s} {"-":-^10s} {"-":-^10s}')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {f"${precio:.2f}":>10s}' 
              f'{cambio:>10.2f}')


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    """
    realiza el informe de un camión cuando la entrada son dos archivos
    """
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


if __name__ == '__main__':
    informe_camion('../Data/fecha_camion.csv', '../Data/precios.csv')
