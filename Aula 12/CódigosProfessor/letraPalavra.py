def apareceLetra(palavra,let):
    cont = 0
    for letra in palavra:
        if letra==let:
            cont+=1
    return cont

print(apareceLetra("programa","p"))
