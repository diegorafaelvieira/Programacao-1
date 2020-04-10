#CRIANDO UMA LISTA QUE MOSTRA SOMENTE VALORES PARES!

a = [0,3,7,5,4,2,9]
c = len(a) - 1

while c >= 0:
    if a[c] % 2 == 0:
        print(a[c])
    c -= 1
