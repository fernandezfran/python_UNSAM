#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#### generala.py
#
# E 5.1: Generala servida (funciones tirar() y es_generala(tirada))
#
# E 5.2: Generala no necesariamente servida (modifico funciones para que
#           consideren hasta 3 tiradas)
#
import random

def tirar(n_dados):
    """
    devuelve una lista con n_dados dados generados aleatoriamente
    """

    tirada = [random.randint(1,6) for i in range(n_dados)]

    return tirada


def es_generala(tirada):
    """
    devuelve True si y sólo si los cinco dados de la lista tirada son iguales
    """
    
    a = tirada[0]
    for dado in tirada:
        if dado != a: return False
        a = dado

    return True


def guardo(tirada):
    """
    devuelve una lista con los valores que coinciden de una tirada
    """

    cuenta = [0] * 6
    for dado in tirada:
        cuenta[dado - 1] += 1
  
    l = []
    dado_max = cuenta.index(max(cuenta)) + 1
    for dado in tirada:
        if dado == dado_max: l.append(dado)

    return l


""" main """
N = 100000 # ó 1000000

print(""" E 5.1 : generala servida """)
G = sum([es_generala(tirar(5)) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {100 * prob:.6f} %')
print()


print(""" E 5.2 : generala no necesariamente servida """)
G = []
for k in range(N):

    l = [] 
    n = 5
    i = 0
    while (i < 3):
        dados = tirar(n)
        dados = dados + l
        check = es_generala(dados)
        if check == True: break

        l = guardo(dados)

        n = 5 - len(l)

        i += 1
    
    G.append(check)

prob = sum(G) / N

print(f'Tiré {N} veces, de las cuales {sum(G)} saqué generala en, como máximo, tres tiradas')
print(f'Podemos estimar la probabilidad de sacar generala en tres tiros como {100 * prob:.6f} %')
