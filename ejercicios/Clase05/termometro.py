#### termometro.py
#
# E 5.7: amplio el script inicial para guardar las temperaturas
#
import random
import numpy as np

media = 0.0
desviacion = 0.2 # grados

T = 37.5

n = 999

temperaturas = []
for i in range(n):
    temp = random.normalvariate(T + media, desviacion)
    temperaturas.append(temp)
    print(temp)

temperaturas = np.array(temperaturas)
np.save('../Data/Temperaturas', temperaturas)

print(f'El máximo es   : {np.max(temperaturas):.2f}')
print(f'El mínimo es   : {np.min(temperaturas):.2f}')
print(f'El promedio es : {np.mean(temperaturas):.2f}')
print(f'La mediana es  : {np.median(temperaturas):.2f}')
