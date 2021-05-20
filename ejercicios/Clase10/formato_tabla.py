#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla
        '''
        raise NotImplementedError()


class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla de formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()


class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))


class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(f'<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print(f'</tr>')

    def fila(self, data_fila):
        print(f'<tr>', end='')
        for d in data_fila:
            print(f'<th>{d}</th>', end='')
        print(f'</tr>')


def crear_formateador(fmt):
    '''
    crea un objeto formateador dado un tipo de salida como txt, csv, html
    '''
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')

    return formateador


def imprimir_tabla(camion, col_sel, formateador):
    '''
    recibe camión e imprime una selección de columnas
    '''
    formateador.encabezado(col_sel)
    for fruta in camion:
        rowdata = [str(getattr(fruta, col_name)) for col_name in col_sel]
        formateador.fila(rowdata)
