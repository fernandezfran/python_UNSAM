### E 1.18: Geringoso rústico
#
# iterar sobre el string `cadena` para agregar la sílaba 'pa', 'pe', 'pi', 'po' o
# 'pu' según corresponda luego de cada vocal
#
# Aclaración: tiene problemas con las sílabas que, qui, gue, etc.
#
# cadena = 'Geringoso'
cadena = str(input("frase que se quiere decir en geringoso: "))
capadepenapa = ''

vocales = 'aeiou'
for c in cadena:
    if c in vocales:
        capadepenapa = capadepenapa + c + 'p' + c
    else:
        capadepenapa = capadepenapa + c

print(capadepenapa)
