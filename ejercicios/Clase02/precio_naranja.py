# E 2.3: Precio de la naranja

file_precios = open('../Data/precios.csv', 'rt')

for line in file_precios:
    columna = line.split(',')
    if (columna[0] == 'Naranja'): precio_naranja = columna[1]

file_precios.close()

print("El precio de la naranja es:", precio_naranja)
