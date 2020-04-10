quantidade = int(input("Informe a quantidade de pizzas consumidas:"))
valorPizzas = quantidade*10.00
imposto = valorPizzas*0.08
valorTotal = valorPizzas+imposto
print("O cliente comprou ",quantidade," pizzas.")
print("Preço das pizzas R$",valorPizzas)
print("Preço do imposto R$",imposto)
print("Preço total R$",valorTotal)


