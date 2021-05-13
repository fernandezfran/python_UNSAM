#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" geom.py
un ejercicio geométrico
"""

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)


class Rectangulo(Punto):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def base(self):
        return abs(self.a.x - self.b.x)

    def altura(self):
        return abs(self.a.y - self.b.y)

    def area(self):
        return Rectangulo.base(self)*Rectangulo.altura(self)

    def desplazar(self, desplazamiento):
        return Rectangulo(self.a + desplazamiento, self.b + desplazamiento)

    def rotar(self):
        pass

    def __str__(self):
        return f'{self.a} {self.b}' 

    def __repr__(self):
        return f'Rectanguno(Punto({self.a}), Punto({self.b}))'
