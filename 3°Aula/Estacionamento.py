m = int(input("Informe a quantidade de minutos:"))
if m <= 15:
    print("Grátis")
elif m>15 and m<= 60:
    print("R$5.40")
else:
    hora = int(m/60)
    preco = (6.2+(hora-1)*1.2)
    print(preco)
           
