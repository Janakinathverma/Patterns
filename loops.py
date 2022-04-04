import turtle
loadWindow=turtle.Screen()
turtle.speed(4)
loadWindow.bgcolor('black')
turtle.color('yellow')
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()