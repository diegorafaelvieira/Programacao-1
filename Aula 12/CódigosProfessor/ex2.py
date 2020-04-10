def letraA(palavra):
    contA = 0
    for letra in palavra:
        if letra=="a":
            contA+=1
    return contA

p = input("Informe uma palavra:")
print(letraA(p))
