a = int(input("Informe um valor:"))
b = int(input("Informe um valor:"))
c = int(input("Informe um valor:"))
somaAB = a + b
if somaAB > c:
    print ("A soma de A+B é igual a",somaAB,",que é maior que C que é",c)
elif somaAB < c:
    print ("A soma de A+B é igual a",somaAB,",que é menor que C que é",c)
elif somaAB == c:
    print ("A soma de A+B é igual a",somaAB,",que é igual ao valor de C que é",c)

