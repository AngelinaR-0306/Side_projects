import turtle 
t = turtle.Turtle()
turtle.title("FOR YOU")
screen = turtle.Screen()
screen.bgcolor("black")

t.color("blue")
t.fillcolor("blue")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill()

t.up()
t.setpos(-65, 150)
t.down()
t.color("black")
t.write("Your poes<3", font= ("Boulder", 20, "bold"))

t.ht()

turtle.mainloop()
