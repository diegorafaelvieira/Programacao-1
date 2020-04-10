def tipoTriangulo(ld1,ld2,ld3):
    if ld1==ld2 and ld1==ld3:
        print("O triângulo é equilátero")
    elif ld1==ld2 or ld2==ld3 or ld1== ld3:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")


l1 = float(input("Informe o valor do 1° lado:"))
l2 = float(input("Informe o valor do 2° lado:"))
l3 = float(input("Informe o valor do 3° lado:"))

tipoTriangulo(l1,l2,l3)
