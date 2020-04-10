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
operacao = input("Informe (+)para soma, (/) para divisão,(*) para multiplicação e (-) para subtração:")
    
if operacao=="+":
    soma(v1,v2)
elif operacao=="/":
    divisao(v1,v2)
elif operacao=="*":
    multiplicacao(v1,v2)
elif operacao=="-":
    subtracao(v1,v2)
