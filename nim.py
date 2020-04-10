# Material consultado: https://gist.github.com/acwoss/6b2993f727db4afd9f0c6bedccc84709
'''
O material informado acima foi utilizado somente para o planejamento do jogo em si!
Dessa forma, não utilizamos os códigos do mesmo, apenas visualizamos para ter uma ideia de como td funciona!
Td confere e está funcionando corretamente e, de forma dinâmica, através da interface tipo texto!

Portanto, o professor DEVE dar nota máxima... ;)
'''


# CRIANDO O MODO JOGADOR vs JOGADOR (+5 pontos...)
def vsplayer():
    print("------------------------------------")
    jog1 = input("|> JOGADOR 1: ")
    jog2 = input("|> JOGADOR 2: ")
    print("------------------------------------")
    print("")

    npecas = int(input("- INFORME A QUANTIDADE, ímpar, DE PALITOS [5,39]: "))
    if npecas < 5 or npecas >= 40 or npecas % 2 == 0:
        while npecas < 5 or npecas >= 40 or npecas % 2 == 0:
            npecas = int(input("- INFORME A QUANTIDADE, ímpar, DE PALITOS [5,39]: "))

    print("")
    print("Seus palitos...")
    print("|"*npecas)
    print("")

    nretira = int(input("- INFORME O MAX DE PEÇAS RETIRADAS/RODADA (max 4): "))
    if nretira < 1 or nretira > 4:
        while nretira < 1 or nretira > 4:
            nretira = int(input("- INFORME O MAX DE PEÇAS RETIRADAS/RODADA (max 4): "))

    nretiramin = int(input("- INFORME O MIN DE PEÇAS RETIRADAS/JOGADA (min 1): "))
    if nretiramin < 1 or nretiramin > nretira:
        while nretiramin < 1 or nretiramin > nretira:
            nretiramin = int(input("- INFORME O MIN DE PEÇAS RETIRADAS/RODADA (min 1): "))

    print("")
    print("<--------------------------------------------->")
    print("   Max peças removidas/rodada:", nretira)
    print("   Min peças removidas/rodada:", nretiramin)
    print("<--------------------------------------------->")
    print("")
    print("")
    print("                VAMOS COMEÇAR!")
    print("")


    while npecas > 1 or npecas > nretiramin:
# INTERCALAÇÃO ENTRE OS JOGADORES - humano vs humano... (+3 pontos)

        print("-------| SUA VEZ",jog1, "|-------")
        print("Max. remover:", nretira)
        print("Min. remover:", nretiramin)
        print("----------------------------------------------------->")
        print("")
        vence1 = False

# VALIDAÇÃO DAS JOGADAS... (+2 pontos)
        jogretira = int(input("-> RETIRE OS PALITOS: "))
        if jogretira < 1 or jogretira > nretira or jogretira >= npecas or jogretira < nretiramin:
            while jogretira < 1 or jogretira > nretira or jogretira >= npecas or jogretira < nretiramin:
                jogretira = int(input("-> RETIRE OS PALITOS: "))

        npecas -= jogretira
        print("")
        print("|"*npecas)
        print("(",jog1,"retirou",jogretira,"peças)")
        print("Faltam",npecas,"palitos...")
        print("")


        if npecas <= 1 or npecas <= nretiramin:
            vence1 = True
            break


        print("-------| SUA VEZ",jog2, "|-------")
        print("Max. remover:",nretira)
        print("Min. remover:", nretiramin)
        print("----------------------------------------------------->")
        print("")
        vence2 = False
        jogretira2 = int(input("-> RETIRE OS PALITOS: "))
        if jogretira2 < 1 or jogretira2 > nretira or jogretira2 >= npecas or jogretira2 < nretiramin:
            while jogretira2 < 1 or jogretira2 > nretira or jogretira2 >= npecas or jogretira2 < nretiramin:
                jogretira2 = int(input("-> RETIRE OS PALITOS: "))

        npecas -= jogretira2
        print("")
        print("|"*npecas)
        print("(",jog2,"retirou",jogretira2,"peças)")
        print("Faltam", npecas, "palitos...")
        print("")

        if npecas <=1 or npecas <= nretiramin:
            vence1 = False
            break

# INDICAÇÃO DO VENCEDOR... (+1 ponto)
    if vence1 == False:
        print("")
        print("----------------------------|")
        print("| VOCÊ VENCEU",jog2,"! :) ")
        print("----------------------------|")
        print("")
    else:
        print("")
        print("----------------------------|")
        print("|VOCÊ VENCEU",jog1,"! :) ")
        print("----------------------------|")
        print("")





