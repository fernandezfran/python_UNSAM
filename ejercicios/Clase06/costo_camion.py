#### costo_camion.py
#
# E 2.2: Lectura de un archivo de datos
#
# [edited] E 2.6: Transformar el script a una función
#
# [edited] E 2.8: Administración de errores
#
# [edited] E 2.9: Funciones de la biblioteca
#
###############################    MODIFICACIÓN    ###############################
#
# E 6.12: Un poco más allá
#
import informe_funciones as informe

def costo_camion(file_camion):
    camion = informe.leer_camion(file_camion)
    
    costo = 0
    for fruta in camion:
        costo += fruta['cajones']*fruta['precio']

    return costo

costo = costo_camion('../Data/camion.csv')
print("Costo total", costo)
