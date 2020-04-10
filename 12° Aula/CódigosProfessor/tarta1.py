def quadrado(t,c):
    #Define a cor de preenchimento
    t.color(c)
    #Inicia preenchimento
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    #Finaliza preenchimento
    t.end_fill()



    
#Importa a biblioteca Turtle
import turtle
#Inicializa a tartaruga
tarta = turtle.Pen()
for i in range(0,100):
    tarta.right(35)
    quadrado(tarta,'red')
    tarta.right(35)
    tarta.forward(10)
    quadrado(tarta,'blue')


















