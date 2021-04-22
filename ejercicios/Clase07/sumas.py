# sumas.py
#
# E 7.6: Sumas
#     i. con cíclo
#
# E 7.7: el invariante es la variable `suma`
#
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    for i in range(desde, hasta):
        suma += i
    return suma
