n1 = float(input("Informe a primeira nota:"))
n2 = float(input("Informe a segunda nota:"))
n3 = float(input("Informe a terceira nota:"))
media = (n1*2+n2*3+n3*5)/(2+3+5)
if media >= 7: 
    print ("Aprovado!")
else:
    print("Reprovado!")
