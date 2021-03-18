# E 2.7: Buscar precios
#
# quizás sería una mejor decisión pedir que devuelva la cadena
#   f'{fruta} ... {precio_fruta}'
# en vez del print()

def buscar_precio(fruta):
    
    precio_fruta = None
    file_precios = open('../Data/precios.csv', 'rt')
    for line in file_precios:
        columna = line.split(',')
        if (columna[0] == fruta): precio_fruta = float(columna[1])
    file_precios.close()

    if precio_fruta is None:
        print(f'{fruta} no figura en el listado de precios')
    else:
        print(f'El precio de la {fruta} es: {precio_fruta}')
