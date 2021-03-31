#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#### propaga.py
#

def propagar(lista):
    """
    recibe una lista con valores posibles 0 ó +/- 1 y los valores 1 se propagan
    a los ceros hasta toparse con un -1
    """
    
    last = len(lista)
    propagada = lista
   
    for i, e in enumerate(lista):

        if e == 1:
            # propago a la izquieda de i hasta que haya un -1 o hasta que la lista
            # llegue al índice -1.
            j = 1
            while (i >= j and propagada[i-j] != -1):
                propagada[i-j] = 1
                j += 1
            
            # propago a la derecha de i hasta que haya un -1 o hasta que la lista
            # llegue al indice len(lista)
            k = 0
            while (i + k < last and propagada[i+k] != -1):
                propagada[i+k] = 1
                k += 1

    return propagada

#%%
# [main] E 4.9: Propagación
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0, 1, 0, 0]))
