#### informe.py
#
# E 2.15: Lista de tuplas
#
# [edited] E 2.16: Lista de diccionarios
#
# [edited] E 2.17: Diccionarios como contenedores
#
# [edited - main] E 2.18: Balance
#
###############################    MODIFICACIÓN    ###############################
#
# E 3.9: función zip()
#
###############################    MODIFICACIÓN    ###############################
#
# E 3.13: Recolectar datos (función hacer_informe)
#
# E 3.14: Imprimir una tabla con formato
#
# E 3.15: Agregar encabezados
#
# E 3.16: Un desafío de formato
#
###############################    MODIFICACIÓN    ###############################
#
# E 6.4: Estructurar un programa como una colecciónde funciones
#
# E 6.5: Crear una función de alto nivel para la ejecución del programa
#
# E 6.11: Usemos el módulo fileparse
#
###############################    MODIFICACIÓN    ###############################
#
# E 7.2: función main
#
# E 7.3: script
#
import sys
import csv
import fileparse as fp
import informe_funciones

def main(argv):
    """
    función main que se ejecuta si el archivo es ejecutado de la terminal y que no
    lo hace si se lo importa
    """
    if (len(argv) != 3):
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} arch_camion arch_precios')
    else:
        informe_funciones.informe_camion(argv[1], argv[2])

if __name__ == '__main__':
    main(sys.argv)
