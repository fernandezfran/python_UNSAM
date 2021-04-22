# documentacion.py
#
# E 7.8: Funciones y documentacion
#

def valor_absoluto(n):
    """
    Devuelve el valor absoluto de un número n.
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    """
    Recibe como argumento una lista y devuelve la suma de sus elementos que son
    pares
    """
    res = 0 # res es el invariante
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res


def collatz(n):
    """
    Recibe como argumento un número natural n, calcula la conjetura de collatz y
    devuelve la cantidad de pasos que le tomó llegar a n = 1.

    Pre : n debe ser mayor que 0
    Pos : modifica el valor de n (= 1)
    """
    res = 1 # res es el invariante

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
