#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" canguros_buenos.py """

class Canguro:
    """ Un Canguro es un marsupial. """

    def __init__(self, nombre, contenido = None):
        """
        Inicializar lso contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista de strings
        """
        if not contenido:
            contenido = []
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def meter_en_marsupio(self, item):
        """
        Agrega un nuevo item al marsupio.

        item: objeto a agregar
        """
        self.contenido_marsupio.append(item)

    def __str__(self):
        """
        devuelve una representación como cadena de este Canguro
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)


if __name__ == '__main__':
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)

    print(madre_canguro)
    print(cangurito)
