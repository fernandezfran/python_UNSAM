#### plot_bbin_vs_bsec.py
#
# E 6.19: Contar comparaciones en la búsqueda binaria
#
import random
import numpy as np
import matplotlib.pyplot as plt

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l


def generar_elemento(m):
    return random.randint(0, m-1)


def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria_(lista, x, verbose = False):
    """
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Además devuelve la cantidad de comparaciones que hace la función.
    """
    comps = 0 # inicializo en cero la cantidad de comparaciones
    
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        comps += 1 # sumo la comparación que estoy por hacer
    return pos, comps


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

m = 10000
k = 1000

largos = np.arange(256) + 1 # los largos de listas que voy a usar
comps_promedio_s = np.zeros(256) # aca guardo el promedio de comparaciones 
comps_promedio_b = np.zeros(256) # aca guardo el promedio de comparaciones 
for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_s[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_b[i] = experimento_binario_promedio(lista, m, k)

plt.xscale("log")
plt.yscale("log")
plt.plot(largos, comps_promedio_s, label='Busqueda secuencial')
plt.plot(largos, comps_promedio_b, label='Busqueda binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Busqueda")
plt.legend()
plt.show()
