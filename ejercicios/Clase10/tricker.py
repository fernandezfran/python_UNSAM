#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" tricker.py """

from vigilante import vigilar
import informe
import formato_tabla
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def tricker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)

    filas = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(filas, camion)

    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for fila in filas:
        datos_fila = [fila['nombre'], str(fila['precio']), str(fila['volumen'])]
        formateador.fila(datos_fila)

if __name__ == '__main__':
    tricker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')
