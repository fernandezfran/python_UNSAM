#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#### envido.py
#
# E 5.3: Envido
#
import random

def envido(mano):
    """
    dada una tupla que tenga el nro de la carta y el palo, calcula el envido
    correspondiente (0 si no tiene) y lo devuelve
    """
    
    # primer caso: todos los palos iguales
    if (mano[0][1] == mano[1][1]) and (mano[1][1] == mano[2][1]):

        # armo lista de valores sin contar 10, 11, 12
        l = [ mano[i][0] for i in range(0, 3) if mano[i][0] < 10]
       
        if len(l) == 0: # ie 10 11 12
            m = 0
        elif len(l) == 1:
            m = l[0]
        elif len(l) == 2:
            m = sum(l)
        else:
            m = max(l)
            l.pop(l.index(max(l)))
            m += max(l)

        return 20 + m

    # segundo caso: solo dos palos iguales
    m = 0
    if (mano[0][1] == mano[1][1]):

        if (mano[0][0] < 10): m += mano[0][0]
        if (mano[1][0] < 10): m += mano[1][0]
        
        return 20 + m
    
    elif (mano[0][1] == mano[2][1]):

        if (mano[0][0] < 10): m += mano[0][0]
        if (mano[2][0] < 10): m += mano[2][0]
        
        return 20 + m

    elif (mano[1][1] == mano[2][1]):
        
        if (mano[1][0] < 10): m += mano[1][0]
        if (mano[2][0] < 10): m += mano[2][0]
        
        return 20 + m
    
    else: # tercer caso: sin envido

        return 0


""" main """
N = 100000

#armo el mazo
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

e31 = 0
e32 = 0
e33 = 0
for i in range(N):
    random.shuffle(naipes) # mezclo
    mano = naipes[-3:]     # elijo las 3 cartas de arriba
    envrido = envido(mano) # calculo el envido

    if (envrido == 31): e31 += 1
    if (envrido == 32): e32 += 1
    if (envrido == 33): e33 += 1

print(f'la probabilidad de que salga 31 es {100 * e31 / N:.6f} %')
print(f'la probabilidad de que salga 32 es {100 * e32 / N:.6f} %')
print(f'la probabilidad de que salga 33 es {100 * e33 / N:.6f} %')
