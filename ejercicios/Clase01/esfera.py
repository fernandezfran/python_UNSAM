### E 1.13: El volumen de una esfera
#
# pide el rado `r` de una esfera y calcula el volumen de la misma.
# Sugerencia: recorda que V_E = 4/3 pi r^3
#
import math

r = float(input("el radio de la esfera es: "))
V = (4 / 3) * math.pi * r**3
print("entonces su volumen es:", V)
