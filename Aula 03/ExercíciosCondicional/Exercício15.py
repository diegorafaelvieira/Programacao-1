nome1 = input("Informe o nome da primeira pessoa:")
altura1 = float(input("Informe a altura da primeira pessoa:"))
peso1 = float(input("Informe o peso da primeira pessoa:"))
nome2 = input("Informe o nome da segunda pessoa:")
altura2 = float(input("Informe a altura da segunda pessoa:"))
peso2 = float(input("Informe o peso da segunda pessoa:"))
if (peso1 > peso2):
    print("O nome da pessoa mais pesada é:",nome1)
elif (peso1 < peso2):
    print("O nome da pessoa mais pesada é:",nome2)
if (altura1 > altura2):
    print("O nome da pessoa mais alta é:",nome1)
elif (altura1 < altura2):
    print("O nome da pessoa mais alta é:",nome2)    
    
