#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt
from comparaciones_ordenamiento import generar_lista 
from seleccion import ord_seleccion
from insercion import ord_insercion
from burbujeo import ord_burbujeo
from merge_sort import merge_sort

def experimento_timeit_merge_sort(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método de selección para
    ordenamiento de listas con las listas pasadas como entrada y devuelve los
    tiempos de ejecución para cada lista en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método
    para cada lista.
    """
    tiempos_merge_sort = []

    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_merge_sort = tt.timeit('merge_sort(lista.copy())', 
                                     number = num, globals = globals())
        
        # guardo el resultado
        tiempos_merge_sort.append(tiempo_merge_sort)
        
    # paso los tiempos a arrays
    tiempos_merge_sort = np.array(tiempos_merge_sort)
    
    return tiempos_merge_sort


def experimento_timeit_burbujeo(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método de selección para
    ordenamiento de listas con las listas pasadas como entrada y devuelve los
    tiempos de ejecución para cada lista en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método
    para cada lista.
    """
    tiempos_burbujeo = []

    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', 
                                     number = num, globals = globals())
        
        # guardo el resultado
        tiempos_burbujeo.append(tiempo_burbujeo)
        
    # paso los tiempos a arrays
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    
    return tiempos_burbujeo


def experimento_timeit_insercion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método de selección para
    ordenamiento de listas con las listas pasadas como entrada y devuelve los
    tiempos de ejecución para cada lista en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método
    para cada lista.
    """
    tiempos_insercion = []

    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', 
                                     number = num, globals = globals())
        
        # guardo el resultado
        tiempos_insercion.append(tiempo_insercion)
        
    # paso los tiempos a arrays
    tiempos_insercion = np.array(tiempos_insercion)
    
    return tiempos_insercion

def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método de selección para
    ordenamiento de listas con las listas pasadas como entrada y devuelve los
    tiempos de ejecución para cada lista en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método
    para cada lista.
    """
    tiempos_seleccion = []

    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', 
                                     number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion


def generar_listas(Nmax):
    return [generar_lista(N) for N in range(1,Nmax)]


if __name__ == '__main__':

    listas = generar_listas(256)

    tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
    tiempos_insercion = experimento_timeit_insercion(listas, 100)
    tiempos_burbujeo = experimento_timeit_burbujeo(listas, 100)
    tiempos_merge_sort = experimento_timeit_merge_sort(listas, 100)

    plt.plot(tiempos_seleccion, label='seleccion')
    plt.plot(tiempos_insercion, label='insercion')
    plt.plot(tiempos_burbujeo, label='burbujeo')
    plt.plot(tiempos_merge_sort, label='merge sort')
    plt.show()
