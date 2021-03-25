# solucion_de_errores.py
# Ejecricios de errores en el código
#%%
# E 3.1: Semántica
# Comentario: dentro del loop `while`, en la condición del `if`, no se consideraba
#     que la cadena de entrada a la función `expresion` tuviera A mayúscula. Por
#     lo cual fue reemplzada la línea:
#         if expresion[i] == 'a':
#     por:
#         if expresion[i] == 'aA':
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'aA':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2021')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%
# E 3.2: Sintaxis
# Comentario:
#     1. Hay un error de sintaxis en la condición del `if` ya que el signo
#        `=` se usa para asignar y en el condicional necesitamos usar `==` para 
#        comparar los dos valores.
#     2. Además, luego de la condición, es necesario agregar `:` en el lenguaje
#        de programación Python.
#     3. En `return Falso` Falso no está definido, la palabra correcta es False.
#     4. Ver el comentario al ejercicio anterior...
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'aA':
            return True
        i += 1
    return False

tiene_a('UNSAM 2021')
tiene_a('La novela 1984 de George Orwell')
#%%
# E 3.3: Tipos
# Comentario: Cuando se intenta llamar `tiene_uno(1984)` el valor de entrada es
#     un entero y lo que esperamos (por la condición del `if` y por los problemas
#     anteriores) es una cadena. Entonces, cuando se le quiere aplicar la función
#     len a un entero no es posible. Esto puede resolverse de dos formas, con
#     try / except como hemos visto en clase y en otros problemas o agregando
#     una condición `isinstance(expresion, str)` si esto es Falso (o sea, el
#     parámetro de entrada no es una cadena) entonces la función devuelve un False
def tiene_uno(expresion):
    if not (isinstance(expresion, str)):
        return False
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2021')
tiene_uno('La novecla 1984 de George Orwell')
tiene_uno(1984)
#%%
# E 3.4: Alcances
# Comentario: Las funciones, por default, devuelven en valor `None`, en este caso
#     no se especificó que la función suma tenía que devolver el valor de c, por
#     lo cual el print imprime:
#         La suma de 2 + 3 = None
#     esto se soluciona agregando un `return c` en la última línea de la función
def suma(a, b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a, b)
print(f"La suma de {a} + {b} = {c}")
#%%
# E 3.5: Pisando memoria
# Comentario: el diccionario `registro` era abierto al principio de la función,
#     para que la función devuelva la lista deseada hace falta crear un
#     diccionario vacío para cada fila, en caso contrario, como el encabezado es
#     siempre el mismo, la nueva fila pisa a la anteriores y agrega una nueva
#     por lo cual al final de la función se obtiene una lista con la cantidad de
#     diccionarios deseados pero cada uno de ellos con el último de los valores.
#     Al crear un nuevo diccionario para cada fila, evitamos solapar la nueva
#     fila con las anteriores.
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
