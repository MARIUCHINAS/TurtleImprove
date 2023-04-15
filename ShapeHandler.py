import turtle
import math


def Bike(size: int, autopen: bool, pensize: int, color: str, fill: bool) -> None:
    current_pos = turtle.position()
    turtle.color(color)
    if autopen:
        turtle.penup()
    turtle.setposition(-size / 2, -size / 2)
    if autopen:
        turtle.pendown()
    
    # Draw the left tyre
    if fill:
        turtle.begin_fill()
    turtle.pensize(pensize)
    turtle.circle(size / 4)
    if fill:
        turtle.end_fill()
    
    # Draw the right tyre
    if fill:
        turtle.begin_fill()
    turtle.penup()
    turtle.setposition(size / 2, -size / 2)
    turtle.pendown()
    turtle.circle(size / 4)
    if fill:
        turtle.end_fill()
    
    # Draw the handle
    turtle.penup()
    turtle.setposition(0, size / 4)
    turtle.pendown()
    turtle.setposition(0, size / 2)
    
    # Draw the straight part of the handle
    turtle.setheading(270)
    turtle.setposition(0, size * 0.6)
    
    # Draw the circular part of the handle
    turtle.circle(size / 8, 180)
    
    # Draw the seat tube
    turtle.penup()
    turtle.setposition(0, size / 4)
    turtle.pendown()
    turtle.setposition(0, -size / 4)
    
    # Draw the saddle
    turtle.setheading(180)
    turtle.setposition(-size / 4, 0)
    
    # Draw the top tube
    turtle.penup()
    turtle.setposition(size / 4, size / 4)
    turtle.pendown()
    turtle.setposition(-size / 4, size / 4)
    
    # Draw the down tube
    turtle.penup()
    turtle.setposition(size / 4, size / 4)
    turtle.pendown()
    turtle.setposition(size / 4, -size / 4)
    
    # Draw the seat stay
    turtle.penup()
    turtle.setposition(-size / 4, 0)
    turtle.pendown()
    turtle.setposition(size / 4, size / 4)
    
    # Draw the chain stay
    turtle.penup()
    turtle.setposition(size / 4, -size / 4)
    turtle.pendown()
    turtle.setposition(-size / 4, -size / 4)
    
    turtle.setposition(current_pos)

def Circle(size, autopen:bool, pensize, color, fill:bool):
    turtle.pensize(pensize)
    turtle.color(color)
    if fill:
        turtle.begin_fill()

    if autopen:
        turtle.pendown()
    turtle.circle(size)
    if autopen:
        turtle.penup()
    if fill:
        turtle.end_fill()

def Triangle(size: int, autopen: bool, pensize: int, color: str, fill: bool) -> None:
    current_pos = turtle.position()
    turtle.color(color)
    if autopen:
        turtle.penup()
    turtle.setposition(-size / 2, -size / (2 * math.sqrt(3)))
    if autopen:
        turtle.pendown()
    if fill:
        turtle.begin_fill()
    
    turtle.pensize(pensize)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    
    if fill:
        turtle.end_fill()
    
    turtle.setposition(current_pos)

def Square(size: int, autopen: bool, pensize: int, color: str, fill: bool) -> None:
    current_pos = turtle.position()
    turtle.color(color)
    if autopen:
        turtle.penup()
    turtle.setposition(-size / 2, -size / 2)
    if autopen:
        turtle.pendown()
    if fill:
        turtle.begin_fill()
    
    turtle.pensize(pensize)
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    
    if fill:
        turtle.end_fill()
    
    turtle.setposition(current_pos)
