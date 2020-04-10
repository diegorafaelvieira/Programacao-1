peso = int(input("Digite a quantidade de KG pescado: "))
excesso = peso - 50
multa = 4.00

if peso > 50:
    multa = float(excesso * multa)
    print("Deverá pagar o valor de R${:.2f} de multa.".format(multa))
elif peso < 0:
    print("Valor inserido Inválido.")
elif peso <= 50:
    print ("Não precisa pagar multa")

