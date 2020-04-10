def letraA(palavra,letraEscolhida):
    contA = 0
    for letra in palavra:
        if letra == letraEscolhida:
            contA+=1
    return contA             

p = input("Informe uma palavra:")
letra = input("Informe a letra escolhida:")
print(letraA(p,letra))  
