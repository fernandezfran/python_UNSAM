#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" vigilante.py """

import os
import time

def vigilar(archivo_activo):
    
    f = open(archivo_activo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue
        yield line 

if __name__ == '__main__':
    import informe

    camion = informe.leer_camion('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
