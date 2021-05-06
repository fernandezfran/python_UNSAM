#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" arbolado_parques_veredas.py
Comparando especies en parques y en veredas
===========================================
+ Este programa analiza las diferencias entre los ejemplares de una misma especie
según si crecen en parques o en veredas.
+ El mismo realiza un boxplot del diámetro a la altura del pecho de las Tipas 
(_tipuana tipu_).
"""
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns


#### (1) lectura de archivos de parque y vereda en DataFrames
dir_data = '../Data'
archivo_parque = 'arbolado-en-espacios-verdes.csv'
archivo_vereda = 'arbolado-publico-lineal-2017-2018.csv'

f_parque = os.path.join(dir_data, archivo_parque)
f_vereda = os.path.join(dir_data, archivo_vereda)

df_parques = pd.read_csv(f_parque)
df_veredas = pd.read_csv(f_vereda)


#### (2) selecciono las Tipas la información de interés y la renombro
cols = ["altura", "diametro"]
cols_parque = ['altura_tot', 'diametro']
cols_vereda = ['altura_arbol', 'diametro_altura_pecho']

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][
                             cols_parque].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][
                             cols_vereda].copy()

df_tipas_parques = df_tipas_parques.rename(columns={cols_parque[0]: cols[0]})
df_tipas_veredas = df_tipas_veredas.rename(columns={cols_vereda[0]: cols[0],
                                                    cols_vereda[1]: cols[1]})


#### (3) Agregar una columna 'ambiente' que diga 'parque' y 'vereda'
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'


#### (4) Junto ambos DataFrames en uno solo
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])


#### (5) boxplot diametro a la altura del pecho distinguiendo por el ambiente
df_tipas.boxplot("diametro", by='ambiente')
plt.show()


#### (6) boxplot altura distinguiendo por el ambiente
df_tipas.boxplot("altura", by='ambiente')
plt.show()
