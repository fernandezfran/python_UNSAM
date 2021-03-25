#### tablamult.py
#
# E 3.17: Tablas de multiplicar

print('      0   1   2   3   4   5   6   7   8   9')
print(f'{"-":-^44s}')

for i in range(10):
    tabla_i = f'{i:d}: '
    m = 0
    for j in range(10):
        tabla_i += f'  {m:>2d}'
        m += i
    print(tabla_i)
