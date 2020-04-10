chuva = (input("Chove?(s)im ou (n)ão?"))
frio = (input("Está frio?(s)im ou (n)ão?"))
if chuva == "s":
    if frio == "s":
        print ( "Vista todos os casacos que puder! E não esqueça do guarda-chuva!")
    else: 
        print ("Vista qualquer coisa, mas leve o guarda-chuva")
else:
    if frio == "s":
        print ("Não esqueça de usar um casaco!")
    else:
        print ("Vista o que quiser, o dia está lindo!")

    
    
