
linhas = ['TIME_A#3#2#5','TIME_B#2#5#3','TIME_C#1#6#3','TIME_D#3#3#4','TIME_E#5#5#0','TIME_F#0#5#5','TIME_G#2#5#3','TIME_H#0#0#10']

nomes = []
pontos = []

for pos in range(0,len(linhas)):
    quebra = linhas[pos].split("#")
    nomes.append(quebra[0])
    pontuacao = (int(quebra[1])*3)+int(quebra[3])
    pontos.append(pontuacao)

maximo = pontos[0]
pMax = 0
minimo = pontos[0]
pMin = 0

for pos in range(0,len(nomes)):
    if pontos[pos]>maximo:
        maximo = pontos[pos]
        pMax = pos

    if pontos[pos]<minimo:
        minimo = pontos[pos]
        pMin = pos

print(nomes[pMax],' - ',pontos[pMax])
print(nomes[pMin],' - ',pontos[pMin])
    
#Avaliação 1 questão com Funções - 5 questões no máximo
#Colinha 10cm X 10 cm / frente e verso / Exercicios / Estruturas / For/ Preencher lista/ imprimir lista
