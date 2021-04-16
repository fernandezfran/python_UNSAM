#### bbin.py
#
# E 6.14: Búsqueda binaria
#
# E 6.15: Insertar un elemento en una lista
#
def donde_insertar(lista, x, verbose = False):
    """
    Precondición: la lista está ordenada
    devuelve la posición de x en la lista, si no se encuentra, dice la posición
    en la que se podría insertar para que la lista permanezca ordenada.
    """
    
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    
    izq = 0
    der = len(lista) - 1
    while izq <= der:

        medio = (izq + der) // 2
        
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break
        
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    return medio


def insertar(lista, x):
    """
    Precondición: la lista está ordenada
    Si el elemento x se encuentra en la lista, solamente devuelve su posición;
    si no se encuentra en la lista, lo inserta en la posición correcta para
    mantener el orden
    """

    idx = donde_insertar(lista, x)
    
    if (x == lista[idx]):
        pass
    elif (x > lista[idx]):
        idx += 1
        lista.insert(idx, x)
    else:
        lista.insert(idx, x)

    return idx
