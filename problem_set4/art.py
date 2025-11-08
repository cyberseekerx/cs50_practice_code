import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
colors = ['red','dark red']
t.penup()
t.goto(0, 0)
t.pendown()
for number in range(900):
    t.forward(number +1)
    t.right(89)
    t.pencolor(colors[number % len(colors)])
turtle.ontimer(turtle.bye,10000)
turtle.done()
