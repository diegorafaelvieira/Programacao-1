#nome = input("Informe o nome:") #Usuário digita SOBRENOME,NOME
#print(nome[0]) #imprime a 1ª letra do nome
#print(nome[-1]) #imprime a última letra do nome
#print(nome[1:-1]) #imprime o nome menos a 1ª e última letra do nome

#nomes = nome.split(",") #utilizamos a vírgula como separador do sobrenome,nome

#print(nomes[1],nomes[0]) #imprime primeiro o nome e depois o sobrenome

arquivo = input("Informe o nome do arquivo:") #Visualizar 2 variaveis diferentes
x = arquivo.split(":")                                      #DocumentoZ:2017.txt

print(x[0])

y = arquivo.split(".")
print(y[1])


#y = x[1].split(".")    outra maneira de visualizar 2 variaveis
#print(y[-1])
