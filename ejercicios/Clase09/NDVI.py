#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" NDVI.py (Normalized Difference Vegetation Index)
Ejecicio optativo de Teledetección : Clasificación automática 
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dir_name = '../Data/clip/'
filename = 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band'
ext = '_clip.npy'
ROJO               = np.load(dir_name + filename + '4' + ext)
INFRARROJO_CERCANO = np.load(dir_name + filename + '5' + ext)

print(ROJO[974][1889], INFRARROJO_CERCANO[974][1889])

NDVI = (INFRARROJO_CERCANO - ROJO) / (INFRARROJO_CERCANO + ROJO)
# filtro datos ruidosos de NDVI que debe estar definido en [-1, 1]
NDVI[NDVI > 1] = 1
NDVI[NDVI < -1] = -1

# KMeans necesita que se le diga cuantos clusters tiene que encontrar
kmeans = KMeans(n_clusters = 5)

# paso la matriz a vector
ndvi = NDVI.reshape(-1,1)
# entreno el clasificador con lso datos
kmeans.fit(ndvi)
# uso el modelo ajustado para poner etiquetas
etiquetas = kmeans.predict(NDVI.reshape(-1,1))

# visualizo los resultados recuperando la estructura bidimensional
plt.imshow(etiquetas.reshape(NDVI.shape))
plt.colorbar()
plt.show()
