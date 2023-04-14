import turtle

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

def Trianangle(size, autopen:bool, pensize, color, fill:bool):
    print("Sorry this feature is currently unavaible")

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
