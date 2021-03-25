#### arboles.py
#
# E 3.18 Lectura de los árboles de un parque (leer_parque)
#
# E 3.19: Determinar las especies de un parque (especies)
#
# E 3.20: Contar ejemplares por especies (contar_ejemplares)
#
# E 3.21: Alturas de una especie en una lista (obtener_alturas)
# 
# E 3.22: Inclinaciones por especie de una lista (obtener_inclinaciones)
#
# E 3.23: Especie con el ejemplar más inclinado (especimen_mas_inclinado)
#
# E 3.24: Especie más inclinada en promedio (especie_promedio_mas_inclinada)
#
import sys
import csv
from collections import Counter

from pprint import pprint


def leer_parque(nombre_archivo, parque):
    """
    abre un archivo .csv con la información de la distribución del arbolado en los
    parques de una ciudad y devuelve una lista de diccionarios donde cada uno de
    ellos tiene información sobre un árbol en particular de ese parque
    """

    with open(nombre_archivo, 'rt') as f:

        filas       = csv.reader(f)
        encabezados = next(filas)
       
        ldd = [] # lista de diccionarios
        for fila in filas:
        
            arbol = dict(zip(encabezados, fila))
            
            if arbol['espacio_ve'] == parque:

                arbol['altura_tot'] = float(arbol['altura_tot'])
                arbol['inclinacio'] = float(arbol['inclinacio'])
                ldd.append(arbol)
    
    return ldd


def especies(lista_arboles):
    """
    lee una lista de árboles y devuelve un conjunto de especies
    """

    lde = [] # lista de especies
    for arbol in lista_arboles:

        lde.append(arbol['nombre_com'])

    sde = set(lde) # conjunto de especies (sin repeticiones)

    return sde 


def contar_ejemplares(lista_arboles):
    """
    lee una lista de árboles y devuelve un diccionario en el que las especies son
    las claves y los valores asociados son la cantidad de ejemplares de dicha 
    especie en la lista que se está dando
    """

    cantidad = Counter()
    for arbol in lista_arboles:
        
        cantidad[arbol['nombre_com']] += 1

    return cantidad 


def obtener_alturas(lista_arboles, especie):
    """
    lee una lista de árboles, una especie particular de árbol y devuelve una lista
    con las alturas de los ejemplares de esa especie en la lista
    """

    lca = [] # lista con alturas
    for arbol in lista_arboles:
        
        if (arbol['nombre_com'] == especie): lca.append(arbol['altura_tot'])

    return lca


def obtener_inclinaciones(lista_arboles, especie):
    """
    lee una lista de árboles, una especie particular de árbol y devuelve una lista
    con las inclinaciones de los ejemplares de esa especie en la lista
    """

    lci = [] # lista con inclinaciones
    for arbol in lista_arboles:
        
        if (arbol['nombre_com'] == especie): lci.append(arbol['inclinacio'])

    return lci


def especimen_mas_inclinado(lista_arboles):
    """
    lee una lista de árboles y devuelve la especie que tiene el ejemplar más
    inclinado y su inclinación
    """
    
    especies_parque = especies(lista_arboles) # conjunto de especies

    inc_max = 0.0
    for especie in especies_parque:
        
        inc = obtener_inclinaciones(lista_arboles, especie)
        inc_M = max(inc)
        if (inc_M > inc_max):
            especie_inc = especie
            inc_max = inc_M

    return especie_inc, inc_max


def especie_promedio_mas_inclinada(lista_arboles):
    """
    lee una lista de árboles y devuelve la especie que en promedio tiene la mayor
    inclinación y el promedio calculado
    """
    
    especies_parque = especies(lista_arboles) # conjunto de especies

    inc_max = 0.0
    for especie in especies_parque:
        
        inc = obtener_inclinaciones(lista_arboles, especie)
        inc_prom = sum(inc) / len(inc)
        if (inc_prom > inc_max):
            especie_inc = especie
            inc_max = inc_prom

    return especie_inc, inc_max


""" main """

datos = '../Data/arbolado-en-espacios-verdes.csv'

print("Ejercicio 3.18:")
pq = 'GENERAL PAZ'
pql = leer_parque(datos, pq)
print(f'el largo obtenido para la lista ({len(pql)}) coincide con el los 690 árboles que el ejercicio dice que hay')
print("\n")


print("Ejercicio 3.19")
pq = 'GENERAL PAZ'
pql = leer_parque(datos, pq)
epql = especies(pql)
print(epql)
print("\n")


print("Ejercicio 3.20")
PARQUES = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
for parque in PARQUES:
    
    pl = leer_parque(datos, parque)
    if (len(pl) == 0): sys.exit("El parque ingresado no se encuentra en la base "
                                "de datos")

    cpl = contar_ejemplares(pl)
    print(f'Las cinco especies más frecuentes en el parque {parque} son')
    pprint(cpl.most_common(5))
print("\n")


print("Ejercicio 3.21")
print("Parque | altura promedio | altura máxima")
PARQUES = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
for parque in PARQUES:
    pl = leer_parque(datos, parque)
    if (len(pl) == 0): sys.exit("El parque ingresado no se encuentra en la base "
                                "de datos")
    
    alturas = obtener_alturas(pl, 'Jacarandá')
    altura_max = max(alturas)
    altura_prom = sum(alturas) / len(alturas) 

    print(f'{parque} {altura_max} {round(altura_prom,2)}')
print("\n")


print("Ejercicio 3.22")
pl = leer_parque(datos, 'CENTENARIO')
pprint(obtener_inclinaciones(pl, 'Jacarandá'))
print("\n")

print("Ejercicio 3.23")
PARQUES = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
for parque in PARQUES:
    
    pl = leer_parque(datos, parque)
    
    print(especimen_mas_inclinado(pl))

print("\n")


print("Ejercicio 3.24")
PARQUES = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
for parque in PARQUES:
    
    pl = leer_parque(datos, parque)
    
    print(especie_promedio_mas_inclinada(pl))

print("\n")
print("\n")
