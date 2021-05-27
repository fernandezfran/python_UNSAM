#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
búsqueeda binaria
"""

def bbinaria_rec(lista, e):
    """
    devuelve True o False si el elemento e está o no en la lista ordenada lista
    """
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] > e:
            res = bbinaria_rec(lista[:medio], e)
        else: # lista[medio] < e
            res = bbinaria_rec(lista[medio:], e)
    return res
