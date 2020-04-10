
l = []

for i in range(0,10):
    n = input("Informe um nome:")
    l.append(n)

n2 = input("INFORME OUTRO NOME: ")

achei = False

for aux in l:
    if aux == n2:
        achei = True

if achei == True:
    print("ACHEI!")
else:
    print("NÃO ACHEI!")
    
