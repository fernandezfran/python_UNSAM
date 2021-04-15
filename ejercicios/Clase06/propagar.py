# Análisis de alternativas para `propagar.py`
#
# E 6.1: Propagar por vecinos
def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")
    print(f"Y obtuve  {l}")
    return m
#%%
propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])
#
#### PREGUNTAS
# 1. ¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino
#    no causan un IndexError en los bordes de la lista?
#    > porque hay una condición en el if i<n-1 e i>0, dependiendo del caso
#
# 2. ¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas 
#    perfectamente simétricas, no generan la misma cantidad de repeticiones de 
#    llamadas a la función propagar_al_vecino?
#    > porque la lista se recorre del primer elemento al último, entonces en el
#    > primer caso tiene que entre len(l) veces para propagar y en el segundo sólo
#    > una vez, ya que modifica todos los 0s a 1s en una sola pasada
#
# 3. Sobre la complejidad. Si te sale, calculá:
#    a) ¿Cuántas veces como máximo se puede repetir el ciclo while en una lista
#       de largo n?
#       > n veces.
#
#    b) ¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n?
#       > n, entra a los n elementos de la lista y opera sobre ellos (lineal)
#
#    c) Entonces, ¿cuántas operaciones hace como máximo esta versión de propagar 
#       en una lista de largo n? ¿Es un algoritmo de complejidad lineal o 
#       cuadrática?
#       > en el peor de los casos entre n veces a la lista y cada vez realiza n
#       > operaciones, por lo cual el algoritmo es cuadrático.
#
#
#
# E 6.2: Propagar como el auto fantastico
# (https://www.youtube.com/watch?v=oNeQi8-PXAU&t=11s&ab_channel=Juanjosecorredor)
#
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    m = l.copy()
    ld=propagar_a_derecha(m)
    lp=propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
#
#### PREGUNTAS
# 1. ¿Por qué se modificó la lista original?
#    > porque en ningún momento se hace una copia, se opera sobre ella.
#
# 2. ¿Por qué no quedó igual al estado propagado?
#    > porque cuando llama a la segunda función sí pasa otra lista distinta a l
#
# 3. Corregí el código para que no cambie la lista de entrada.
#    > done!
#
# 4. ¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de 
#    largo n?
#    > n veces
#
# 5. Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de 
#    operaciones en la longitud de la lista ¿Cuántas operaciones hace como máximo
#    propagar en una lista de largo n?
#    > 3 * n operaciones, 1 vez recorre n a la derecha, +1 para invertir, +1
#    > recorrerla invertida.
#
#
#
# E 6.3: Propagar con cadenas
#
def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps='x'.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
#
#### PREGUNTAS
# 1. ¿Por qué se acorta la lista?
#    > porque la divide cuando hay 'x' pero después en el join no introduce las
#    > 'x's
#
# 2. ¿Podés corregir el error agregando un solo caracter al código?
#    > Sí, cambiando la línea
#    > $ ps = ''.join(PW)
#    > por
#    > $ ps = 'x'.join(PW)
#
# 3. ¿Te parece que este algoritmo es cuadrático como el E 6.1 o lineal como el
#    E 6.2?
#    > parece lineal
