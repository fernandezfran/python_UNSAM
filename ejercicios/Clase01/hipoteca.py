### Ejercicio de hipoteca
#
# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija
# nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de 
# $2684,11.
#
# Bonus : 
#   .9  David agrega $1000 por mes durante 4 años, comenzando en el sexto año
#   .10 Imprime tabla: mes, total pagado hasta el momento, saldo restante
#   .11 El pago del último mes se ajusta a lo adeudado
#
saldo = 500000
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra = 1000.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

mes = 0
while saldo > 0:
    
    mes = mes + 1
    
    if (mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
        pago_mensual_ef = pago_mensual + pago_extra
    else:
        pago_mensual_ef = pago_mensual
    if (pago_mensual > saldo * (1 + tasa/12)): 
        pago_mensual_ef = saldo * (1 +tasa/12)

    saldo = saldo * (1 + tasa/12) - pago_mensual_ef
    total_pagado = total_pagado + pago_mensual_ef
    
    print(mes, round(total_pagado,2), round(saldo,2))
    
print(f'David pagó ${total_pagado:0.2f} en {mes} meses')
