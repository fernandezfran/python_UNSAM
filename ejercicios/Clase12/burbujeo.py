#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ord_burbujeo(lista):
    """
    Ordenamiento por burbujeo. O(N^2)
    Pre:  los elementos de la lista deben ser comparables
    Post: la lista está ordenada

    Devuelve la cantidad de comparaciones realizadas
    """
    
    #comparaciones = 0
    n = len(lista) - 1
    while (n > 0):

        for i in range(n):
            a = lista[i]
            b = lista[i+1]
            #comparaciones += 1
            if a > b:
                lista[i+1] = a
                lista[i]   = b

        n -= 1

    #return comparaciones

if __name__ == '__main__':
    lista_1 = [1, 2, -3, 8, 1, 5]
    print("lista    = ", lista_1)
    ord_burbujeo(lista_1)
    print("burbujeo = ", lista_1)
    print("-----------")

    lista_2 = [1, 2, 3, 4, 5]
    print("lista    = ", lista_2)
    ord_burbujeo(lista_2)
    print("burbujeo = ", lista_2)
    print("-----------")
    
    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    print("lista    = ", lista_3)
    ord_burbujeo(lista_3)
    print("burbujeo = ", lista_3)
    print("-----------")
    
    lista_4 = [10, 8, 6, 2, -2, -5]
    print("lista    = ", lista_4)
    ord_burbujeo(lista_4)
    print("burbujeo = ", lista_4)
    print("-----------")
    
    lista_5 = [2, 5, 1, 0]
    print("lista    = ", lista_5)
    ord_burbujeo(lista_5)
    print("burbujeo = ", lista_5)
