#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#### figuritas.py
#
# # # # # # # # # Figuritas sueltas
#
# E  5.9: Crear (función crear_album(figus_total))
#
# E 5.10: Incompleto (función album_incomleto(A))
#
# E 5.11: Comprar (función comprar_figu(figus_total)
#
# E 5.12: Cantidad de compras (función cuantas_figus)
#
# E 5.13 y .14: main
#
# # # # # # # # # Figuritas en paquetes
#
# E 5.15: paquete de cinco figuritas
#
# E 5.16: función comprar_paquete(figus_total, figus_paquete)
#
# E 5.17: función cuantos_paquetes(figus_total, figus_paquete)
#
# E 5.18: main 
#
import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    """
    devuelve un álbum vacío en forma de un vector de largo figus total
    """

    return np.zeros(figus_total, dtype=np.intc)


def album_incompleto(A):
    """
    función que recibe un vector (álbum) y devuelve True si hay algún 0 en él,
    en el caso contrario devuelve False.
    """

    return 0 in A


def comprar_figu(figus_total):
    """
    recibe el número de figuritas total que tiene un álbum a través del parámetro
    figus_total y devuelve un número entero aleatorio que representa la figurita
    que toco (entre 0 y figus_total-1)
    """

    return random.randint(0, figus_total-1)


def cuantas_figus(figus_total):
    """
    dado el tamaño del álbum (figus_total) genera un álbum nuevo, simula su
    llenado y devuelve la cantidad total de figuritas que se debieron comprar
    para completarlo
    """
   
    A = crear_album(figus_total)

    i = 0
    chequeo = True
    while (chequeo):
        
        idx = comprar_figu(figus_total)
        A[idx] += 1

        chequeo = album_incompleto(A)
        i += 1

    return i


def comprar_paquete(figus_total, figus_paquete):
    """
    dado el tamaño del álbum y la cantidad de figuritas que vienen en un paquete
    devuelve una lista de figuritas al azar del tamaño del paquete
    """

    return [random.randint(0, figus_total-1) for i in range(figus_paquete)]


def cuantos_paquetes(figus_total, figus_paquete):
    """
    dado el tamaño del álbumy la cantidad de figus por paquete, genera un nuevo
    álbum, simula su llenado y devuelve la cantidad de paquetes que se debieron
    comprar para llenarlo
    """

    A = crear_album(figus_total)

    i = 0
    chequeo = True
    while (chequeo):

        lidx = comprar_paquete(figus_total, figus_paquete)

        for idx in lidx:
            A[idx] += 1

        chequeo = album_incompleto(A)
        i += 1

    return i


print(""" main : 5.14 """)
n_repeticiones = 100
figus_total = 670

l = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
l = np.array(l)

print(np.mean(l))
print()


print(""" main : 5.18 """)
n_repeticiones = 100
figus_total = 670
figus_paquete = 5

l = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
l = np.array(l)

print(np.mean(l))
print()


print(""" main : grafico el llenado """)

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
print()


print(""" main : optativos """)
n_repeticiones = 100
figus_total = 670
figus_paquete = 5

l = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
l = np.array(l)

print(f'E 5.19: el {100 * (l <= 850).sum() / n_repeticiones} % de los albunes se llenaron con la compra de menos de 850 paquetes')
print()


plt.hist(l, bins=25)
plt.title("E 5.20: Histograma")
plt.xlabel("nro de paquetes totales")
plt.show()


i = np.mean(l)
while ((l < i).sum() / n_repeticiones < 0.9): i += 5
print(f'E 5.21: para obtener más del 90 % de chances de completar el álbum se necesitan comprar {int(i):d} paquetes (tiene sentido, es el final de la cola superior de la gaussiana)')
print()


print(f'E 5.22: trivial (si no se repiten las figuritas, entonces el album se llena con la misma cantidad de compras de figuritas necesaria, si no hay paquetes, y si son paquetes, el nro de figuritas / nro de figuritas en el paquete)')
print()


print(f'E 5.23: cooperacion == album de n_cooperadores * cantidad de figuritas')
n_repeticiones = 100
amigues = 5
figus_total = 670 * amigues
figus_paquete = 5

ll = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
ll = np.array(ll)

print(f'En promedio, la cantidad de paquetes que tienen que comprar los {amigues} amigues es {ll.mean()}, que si lo dividimos por {amigues} nos da {ll.mean() / amigues:.2f} (comparar con {l.mean()} que compra 1 solo')
