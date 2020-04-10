def funcaox(lista):
    tam  = len(lista)
    novaLista = []
    for i in range(0,tam):
        if lista[i]%2==0:
            novaLista.append(lista[i])
    return novaLista

L = [-10,11,4,33,15,22,1,145]
L = funcaox(L)
print(L)
