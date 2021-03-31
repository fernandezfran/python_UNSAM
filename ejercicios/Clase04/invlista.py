#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#### invlista.py
#
def invertir_lista(lista):
    """
    Recibe una lista y la develve invertida
    """

    invertida = []
    for e in lista:
        
        invertida.insert(0, e)  # agrego el elemento e al principio de la lista
                                # invertida
    return invertida

#%%
# [main] E 4.8: Invertir una lista
print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
