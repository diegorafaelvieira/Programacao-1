nome = input ("Informe o nome:")
d = int(input("Informe o número de dias:"))
if d > 15:
    print ("O valor da diária de",nome,"é de:R$",((d * 5.50)+60.00))
elif d == 15:
    print ("O valor da diária de",nome,"é de:R$",((d * 6.00)+60.00))
elif d < 15:
    print ("O valor da diária de",nome,"é de:R$",((d * 8.00)+60.00))
