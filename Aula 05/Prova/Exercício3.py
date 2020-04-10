v1 = float(input("Informe o 1° valor:"))
v2 = float(input("Informe o 2° valor:"))
op = float(input("Informe a operação desejada:(1)Soma,(2)Subtração,(3)Multiplicação ou (4)Divisão:"))
c1 = (v1+v2)
c2 = (v1-v2)
c3 = (v1*v2)
c4 = (v1/v2)
if op == 1 and  c1 >= 0 and c1 % 2 == 0: #SOMA/Positivo/Par
    print("O resultado da operação é: ",c1,"valor positivo e par")
elif op == 1 and c1 < 0 and c1 % 2 == 0: #SOMA/Negativo/Par
    print("O resultado da operação é: ",c1,"valor negativo e par")
elif op == 1 and c1 >= 0 and c1 % 2 != 0:#SOMA/Positivo/Ímpar
    print("O resultado da operação é: ",c1,"valor positivo e ímpar")
elif op == 1 and c1 < 0 and c1 % 2 != 0: #SOMA/Negativo/Ímpar
    print("O resultado da operação é: ",c1,"valor negativo e ímpar")
elif op == 2 and c2 >= 0 and c2 % 2 == 0: #SUBTRAÇÃO/Positivo/Par
    print("O resultado da operação é: ",c2,"valor positivo e par")
elif op == 2 and c2 < 0 and c2 % 2 == 0: #SUBTRAÇÃO/Negativo/Par
    print("O resultado da operação é: ",c2,"valor negativo e par")
elif op == 2 and c2 >= 0 and c2 % 2 != 0: #SUBTRAÇÃO/Positivo/Ímpar
    print("O resultado da operação é: ",c2,"valor positivo e ímpar")
elif op == 2 and c2 < 0 and c2 % 2 != 0: #SUBTRAÇÃO/Negativo/Ímpar
    print("O resultado da operação é: ",c2,"valor negativo e ímpar")
elif op == 3 and c3 >= 0 and c3 % 2 == 0: #MULTIPLICAÇÃO/Positivo/Par
    print("O resultado da operação é: ",c3,"valor positivo e par")
elif op == 3 and c3 < 0 and c3 % 2 == 0: #MULTIPLICAÇÃO/Negativo/Par
    print("O resultado da operação é: ",c3,"valor negativo e par")
elif op == 3 and c3 >= 0 and c3 % 2 != 0: #MULTIPLICAÇÃO/Positivo/Ímpar
    print("O resultado da operação é: ",c3,"valor positivo e ímpar")
elif op == 3 and c3 < 0 and c3 % 2 != 0: #MULTIPLICAÇÃO/Negativo/Ímpar
    print("O resultado da operação é: ",c3,"valor negativo e ímpar")
elif op == 4 and c4 >= 0 and c4 % 2 == 0: #DIVISÃO/Positivo/Par
    print("O resultado da operação é: ",c4,"valor positivo e par")
elif op == 4 and c4 < 0 and c4 % 2 == 0: #DIVISÃO/Negativo/Par
    print("O resultado da operação é: ",c4,"valor negativo e par")
elif op == 4 and c4 >= 0 and c4 % 2 != 0: #DIVISÃO/Positivo/Ímpar
    print("O resultado da operação é: ",c4,"valor positivo e ímpar")
elif op == 4 and c4 < 0 and op % 2 != 0: #DIVISÃO/Negativo/Ímpar
    print("O resultado da operação é: ",c4,"valor negativo e ímpar")          
          
          
