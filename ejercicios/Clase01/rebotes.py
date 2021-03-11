# rebotes.py
#
# Archivo de ejemplo
#
### Ejercicio
#
# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que 
# toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa 
# `rebotes.py` que imprima una tabla mostrando las alturas que alcanza en cada 
# uno de sus primeros diez rebotes.
#
### output esperado:
#
# 1 60.0
# 2 36.0
# 3 21.599999999999998
# 4 12.959999999999999
# 5 7.775999999999999
# 6 4.6655999999999995
# 7 2.7993599999999996
# 8 1.6796159999999998
# 9 1.0077695999999998
# 10 0.6046617599999998
#
altura = 100    # metros

i = 0
while (i < 10):
    altura = (3/5) * altura
    i = i + 1
    print(i, round(altura, 4))
