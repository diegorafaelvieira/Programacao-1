v1 = int(input("Informe o primeiro valor:"))
v2 = int(input("Informe o segundo valor:"))
v3 = int(input("Informe o terceiro valor:"))
if (v1 > v2) and (v1 > v3) and (v2 > v3):
    print (" A ordem decrescente é:",v1,v2,v3)
elif (v1 > v2) and (v1 > v3) and (v2 < v3):
    print ("A ordem decrescente é:",v1,v3,v2)
elif (v2 > v1) and (v2 > v3) and (v1 > v3):
    print ("A ordem decrescente é:",v2,v1,v3)
elif (v2 > v1) and (v2 > v3) and (v1 < v3):
    print ("A ordem decrescente é:",v2,v3,v1)
elif (v3 > v1) and (v3 > v2) and (v1 > v2):
    print ("A ordem decrescente é:",v3,v1,v2)
elif (v3 > v1) and (v3 > v2) and (v1 < v2):
    print ("A ordem decrescente é:",v3,v2,v1)
elif v1 == v2 == v3:
    print ("Números iguais!")
