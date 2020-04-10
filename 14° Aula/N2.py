temperatura = []
meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

for x in range (0,12):
    t = float(input("Informe a temperatura:"))
    temperatura.append(t)


soma = 0.0
for tempMes in temperatura:
    soma+=tempMes

media = soma/len(temperatura)
print ("A média anual é de :",media,"graus")

for x in range (0,12):
    if temperatura[x] > media:
        print(temperatura[x], " - ",meses[x])
        

