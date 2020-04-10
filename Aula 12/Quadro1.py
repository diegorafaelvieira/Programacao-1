def quadrado(tarta,c):
    #Define a cor de preenchimento
    tarta.color(c)
    #Inicia preenchimento
    tarta.begin_fill()
    #Comandos
    tarta.forward(100)
    tarta.left(90)
    tarta.forward(100)
    tarta.left(90)
    tarta.forward(100)
    tarta.left(90)
    tarta.forward(100)
    tarta.left(90)
    #Finaliza preenchimento
    tarta.end_fill()


#Importa a biblioteca Turtle
import turtle
#Inicializa a tartaruga
tarta = turtle.Pen()
for i in range(0,100):  # Repete 100 vezes o quadrado
    tarta.right(35)
    quadrado(tarta,'blue')
    tarta.right(35)
    tarta.forward(10)
    quadrado(tarta,'red')




