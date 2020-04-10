usuario = int(input("Informe um número entre 1 e 60:"))
from random import randint
numero = randint (1,60)
if usuario == numero:
    print ("Parabéns você acertou o número sorteado!",numero)
else:
    print ("Você errou!",numero)
   
