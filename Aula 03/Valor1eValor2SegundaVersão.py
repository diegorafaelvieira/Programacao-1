chuva = input("Chove?(s)im ou (n)ão?")
frio = input("Está frio?(s)im ou (n)ão?")
if chuva == "s" and frio == "s":
    print ( "Vista todos os casacos que puder! E não esqueça do guarda-chuva!")
elif chuva == "s" and frio == "n":
    print ("Vista qualquer coisa, mas leve o guarda-chuva")
elif chuva == "n" and frio =="s":
    print ("Não esqueça de usar um casaco!")
elif chuva == "n" and frio == "n":
    print ("Vista o que quiser, o dia está lindo!")


