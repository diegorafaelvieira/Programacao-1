texto = ("Deixe-me começar dizendo o que pensamento computacional não é. Não se trata, por exemplo, de saber navegar na internet, enviar email, publicar um blog, ou operar um processador de texto.Pensamento computacional é saber usar o computador como um instrumento de aumento do poder cognitivo e operacional humano – em outras palavras, usar computadores, e redes decomputadores, para aumentar nossa produtividade, inventividade, e criatividade. Grandes intelectuais da educação, como Seymour Papert e Andrea diSessa, já publicaram vários livros sobreo assunto. Estamos em uma época de transição no mundo científico, em que o pensamento computacional está transformando profundamente a academia e a indústria. Hoje em dia, um cientista em um laboratório de pesquisa de ponta em nada lembra o estereótipo do cientista do século XIX, com seu avental branco, trancado em um laboratório com tubos de ensaio. Em vez disso, ele provavelmente passa a maior parte do tempo em frente a um computador, construindo e estudando modelos computacionais. Um engenheiro industrial, ao tentar redesenhar a linha deprodução, não usa só papel e lápis – usa modelos computacionais. Um economista tentando fazer uma projeção de inflação não faz as contas de cabeça – usa, claro, modelos. A primeira etapa dopensar computacionalmente é identificar as tarefas cognitivas que podem ser feitas de forma mais rápida e eficiente por um computador. A segunda etapa é saber programar um computador para realizar essas tarefas cognitivas – em outras palavras, transferir aquilo que não é essencialmente humano para um computador que, como sabemos, é bem burrinho, mas muito rápido.")
palavras = texto.split(" ")
#print(palavras)
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0
contComputador = 0
contVogal = 0
contMaiorPalavra = 0

#1. Desenvolva uma função que imprima quantas palavras iniciam com cada uma das
#vogais (a, e i, o, u).
for p in palavras:
    if p[0] == "A" or p[0] == "a":
        contA+=1
    elif p[0] == "E" or p[0] == "e":
        contE+=1    
    elif p[0] == "I" or p[0] == "i":
        contI+=1
    elif p[0] == "O" or p[0] == "o":
        contO+=1
    elif p[0] == "U" or p[0] == "u":
        contU+=1      
    
print("Com A:",contA)
print("Com E:",contE)
print("Com I:",contI)
print("Com O:",contO)
print("Com U:",contU)

#2. Desenvolva uma função que informe quantas vezes a palavra computador aparece no
#texto.
for p in palavras: #Pensar numa nova busca
    x = p.split(",")
    if x[0] == "computador" or x[0] == "Computador":
        contComputador += 1

print("Computador:",contComputador)

#3. Desenvolva uma função que informe quais palavras iniciam e terminam com vogais.
for p in palavras: 
    if p[0] in "aeiouAEIOU" and p[-1] in "aeiou":
        contVogal += 1
        print("Vogal:",contVogal,"->",p)


#4. Desenvolva uma função que informe qual é a maior palavra do texto.
maior = palavras[0]
for p in palavras:
    if len(p)>len(maior):
        maior = p
print(maior)        
    

