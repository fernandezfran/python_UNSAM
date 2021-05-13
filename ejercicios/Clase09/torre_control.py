#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" torre_de_control.py 
Modela el trabajo de una torre de control de un aeropuerto con una pista de
aterrizaje. Los aviones que están esperando para aterrizar tienen prioridad sobre
los que están esperando para despegar.

Utiliza la clase `Cola` de las notas de la materia
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

    def __str__(self):
        return ", ".join(self.items)


class TorreDeControl(Cola):
    ''' Representa los vuelos que esperan para aterrizar/despegar en una torre
    de control. Los que van a aterrizar tienen prioridad sobre los que esperan
    despegar.
    '''
    def __init__(self):
        self.vuelos_arribos  = Cola()
        self.vuelos_partidas = Cola()
    
    def nuevo_arribo(self, vuelo):
        ''' agrega un vuelo a los que esperan aterrizar '''
        self.vuelos_arribos.encolar(vuelo)

    def nueva_partida(self, vuelo):
        ''' agrega un vuelo a los que esperan aterrizar '''
        self.vuelos_partidas.encolar(vuelo)

    def asignar_pista(self):
        try:
            if self.vuelos_arribos.esta_vacia():
                a = self.vuelos_partidas.desencolar()
                print(f'El vuelo {a} despegó con éxito.')
            else:
                b = self.vuelos_arribos.desencolar()
                print(f'El vuelo {b} aterrizó con éxito.')
        except ValueError:
            print('No hay vuelos en espera.')

    def ver_estado(self):
        ''' informe de los vuelos esperando aterrizar / despegar '''
        estado = f'Vuelos esperando para aterrizar: {self.vuelos_arribos}\n'
        estado += f'Vuelos esperando para despegar: {self.vuelos_partidas}'
        print(estado)


if __name__ == '__main__':
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
