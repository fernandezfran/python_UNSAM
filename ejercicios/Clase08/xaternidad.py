#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" xaternidad.py
Una licencia de xaternidad empieza el 26 de septiembre de 2020 y dura 200 días
¿qué día te reincorporás al trabajo?
"""
from datetime import datetime, timedelta

t_start    = datetime(2021, 9, 26)
t_licencia = timedelta(days = 200)

t_vuelta = t_start + t_licencia 

print(f'volves a trabajar el {t_vuelta.day}/{t_vuelta.month}/{t_vuelta.year}')
