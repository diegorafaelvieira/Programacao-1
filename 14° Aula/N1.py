a = 80000
# cresce 3% ao ano
b = 200000
# cresce 1.5% ao ano

ano = 0

while b > a or b == a:
    a+= (a/100) * 3
    b+= (b/100) * 1.5
    ano+=1
    print("Crescimento de A:",a)
    print("Crescimento de B:",b)
    print("Anos:",ano)
    print("")


''' Código Professor
A = 80000
B = 200000
tA = 0.03

anos = 0

while A<B:
    A = A + (A*tA)
    B = B + (B*tB)
    anos = anos + 1
    print("A:",A)
    print("B:",B)
    print("Anos:", anos)
'''    
