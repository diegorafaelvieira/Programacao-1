quantidade = 0
for i in range(0,1000001,1): #menor valor,menor que o segundo valor(imprime até 1000000),de 1 em 1
    if i%7==0 and i%2!=0:
        quantidade+=1
print(quantidade)         
