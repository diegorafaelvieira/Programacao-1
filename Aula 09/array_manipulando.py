#Iniciando um array vazio
lista = []

#Iniciando um array com valores
lista2 = [2,"texto",3.4,True]
lista3 = [1,2,3,4,5]

#Acessando os valores de um array
print(lista2[3])

#Igualando arrays
lista = lista2

print(lista)
print(lista2)

#Igualando arrays
lista = lista3[:]

print(lista)
print(lista2)

#Modificando arrays
lista[2] = 10

print(lista)

#Adicionando elementos em um array
lista.append(4)

print(lista)

#Adicionando elementos de um array em outro
lista.extend(lista2)
print(lista)

#Removendo elemento de um array
del lista[-1]

#Fatiamento de arrays

#-1 indica o último elemento
print(lista[-1])

#Pode-se determinar um intervalo que deve ser exibido
print(lista[0:-1])

print(lista[1:4])

print(lista[:4])

print(lista[3:])



