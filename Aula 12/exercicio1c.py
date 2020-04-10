def letraA(palavra):
    contA = 0
    for letra in palavra:
        if letra == "a":
            contA+=1
    return contA             #Conta quantas vezes a letra "a" aparece na palavra

p = input("Informe uma palavra:")
print(letraA(p))  

    

