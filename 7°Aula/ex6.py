val = int(input("Valor:"))
soma = val
maior = val
menor = val

for i in range(0,9):
    val = int(input("Valor:"))
    if val>maior:
        maior = val
    if val<menor:
        menor=val
    soma+=val

print("O maior valor é:",maior)
print("O menor valor é:",menor)
print("A média é:",(soma/10))
    
