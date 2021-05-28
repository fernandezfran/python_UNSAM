#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Peso específico R : peso / volumen [g/cm^3]
barras -> base de 1 cm^2 y largos diversos

Ajuste : peso ~ longitud
"""
import requests
import io
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

enlace = 'https://raw.githubusercontent.com/python-unsam/Programacion_en_Python_UNSAM/master/Notas/11_Recursion/longitudes_y_pesos.csv'
r = requests.get(enlace).content
data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))

ajuste = linear_model.LinearRegression(fit_intercept=False)
ajuste.fit(data_lyp[['longitud']], data_lyp[['peso']])

a = ajuste.coef_
R = a[0][0]
print(f"El peso específico del metal es {R} [g/cm^3]")

errores = data_lyp.peso - R * data_lyp.longitud
print(f"ECM:", (errores**2).mean())

data_lyp.plot.scatter('longitud', 'peso')
plt.plot(data_lyp.longitud, R * data_lyp.longitud, c='green')
plt.title("ajuste lineal : peso ~ longitud")
plt.show()
