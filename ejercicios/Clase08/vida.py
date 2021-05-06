#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vida.py
import sys
from datetime import datetime, timedelta

def segundos_vividos(fecha_nacimiento):
    """
    Asumiendo que naciste a las 00:00hs de tu fecha de nacimiento, le pasas un str
    con el formato 'dd/mm/AAAA' de tu fecah de nacimiento y te devuelve la 
    cantidad de segundos que viviste
    """

    t_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    t_now        = datetime.now()
    
    delta = t_now - t_nacimiento
    
    return delta.total_seconds()


if __name__ == '__main__':
    
    nacimiento = sys.argv[1]
    segundos   = segundos_vividos(nacimiento)

    print(f'desde el {nacimiento} hasta ahora viviste {int(segundos)} segundos')