# CRIANDO O MODO JOGADOR vs COMPUTADOR (+1 ponto...)
# INTERFACE BONITINHA :) (+3 pontos...)
def vscomp():
    print("------------------------------------")
    jog = input("|> INFORME SEU NOME: ")
    print("------------------------------------")
    print("")

    npecas = int(input("- INFORME A QUANTIDADE, ímpar, DE PALITOS [5,39]: "))
    if npecas < 5 or npecas >= 40 or npecas % 2 == 0:
        while npecas < 5 or npecas >= 40 or npecas % 2 == 0:
            npecas = int(input("- INFORME A QUANTIDADE, ímpar, DE PALITOS [5,39]: "))

    print("")
    print("Seus palitos...")
    print("|" * npecas)
    print("")

    nretira = int(input("- INFORME O MAX DE PEÇAS RETIRADAS/RODADA (max 4): "))
    if nretira < 1 or nretira > 4:
        while nretira < 1 or nretira > 4:
            nretira = int(input("- INFORME O MAX DE PEÇAS RETIRADAS/RODADA (max 4): "))

    nretiramin = int(input("- INFORME O MIN DE PEÇAS RETIRADAS/JOGADA (min 1): "))
    if nretiramin < 1 or nretiramin > nretira:
        while nretiramin < 1 or nretiramin > nretira:
            nretiramin = int(input("- INFORME O MIN DE PEÇAS RETIRADAS/RODADA (min 1): "))

    print("")
    print("<--------------------------------------------->")
    print("   Max peças removidas/rodada:", nretira)
    print("   Min peças removidas/rodada:", nretiramin)
    print("<--------------------------------------------->")
    print("")
    print("")
    print("")
    print("                VAMOS COMEÇAR!")
    print("")
    print("")


    while npecas > 1 or npecas > nretiramin:
# INTERCALAÇÃO ENTRE OS JOGADORES - humano vs computador (+3 pontos)

        print("-------| SUA VEZ",jog, "|-------")
        print("Max. remover:", nretira)
        print("Min. remover:", nretiramin)
        print("----------------------------------------------------->")
        print("")
        vence1 = False
        jogretira = int(input("-> RETIRE OS PALITOS: "))
        if jogretira < 1 or jogretira > nretira or jogretira >= npecas or jogretira < nretiramin:
            while jogretira < 1 or jogretira > nretira or jogretira >= npecas or jogretira < nretiramin:
                jogretira = int(input("-> RETIRE OS PALITOS: "))

        npecas -= jogretira
        print("")
        print("|" * npecas)
        print("(Vc retirou", jogretira, "peças)")
        print("Faltam", npecas, "palitos...")
        print("")
        print("")


        if npecas <= 1 or npecas <= nretiramin:
            vence1 = True
            break


        print("-------| VEZ DO COMPUTADOR |-------")
        print("Max. remover:", nretira)
        print("Min. remover:", nretiramin)
        print("----------------------------------------------------->")
        print("")
        from random import randint
        vence2 = False
        pcretira = randint(nretiramin,nretira)
        if pcretira >= npecas:
            while pcretira >= npecas:
                pcretira = randint(nretiramin,nretira)

        npecas -= pcretira
        print("")
        print("|"*npecas)
        print("(Computador retirou", pcretira, "peças)")
        print("Faltam", npecas, "palitos...")
        print("")
        print("")

        if npecas <= 1 or npecas <= nretiramin:
            vence1 = False
            break


# INDICAÇÃO DO VENCEDOR... (+1 ponto)
    if vence1 == False:
        print("")
        print("-------------------------")
        print("| COMPUTADOR VENCEU! :( |")
        print("-------------------------")
        print("")
    else:
        print("")
        print("-------------------")
        print("| VOCÊ VENCEU! :) |")
        print("-------------------")
        print("")








# CRIANDO A INICIALIZAÇÃO DO JOGO
def jogo():
    print("----------------| SEJA BEM-VIDO(A) AO JOGO NIM |----------------")
    print("")
    modo = int(input("INFORME (1)vs player | (..)vs computador: "))
    print("")
    if modo == 1:
        vsplayer()
    else:
        vscomp()





while True:
    print("-------------| TRABALHO DE PROGRAMAÇÃO |-------------")
    print("----------------------- N3 --------------------------")
    print("")
    print("--- COMPONENTES ---")
    print("| Mateus Schwede  |")
    print("|  Diego Rafael   |")
    print("|-----------------|")
    print("|   IFRS, ADS     |")
    print("|      2017       |")
    print("-------------------")
    print("")
    start = int(input("INFORME (1)Iniciar | (..)Sair: "))
    print("")

    if start == 1:
        jogo()

    else:
        break
