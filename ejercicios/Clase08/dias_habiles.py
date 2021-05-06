#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

def dias_habiles(inicio, fin, feriados=[]):
    """
    calcula los días hábiles entre dos fechas

    Parametros
    ----------
    inicio   : str (dd/mm/AAAA)
        dia inicial
    fin      : str (dd/mm/AAAA)
        dia final
    feriados : lista 
        de fechas correspondientes a los feriados que haya dentro del lapso

    Devuelve
    --------
    la cantidad de días hábiles
    """

    dia  = datetime.strptime(inicio, '%d/%m/%Y') 
    last = datetime.strptime(fin, '%d/%m/%Y')
    feriad = []
    for feriado in feriados:
        feriad.append(datetime.strptime(feriado, '%d/%m/%Y'))

    dias = 1
    while (dia != last):

        try:
            dia = datetime(dia.year, dia.month, dia.day + 1)
        except ValueError:
            try:
                dia = datetime(dia.year, dia.month + 1, 1)
            except ValueError:
                dia = datetime(dia.year + 1, 1, 1)

        if (dia in feriad) or (dia.weekday() in [5, 6]): continue

        dias += 1

    return dias


if __name__ == '__main__':
    feriados= ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
    d = dias_habiles('10/10/2020', '31/12/2020', feriados)
    print(d)
