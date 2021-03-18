numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        raise RuntimeError('¡Qué moco!')
        #print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
