l1 = float(input("Informe o valor do 1° lado:"))
l2 = float(input("Informe o valor do 2° lado:"))
l3 = float(input("Informe o valor do 3° lado:"))
if l1==l2 and l1==l3:
    print("O triângulo é equilátero")
elif l1!=l2 and l2!=l3:
    print("O triângulo é escaleno")
else:
    print("o triângulo é isósceles")
