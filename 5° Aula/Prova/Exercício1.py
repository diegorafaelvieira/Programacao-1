augusto1 = int(input("Augusto informe o primeiro valor (1 à 10):"))
ana1 = int(input("Ana informe o primeiro valor (1 à 10):"))
augusto2 = int(input("Augusto informe o segundo valor (1 à 10):"))
ana2 = int(input("Ana informe o segundo valor (1 à 10):"))
augusto3 = int(input("Augusto informe o terceiro valor (1 à 10):"))
ana3 = int(input("Ana informe o terceiro valor (1 à 10):"))
augustoTotal = augusto1 + augusto2 + augusto3
print("Os números escolhidos por Augusto foram:",augusto1,augusto2,augusto3)
print("Os números escolhidos por Ana foram:",ana1,ana2,ana3)
if augustoTotal % 2 == 0:
    print("Augusto venceu!")
else:
    print("Ana venceu!")

