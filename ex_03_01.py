hr=input("Introduzca horas: ")
rt=input("Introduzca tarifa: ")
hr=float(hr)
rt=float(rt)
if hr>40:
    pago=(rt*40)+(1.5*rt*(hr%40))
else:
    pago=(rt*hr)
print("Salario: ",pago)