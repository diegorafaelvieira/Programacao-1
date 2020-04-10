c1 = float(input("Informe o valor do corretor 1:"))
nomec1 = input("Informe o nome do corretot 1:")
c2 = float(input("Informe o valor do corretor 2:"))
nomec2 = input("Informe o nome do corretot 2:")
c3 = float(input("Informe o valor do corretor 3:"))
nomec3 = input("Informe o nome do corretot 3:")
totalVendas = c1 + c2 + c3
print ("O valor total das vendas é de:",totalVendas)
if c1 > 50000: 
    print("O corretor",nomec1,"vendeu no valor de:",c1,"e recebeu comissão de:",((12/100)*c1))
elif c1 >= 30000 and  c1 <= 50000:
    print("O corretor",nomec1,"vendeu no valor de:",c1,"e recebeu comissão de:",((9.5/100)*c1))
elif c1 < 30000:
    print("O corretor",nomec1,"vendeu no valor de:",c1,"e recebeu comissão de:",((7/100)*c1))
if c2 > 50000: 
    print("O corretor",nomec2,"vendeu no valor de:",c2,"e recebeu comissão de:",((12/100)*c2))
elif c2 >= 30000 and c2 <= 50000:
    print("O corretor",nomec2,"vendeu no valor de:",c2,"e recebeu comissão de:",((9.5/100)*c2))
elif c2 < 30000:
    print("O corretor",nomec2,"vendeu no valor de:",c2,"e recebeu comissão de:",((7/100)*c2))    
if c3 > 50000: 
    print("O corretor",nomec3,"vendeu no valor de:",c3,"e recebeu comissão de:",((12/100)/c3))
elif c3 >= 30000 and c3 <= 50000:
    print("O corretor",nomec3,"vendeu no valor de:",c3,"e recebeu comissão de:",((9.5/100)*c3))
elif c3 < 30000:
    print("O corretor",nomec3,"vendeu no valor de:",c3,"e recebeu comissão de:",((7/100)*c3))    

