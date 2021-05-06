#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" mareas_fft.py
Análisis y visualización de series temporales: _onda de marea_ generada por la 
    atracción gravitacional que ejercen la luna y el sol sobre el agua.

Datos de mareas en el Río de la Plata:
    + 14 picos cada 7 días debido a la frecuencia semidiura de las mareas.
    + Marea de San Fernando (SF) retrasada con respecto a la de Buenos Aires (BA).
      (SF está más lejos que BA, desde el atlántico).
    + Hay una diferencia en las alturas porque los ceros no están nivelados entre
      sí.
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'],
                 parse_dates=True)

dh = df['12-25-2014':].copy()

delta_t = -1    # tiempo que tarda la marea entre ambos puertos
delta_h = 23.62  # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
plt.show()
