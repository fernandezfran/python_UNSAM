#### secuencias_binarias.py
#
# E 6.17: Complejidad de incrementar()
#
# E 6.18: Un ejemplo más complejo
#
def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


def listar_secuencias(n):
    """
    devuelve una lista con todas las secuencias (listas) binarias de longitud n,
    donde la primera es [0]*n y después utiliza la función incrementar.
    """
    l = []

    s = [0] * n
    l.append(s.copy())
    while (s != [1] * n):
        s = incrementar(s)
        l.append(s.copy())
    
    return l
