### E 1.12: Expresiones regulares
texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020.'
# Encontrar las apariciones de una fecha en el texto
import re
print(re.findall(r'\d+/\d+/\d+', texto))
# ['6/8/2020', '7/8/2020']
# Reemplazá esas apariciones, cambiando el formato
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto))
# 'Hoy es 2020-8-6. Mañana será 2020-8-7.'
