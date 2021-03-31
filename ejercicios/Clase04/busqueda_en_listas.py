#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#### busqueda_en_listas.py

def buscar_u_elemento(lista, elemento):
    """
    recibe una lista y un elemento
    devuelve la posición de la última aparición de ese elemento en la lista o -1
        si el elemento no pertenece a la lista
    """

    pos = -1
    for i, l_i in enumerate(lista):
        
        if l_i == elemento: pos = i

    return pos


def buscar_n_elemento(lista, elemento):
    """
    recibe una lista y un elemento
    devuelve la cantidad de veces que aparece el elemento en la lista
    """

    ntimes = 0
    for i, l_i in enumerate(lista):

        if l_i == elemento: ntimes += 1

    return ntimes


def maximo(lista):
    """
    devuelve el máximo de una lista (la lista debe ser no vacía y de números
                                     positivos)
    """

    # m guarda el máximo de los elementos a medida que recorro la lista.
    m = lista[0] # Lo inicializo en 0
    for e in lista: # recorro la lista y voy guardando el mayor
        if e > m: m = e

    return m


#%%
# [main] E 4.6: Búsquedas de un elemento
#
lista = [1, 2, 3, 2, 3, 4]
print(buscar_u_elemento(lista,1))
print(buscar_u_elemento(lista,2))
print(buscar_u_elemento(lista,3))
print(buscar_u_elemento(lista,5))
print()

nro = 2
print(f"El número {nro} aparece {buscar_n_elemento(lista, 2)} veces en la lista")
print()

#%%
# [main] E 4.7: Búsqueda de máximo y mínimo
#
print(maximo([1,2,7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5,4]))
print(maximo([-5,-4]))
print()

#%%

