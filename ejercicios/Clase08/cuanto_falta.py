#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" cuanto_falta.py
¿Cuántos días faltan desde hoy hasta la próxima primavera?
"""
from datetime import datetime, timedelta

t_now  = datetime.now()
t_next = datetime(t_now.year, 9, 21)

spring = (t_next - t_now).days

if spring > 0:
    print(f'faltan {(t_next - t_now).days} días para la primavera')
else:
    print(f'la primavera de este año ya empezó')
