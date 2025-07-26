import turtle
turtle.Screen().bgcolor('pink')
turtle.Screen().setup(600,500)
turtle.Screen().title('Star')

p = turtle.Turtle()
p.color('white')
p.pensize(5)
p.shape('circle')

p.penup()
p.goto(-80,70)
p.pendown()
n= 5

for i in range(n):
    p.forward(200)
    p.right(144)
    
turtle.done()