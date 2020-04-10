while True:
    valor = int(input("Valor (de 120 à 1001):"))
    if valor>=120 and valor<1002:
        break
qtd=0
while valor>2:
    valor=valor/2
    qtd+=1
print(qtd)
