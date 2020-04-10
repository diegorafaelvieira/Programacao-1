n = int(input("Informe o número da conta:"))
saldo = float(input("Informe o saldo da conta:"))
op = int(input("Informe a operação:(1)Depósito ou (0)Retirada:"))
valor = float(input("Informe o valor:"))
saldoDeposito = saldo + valor  #Saldo atual mais valor depositado
saldoRetirada = saldo - valor  #Saldo atual menos valor retirado
if op == 1:
    print("O saldo atual é:R$",saldoDeposito)
elif op == 0:
    print("O saldo atual é:R$",saldoRetirada)
else:
    print("Operação inválida!Digite (1)Depósito ou (0)Retirada")

