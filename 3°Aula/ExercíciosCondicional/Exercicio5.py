portugues = float(input("Informe a nota em português:"))
matematica = float(input("Informe a nota em matemática:"))
conhecimentosGerais = float(input("Informe a nota^em conhecimentos gerais:"))
media = (portugues+matematica+conhecimentosGerais) / 3
print ("A nota em português foi:",portugues)
print ("A nota em matemática foi:",matematica)
print ("A nota em conhecimentos gerais foi:",conhecimentosGerais)
print ("A média do candidato foi:",media)
if  (media > 7) and(portugues > 5) and (matematica > 5) and (conhecimentosGerais > 5):
    print ("Aprovado!")
elif (media <= 7):
    print ("Reprovado!")

