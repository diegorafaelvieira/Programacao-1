altura = float(input("Informe uma altura:"))
sexo = input("Informe o sexo (m)asculino ou (f)eminino:")
pesoMasculino = (72.7*altura)-58
pesoFeminino = (62.1*altura)-44.7
if sexo == "m":
    print ("O peso ideal é:",pesoMasculino)
elif sexo == "f":
    print("O peso ideal é:",pesoFeminino)

