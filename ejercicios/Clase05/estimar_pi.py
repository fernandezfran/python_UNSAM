#### pi.py
#
# E 5.4: Calcular pi
#
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x, y

def circulo(punto):
    x = punto[0]
    y = punto[1]
    if (x**2 + y**2 < 1): return True
    return False

N = 100000
M = sum([circulo(generar_punto()) for i in range(N)])
pi = 4 * M / N
print(pi)
