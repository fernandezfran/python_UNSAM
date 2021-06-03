#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ISO 216 : tamaños de papel
"""

def A(N):
    """
    para un valor de N > 0 devuelve el ancho y el largo de la hoja A{N} en mm
    """
    if N == 0:
        ancho, largo = 841, 1189
    else:
        ancho, largo = A(N-1)
        ancho, largo = largo // 2, ancho
    return ancho, largo


if __name__ == '__main__':
    for i in range(6):
        ancho, largo = A(i)
        print(f'La hoja A{i} mide ({ancho} x {largo} mm)')
