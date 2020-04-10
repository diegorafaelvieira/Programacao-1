def calculaMulta(velocidade):
    if velocidade>50 and velocidade<=55:
        return 230
    elif velocidade >55 and velocidade<=60:
        return 340
    elif velocidade >60:
        valor = (velocidade-50)*19.28
        return valor
    else:
        return 0
    
vel = int(input("Informe a velocidade:"))    
print(calculaMulta(vel))
        
