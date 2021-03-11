### E 1.29: Traductor (rústico) al lenguaje inclusive
#
# Queremos hacer un traductor que cambie las palabras masculinas de una frase por
# su versión neutra. Como primera aproximación, completá el siguiente código para 
# reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter 
# de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' pasaría a
# ser 'todes somes programadores'. Guardá tu código en el archivo `inclusive.py`
#
# Falla si hay una coma al final de la palabra, e.g. 'Todos, tu también', lo mismo
# si la palabra termina con una 'o' y un signo de pregunta '?', i.e. si intriduzco
# 'infinito?', esto pasa a 'infinite?'
#
frase = str(input('frase que se quiere pasar a inclusive: '))
palabras = frase.split()

palabras_inclusivas = []
for palabra in palabras:

    if len(palabra) > 1:
        palabra = list(palabra)
        if (palabra[-2] == 'o'):
            palabra[-2] = 'e'
        palabra = ''.join(palabra)
    
    palabras_inclusivas.append(palabra)

frase_inclusiva = ' '.join(palabras_inclusivas)
print(frase_inclusiva)
