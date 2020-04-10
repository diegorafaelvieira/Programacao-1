def converte (numero):
    binario = []
    resto = int(numero%2)
    binario.append(resto)
    numero = int (numero / 2)
    while numero > 1:
        resto = int(numero%2)
        binario.append(resto)
        numero = int(numero / 2)
    binario.append(numero)
    return binario[::-1]

lista = converte(39)
texto = ""
for x in lista:
    texto+=str(x)
print(texto)


    
#Ndecimal = int(input("Digite um número em Decimal: "))
#Nbinario = bin(Ndecimal)
#print("O número %d em Binário é: %s" % (Ndecimal,Nbinario[2:]))
    
#Fazer o contrário(receber em binário e passar para decimal)

# passar número para string (usar o comando "str")
