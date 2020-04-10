i = int(input("Informe o número do item:"))
q = int(input("Informe a quantidade:"))
if i == 100:
    print("O item escolhido foi Cachorro Quente e o valor total é:R$",q * 1.10)
elif i == 101:
    print("O item escolhido foi Bauru Simples e o valor total é:R$", q * 1.30)
elif i == 102:
    print("O item escolhido foi Bauru c/Ovo e o valor total é:R$", q * 1.50)
elif i == 103:
    print("O item escolhido foi Hambúrguer e o valor total é:R$", q * 1.10)
elif i == 104:
    print("O item escolhido foi Cheeseburguer e o valor total é:R$", q * 1.30)
elif i == 105:
    print("O item escolhido foi Refrigerante e o valor total é:R$", q * 1.00)
else:
    print("Item não encontrado no menu")
