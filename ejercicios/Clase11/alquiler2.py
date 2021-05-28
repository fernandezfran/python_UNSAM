#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo : precio_alquiler ~ superficie + antigüedad
precios [en miles de pesos] de alquiler mensual en Caballito (CABA)
superfices [en metros cuadrados]
antiguedad [en años]
"""
import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = np.array([50.0, 5.0, 25.0, 70.0])

data_deptos = pd.DataFrame({'alquiler': alquiler, 
                            'superficie': superficie, 
                            'antigüedad': antigüedad})

X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)

errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio

#b0 = ajuste_deptos.intercept_
#b1, b2 = ajuste_deptos.coef_

#plt.plot(superficie, b1*superficie + b0, label='superficie')
#plt.plot(antigüedad, b2*antigüedad + b0, label='antigüedad')
#plt.legend()
#plt.show()
