v1 = float(input("Informe o primeiro valor:"))
v2 = float(input("Informe o segundo valor:"))
v3 = float(input("Informe o terceiro valor:"))
if (v1 > v2) and (v1 > v3) and (v2 > v3):
    print (" A ordem crescente é:",v3,v2,v1)
elif (v1 > v2) and (v1 > v3) and (v2 < v3):
    print ("A ordem crescente é:",v2,v3,v1)
elif (v2 > v1) and (v2 > v3) and (v1 > v3):
    print ("A ordem crescente é:",v3,v1,v2)
elif (v2 > v1) and (v2 > v3) and (v1 < v3):
    print ("A ordem crescente é:",v1,v3,v2)
elif (v3 > v1) and (v3 > v2) and (v1 > v2):
    print ("A ordem crescente é:",v2,v1,v3)
elif (v3 > v1) and (v3 > v2) and (v1 < v2):
    print ("A ordem crescente é:",v1,v2,v3)
elif v1 == v2 == v3:
    print ("Números iguais!")
    
