#### diccionario_geringoso.py
#
# E 2.14: Diccionario geringoso

def diccionario_geringoso(lista_de_palabras):
    """
    devuelve un diccionario donde sus claves son las palabras de la lista
    y los valores son sus traducciones al geringoso rústico
    """

    d = {}
    for palabra in lista_de_palabras:
        papalapabrapa = ''
        for l in palabra:
            papalapabrapa += l
            if l in 'aeiou':
                papalapabrapa += 'p' + l

        d[palabra] = papalapabrapa

    return d


lista_prueba = ['banana', 'manzana', 'mandarina']
print(diccionario_geringoso(lista_prueba))
