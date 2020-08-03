num= None
mayor= None
menor= None
while True:
    num=input("Introduzca un numero:")
    try:
        num=float(num)
        if mayor is None:
            mayor=num
        elif mayor<num:
            mayor=num
        if menor is None:
            menor=num
        elif menor>num:
            menor=num
    except:
        if num=="fin":
            break
        else:
            print("Entrada invalida")
            continue
print(mayor,menor)

