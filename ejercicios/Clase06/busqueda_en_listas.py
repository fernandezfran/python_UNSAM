#### busqueda_en_listas.py
def busqueda_lineal_ordenada(lista, e):
    """
    Si e está en la lista devuelve su posición, de lo contrario devuelve -1.
    """
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:      # recorremos los elementos de la lista
        if z > e: break  # para si encuentra un número mayor a e
        if z == e:       # si encontramos a e
            pos = i      # guardamos su posición
            break        # y salimos del ciclo
        i += 1       
    return pos

def busqueda_binaria(lista, x, verbose = False):
    """
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """
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
    return pos
