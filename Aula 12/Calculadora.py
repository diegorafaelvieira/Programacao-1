def soma(a,b):
    print(a+b)
    
def subtracao(a,b):
    print(a-b)
    
def multiplicacao(a,b):
    print(a*b)
    
def divisao(a,b):
    print(a/b)    

    

v1 = int(input("Valor 1:"))
v2 = int(input("Valor 2:"))
operacao = input("Informe soma, div, mult, sub:")
    
if operacao=="soma":
    soma(v1,v2)
elif operacao=="div":
    divisao(v1,v2)
elif operacao=="mult":
    multiplicacao(v1,v2)
elif operacao=="sub":
    subtracao==(v1,v2) 


