import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.width(2)
t.speed(0)
col=['white','red','orange','yellow','green','blue','cyan']

for i in range(300):
    t.color(col[i%7])
    t.forward(i*4)
    t.right(91)
    for b in range(3):
        t.forward(i*4)
        t.right(91)
        for c in range(2):
            t.forward(i*4)
            t.right(91)
