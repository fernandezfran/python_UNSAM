#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#### arboles.py
#
# para más información ver: '../Clase03/arboles.py' y '../Clase04/arboles.py'
#
import os
import sys
import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

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


""" E 5.* en funciones """
# 5.24: Histograma de altos de Jacarandás
def histo_altura(altura_especie, nbins):
    """
    recibe una lista numerica con los altos de una especie particular de arboles
    y el numero de bins deseados para realizar un histograma
    """
    plt.hist(altura_especie, bins=nbins)
    plt.show()


# E 5.25: Scatter plot (diametro vs alto)
def scatter_dvsa(diametros, alturas, s):
    """
    recibe dos vectores de numpy, que contienen los diametros y alturas de los
    arboles y un string s con el tipo de arbol para grafica un scatter plot
    """
    plt.scatter(diametros, alturas, alpha=0.05)
    plt.xlabel("diametro [cm]")
    plt.ylabel("alto [m]")
    plt.title(f"Relacion diámtro-alto para {s}")
    plt.xlim(0,200)
    plt.ylim(0,50)
    plt.show()

# E 5.24: main (lista de altos de Jacarandá)
nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
H = [float(arbol['altura_tot']) for arbol in arboleda 
        if arbol['nombre_com'] == 'Jacarandá']
histo_altura(H, 20)

# E 5.25: Scatterplot (diámetro vs alto) de Jacarandás
lAD= [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda
        if arbol['nombre_com'] == 'Jacarandá']
AD = np.transpose(np.array(lAD))
A = AD[0]
D = AD[1]
scatter_dvsa(D, A, 'Jacarandá')

# E 5.26: Scatterplot para diferentes especies
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
MDE = medidas_de_especies(especies, arboleda)
for especie, lAD in MDE.items():
    AD = np.transpose(np.array(lAD))
    A = AD[0]
    D = AD[1]
    scatter_dvsa(D, A, especie)
