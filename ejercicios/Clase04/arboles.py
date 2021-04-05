#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#### arboles.py
#
# para más información ver: '../Clase03/arboles.py'
#
import sys
import csv
from collections import Counter

from pprint import pprint


def leer_arboles(nombre_archivo):
    """
    abre un archivo .csv con la información de la distribución del arbolado en los
    parques de una ciudad y devuelve una lista de diccionarios donde cada uno de
    ellos tiene información sobre un árbol en particular de todos los parques
    """

    with open(nombre_archivo, 'rt') as f:

        filas       = csv.reader(f)
        encabezados = next(filas)
      
        ldd = [dict(zip(encabezados, fila)) for fila in filas]
    
    return ldd


def medidas_de_especies(especies, arboleda):
    """
    reccibe una lista de nombres de especies y una lista con un diccionario para
    cada arbol (como la generada por la función `leer_arboles`) y devuelve un
    diccionario cuyas claves son las especies y su valor asociado es una lista
    con tuplas en las que se encuentran la altura total y del diametro de los
    árboles de esa especie
    """

    #d = {}
    #for especie in especies:
    #    lAD= [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in
    #                arboleda if arbol['nombre_com'] == especie]
    #    d[especie] = lAD
    d = { especie : [(float(arbol['altura_tot']), float(arbol['diametro']))
                      for arbol in arboleda if arbol['nombre_com'] == especie] 
              for especie in especies}

    return d


""" main : ejercicios """

# E 4.18: Lectura de todos los árboles
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

# E 4.19: Lista de altos de Jacarandá
H = [float(arbol['altura_tot']) for arbol in arboleda 
        if arbol['nombre_com'] == 'Jacarandá']

# E 4.20: Lista de altos y diámetros de Jacarandá
lAD = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda
        if arbol['nombre_com'] == 'Jacarandá']
#pprint(lAD)

# E 4.21: Diccionario con medidas
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
MDE = medidas_de_especies(especies, arboleda)
#print(len(MDE), len(MDE[especies[0]]), len(MDE[especies[1]]), len(MDE[especies[2]]))
