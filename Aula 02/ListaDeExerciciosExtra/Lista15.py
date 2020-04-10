valor = float(input("Informe o valor da hora trabalhada R$:"))
hora = int(input("Informe o números de horas trabalhadas no mês:"))
salarioBruto = valor * hora

ir = salarioBruto * 0.11

inss = salarioBruto * 0.08

sindicato = salarioBruto * 0.05

salarioLiquido = (salarioBruto - (ir + inss + sindicato))
print ("O salário Bruto é:R$ ",salarioBruto)
print ("O valor descontado pelo Imposto de Renda é: R$",ir)
print ("O valor descontado pelo INSS é: R$",inss)
print ("O valor descontado pelo Sindicato é: R$",sindicato)                  
print ("O salário Liquido é: R$",salarioLiquido)
