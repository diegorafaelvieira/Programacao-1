def menor(val):
lista=[]
    for i in range(0,9):
        val = input (int("Informe um valor:"))
        if val<menor:
            menor = val

val = int(input("Valor:"))
print("O menor valor é:",(menor(val)))
