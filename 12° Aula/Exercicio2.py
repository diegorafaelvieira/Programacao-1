def funcaox(lista):
    tam  = len(lista)
    for i in range(0,tam):
        if lista[i]%2==0:
            lista[i] = "P"
        else:
            lista[i] = "I"
    return lista


L = [-10,11,4,33,15,22,1,145]
L = funcaox(L)
print(L)
