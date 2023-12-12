import turtle
from turtle import *

"""
Módulo que inicia turtle y asigna parámetros para 
hacer una estrella
"""
#Cursor con forma de tortuga
turtle.shape("turtle")


def dibujar_estrella(puntas, tamaño, col, x, y):
    penup()
    goto(x, y)
    pendown()
    angulo = 180 - (180/puntas)
    color(col)
    begin_fill()
    
    for i in range(puntas):
        forward(tamaño)
        right(angulo)


    end_fill()
    exitonclick()

