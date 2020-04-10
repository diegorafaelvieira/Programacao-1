qtd10_100=0
soma=0
qtdPares_100=0
for x in range(0,1000):
    valor = int(input("Informe o valor:"))
    if valor>10 and valor<100:
        qtd10_100+=1
        soma+=valor
    if valor>100 and valor%2==0:
        qtdPares_100+=1
print("Números pares e maiores do que 100:",qtdPares_100)
print("Números maiores que 10 e menores que 100:",(soma/qtd10_100))
