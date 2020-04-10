while True:
    v1 = int(input("Valor 1:"))
    v2 = int(input("Valor 2:"))
    operacao = input("Informe soma, div, mult, sub ou sair:")
    if operacao == "sair":
        break
    elif operacao=="soma":
        print("Resultado:",v1+v2)
    elif operacao=="div":
        print("Resultado:",v1/v2)
    elif operacao=="mult":
        print("Resultado:",v1*v2)
    else:
        print("Resultado:",v1-v2)
print("FIM")        
