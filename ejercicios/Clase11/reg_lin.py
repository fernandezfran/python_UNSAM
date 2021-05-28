#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ajuste del modelo de cuadrados mínimos
"""
import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
a, b = ajuste_lineal_simple(x, y)

plt.scatter(x = x, y = y)
plt.plot(x, a*x + b, c='green')
plt.title('ajuste lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
