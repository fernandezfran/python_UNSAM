#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo : precio_alquiler ~ superficie
superfices (en metros cuadrados)
precios (en miles de pesos) de alquiler mensual en Caballito (CABA)
"""
import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
a, b = ajuste_lineal_simple(superficie, alquiler)

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
