#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from seleccion import ord_seleccion
from insercion import ord_insercion
from burbujeo import ord_burbujeo
from merge_sort import merge_sort

def generar_lista(N, nmax=1000):
    """
    devuelve una lista de largo N con números aleatorios entre 0 y nmax
    """
    return list(np.random.choice(range(1,nmax+1), N, replace=True))

if __name__ == '__main__':
    
    nI, nS, nB, nM = [], [], [], []
    for N in range(1, 256):
        l = generar_lista(N)
        lS, lI, lB, lM = l.copy(), l.copy(), l.copy(), l.copy()

        nS.append(ord_seleccion(lS))
        nI.append(ord_insercion(lI))
        nB.append(ord_burbujeo(lB))
        lM, m = merge_sort(lM)
        nM.append(m)
       
    x = np.array(range(1,256))

    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("N largo de la lista")
    plt.ylabel("# de comparaciones")
    plt.plot(x, nB, label='burbujeo')
    plt.plot(x, nS, '--', label='seleccion')
    plt.plot(x, nI, label='insercion')
    plt.plot(x, nM, label='merge sort')
    plt.legend()
    plt.show()
