nota=input("Por favor introduzca una nota: ")
try:
    nota=float(nota)
    if nota>1.0 or nota<0:
        print("puntuacion incorrecta")
    elif nota<0.6:
        print("Insuficiente")
    elif nota>=0.6 and nota<0.7:
        print("Suficiente")
    elif nota>=0.7 and nota<0.8:
        print("Bien")
    elif nota>=0.8 and nota<0.9:
        print("Notable")
    else:
        print("Sobresaliente")
except:
    print("puntuacion incorrecta")