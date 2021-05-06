#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" listar_img.py
Dado un directorio, imprime en pantalla los nombres de todos los archivos .png
que se encuentran en algún subdirectorio de él.
"""
import os

def listar_extension(dir_name, ext='.png'):
    """
    recibe el nombre de un directorio y devuelve una lista con todos los archivos
    que tienen la extension 'ext'
    """

    list_ext = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if ext in name:
                list_ext.append(name)
        for name in dirs:
            if ext in name:
                list_ext.append(name)

    return list_ext


if __name__ == '__main__':
    import sys
    
    directorio = sys.argv[1]
    lista_png  = listar_extension(directorio)
    for imagen in lista_png:
        print(imagen)
