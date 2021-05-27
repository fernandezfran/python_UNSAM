#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
triango de Pascal
"""

def pascal(n, k):
    """
    n >= 0 es la fila (de arriba hacía abajo)
    0 <= k <= n es la columna (de izquierda a derecha)
    """
    if n <= 1:
        res = 1
    else:
        if k == 0 or k == n:
            res = 1
        else:
            res = pascal(n-1, k-1) + pascal(n-1, k)
    return res
