#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" lote.py
Lote de cajones de una misma fruta
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre  = nombre
        self.cajones = cajones
        self.precio  = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, n):
        self.cajones -= n


class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
        super().__init__(nombre, cajones, precio)
        self.factor = factor

    def rematar(self):
        self.vender(self.cajones)

    def costo(self):
        return self.factor * self.cajones * self.precio

    def precio(self):
        costo_orig = super().costo()
        return self.factor * costo_orig
