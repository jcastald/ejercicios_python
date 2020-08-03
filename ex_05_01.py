num= None
tot= None
cont= None
while True:
    num=input("Introduzca un numero:")
    try:
        num=float(num)
        if tot is None:
            tot=num
            cont=1
        else:
            tot=tot+num
            cont=cont+1
    except:
        if num=="fin":
            break
        else:
            print("Entrada invalida")
            continue
print(tot,cont,tot/cont)

