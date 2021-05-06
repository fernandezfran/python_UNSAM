#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis por medio de transformadas de Fourier
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal # para procesar señales


def calcular_fft(y, freq_sampleo = 24.0):
    """
    y debe ser un vector con números reales representando datos de una serie 
    temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.

    Devuelve dos vectores, uno de frecuencias y otro con la transformada
    propiamente. La transformada contiene los valores complejos que se 
    corresponden con respectivas frecuencias.
    """
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran


if __name__ == '__main__':
    # leo las mareas con pandas
    df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'],
                     parse_dates=True)

    # dentro de un lapso temporal entre inicio - fin, se seleccionan las alturas 
    #     de las mareas como arreglos de numpy
    inicio = '2014-01'
    fin    = '2014-06'
    alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
    alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

    # San Fernando
    freq_sf, fft_sf = calcular_fft(alturas_sf)
    
    pico_sf = signal.find_peaks(np.abs(fft_sf), prominence = 8)[0][-1]
    ang_sf = np.angle(fft_sf[pico_sf])
    ang_sf = ang_sf * 24 / (2 * np.pi * freq_sf[350])

    # Buenos Aires
    freq_ba, fft_ba = calcular_fft(alturas_ba)
    
    pico_ba = signal.find_peaks(np.abs(fft_ba), prominence = 8)[0][-1]
    ang_ba = np.angle(fft_ba[pico_ba])
    ang_ba = ang_ba * 24 / (2 * np.pi * freq_ba[350])

    print(f'La diferencia de altura entre las dos series temporales es de '
          f'{np.abs(fft_sf[0]) - np.abs(fft_ba[0])} cm\n')
    print(f'y el retardo de la onda de las mareas es de {(ang_ba - ang_sf) * 60} '
           'minutos')

    # espectro de potencias
    plt.xlabel("Frecuencia")
    plt.ylabel("Potencia (energía)")
    plt.xlim(0,4)
    plt.ylim(0,20)
    plt.plot(freq_sf, np.abs(fft_sf), label='SF', alpha=1.0)
    plt.plot(freq_ba, np.abs(fft_ba), label='BA', alpha=0.8)
    plt.scatter(freq_ba[pico_ba], np.abs(fft_ba)[pico_ba], facecolor='r')
    plt.scatter(freq_sf[pico_sf], np.abs(fft_sf[pico_sf]), facecolor='r')
    plt.legend()
    plt.show()
