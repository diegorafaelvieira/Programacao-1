somaP = 0
qtdPares = 0
for  n in range(0,20):
    num = int(input("Informe o valor: "))
    if num > 0:
        somaP += num
    if num % 2 ==0:
        qtdPares +=1
print ("Total de números: ",somaP)
print ("Quantidade de números pares",qtdPares)
