import turtle
screen = turtle.Screen()
screen.bgcolor('black')
screen.screensize(300, 300)
t = turtle.Turtle()

t.speed('fast')
t.color('white')        #sets color
t.width(3)              #sets width

#travel to -100,0
t.up()
t.goto(-100, 0)
t.down()

#draws filled circle
t.begin_fill()
t.circle(50)
t.end_fill()

#travels to center of drawn circle
t.up()
t.goto(-100,50)
t.down()

#draws pupil
t.begin_fill()
t.color('black')
t.circle(5)
t.end_fill()
t.color('white')


t.up()
t.goto(100,0)
t.down()
print(t.pos())

t.begin_fill()
t.circle(50)
t.end_fill()

t.goto(100,50)
t.color('black')
t.begin_fill()
t.circle(5)
t.end_fill()
t.color('white')

#draws smiley
t.up()
t.goto(-151, -100)
t.down()
t.setheading(270)
t.circle(150,180)


t.shape('turtle')
t.up()
t.goto(0,-300)
t.setheading(0)
t.speed(1)
while True:
    t.circle(300)

turtle.done()