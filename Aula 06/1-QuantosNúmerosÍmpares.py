contador = 0
contadorAchou = 0
while True:
    if contador==1000000:
        break
    if contador%7==0 and contador%2!=0:
        contadorAchou+=1
    contador+=1    
print(contadorAchou)
