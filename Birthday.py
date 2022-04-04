import turtle
happy=turtle.Screen()
happy.setup(700,700)
happy.bgcolor("black")
turtle=turtle.Turtle()
turtle.shape("turtle")
turtle.width(5)
turtle.speed(150)
  
def mov(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.lt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.pendown()

#letters
def A():
  turtle.rt(16)
  turtle.forward(60)
  turtle.rt(150)
  turtle.fd(60)
  turtle.backward(30)
  turtle.rt(105)
  turtle.fd(15)   
  
  
def B():
   turtle.forward(70)
   turtle.rt(90)
   for i in range(18):
      turtle.rt(9)
      turtle.fd(3)
   for i in range(18):
      turtle.rt(13)
      turtle.backward(4) 


def D():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(9)
   for i in range(13):
      turtle.rt(14)
      turtle.fd(7.3)  

       
       
def Y():
   turtle.fd(40)
   turtle.left(47)
   turtle.fd(30)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   


def H():
   turtle.fd(60)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   turtle.lt(90)
   turtle.fd(30)
   turtle.backward(60)
   
   
def P():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(8):
       turtle.rt(20)
       turtle.fd(5)
       
def u():
  turtle.rt(180)
  turtle.fd(55)
  turtle.lt(45)
  turtle.fd(7)
  turtle.lt(45)
  turtle.fd(20)
  turtle.lt(45)
  turtle.fd(7)
  turtle.lt(45)
  turtle.fd(55)


def j():
  turtle.rt(90)
  turtle.fd(10)
  turtle.backward(30)
  turtle.fd(20)
  turtle.rt(90)
  turtle.fd(55)
  turtle.rt(45)
  turtle.fd(7)
  turtle.rt(45)
  turtle.fd(10)
  turtle.rt(45)
  turtle.fd(7)
  turtle.rt(45)
  turtle.fd(15)
#ff9900 b3b3b3 ff6699

# happy
turtle.speed(6)
turtle.width(9)
turtle.color("#b3b3b3")
mov(180,120)
turtle.width(9)
H()
turtle.speed(8)
turtle.width(5)
mov(140,120)
A()
mov(100,120)
P()
mov(70,120)
P()
mov(20,120)
Y()
# b'day'
turtle.speed(6)
turtle.width(9)
turtle.color("#ff9900")
mov(-20,120)
B()
mov(-60,170)
turtle.fd(10)
turtle.speed(8)
turtle.width(5)
mov(-80,120)
D()
mov(-120,120)
A()
mov(-180,120)
Y()
turtle.speed(150)
turtle.width(5)
#cake base
turtle.color("#f2f2f2")
mov(138.84,-250)
turtle.begin_fill()
turtle.lt(10)
turtle.fd(121.85)
turtle.rt(10)
turtle.rt(150)
for i in range(30):
  turtle.lt(4)
  turtle.fd(12.8)
turtle.rt(150)
turtle.rt(10)
turtle.fd(121.85)
turtle.lt(10)
turtle.rt(41)
for i in range(30):
  turtle.rt(3)
  turtle.fd(10.1)
turtle.end_fill()
turtle.color("#3377ff")
turtle.width(11)
mov(138.84,-250)
turtle.lt(10)
turtle.fd(121.85)
turtle.rt(10)
turtle.rt(150)
for i in range(30):
  turtle.lt(4)
  turtle.fd(12.8)
turtle.rt(150)
turtle.rt(10)
turtle.fd(121.85)
turtle.lt(10)
turtle.rt(41)
for i in range(30):
  turtle.rt(3)
  turtle.fd(10.1)
# cake top
mov(155,-150)
turtle.width(5)
turtle.color("#3377ff")
turtle.begin_fill()
turtle.rt(150)
for i in range(30):
  turtle.lt(4)
  turtle.fd(12.33)
for i in range(15):
  turtle.lt(4)
  turtle.fd(6)
for i in range(30):
  turtle.lt(4)
  turtle.fd(12.33)
for i in range(15):
  turtle.lt(4)
  turtle.fd(6)
turtle.end_fill()
#inner face
turtle.width(5)
mov(100,-135)
turtle.color("#f2f2f2")
turtle.begin_fill()
turtle.rt(150)
for i in range(30):
  turtle.lt(4)
  turtle.fd(8)
for i in range(15):
  turtle.lt(4)
  turtle.fd(4)
for i in range(30):
  turtle.lt(4)
  turtle.fd(8)
for i in range(15):
  turtle.lt(4)
  turtle.fd(4)
turtle.end_fill()
mov(100,-135)
turtle.color("black")
turtle.rt(150)
for i in range(30):
  turtle.lt(4)
  turtle.fd(8)
for i in range(15):
  turtle.lt(4)
  turtle.fd(4)
for i in range(30):
  turtle.lt(4)
  turtle.fd(8)
for i in range(15):
  turtle.lt(4)
  turtle.fd(4)
#mouth
turtle.speed(150)
turtle.width(5)
mov(75,-130)
turtle.color("#ff3333")
turtle.begin_fill()
turtle.rt(150)
for i in range(60):
  turtle.lt(2)
  turtle.fd(3)
turtle.lt(120)
turtle.fd(150)
turtle.end_fill()
mov(75,-130)
turtle.color("black")
turtle.rt(150)
for i in range(60):
  turtle.lt(2)
  turtle.fd(3)
turtle.lt(120)
turtle.fd(150)
mov(50,-155)
turtle.rt(60)
for i in range(10):
  turtle.fd(4)
  turtle.rt(6)
turtle.lt(60)
for i in range(12):
  turtle.fd(4)
  turtle.rt(8)
#nose
mov(0,-128)
turtle.color("#ff3333")
turtle.begin_fill()
turtle.fd(32)
turtle.lt(90)
for i in range(60):
  turtle.rt(6)
  turtle.fd(2)
turtle.end_fill()
mov(0,-128)
turtle.color("black")
turtle.fd(32)
turtle.lt(90)
for i in range(60):
  turtle.rt(6)
  turtle.fd(2)
#left eye
mov(35,-45)
turtle.color("#f2f2f2")
turtle.begin_fill()
turtle.lt(90)
for i in range(60):
  turtle.rt(6)
  turtle.fd(2.5)
turtle.end_fill()
mov(35,-45)
turtle.color("black")
turtle.lt(90)
for i in range(60):
  turtle.rt(6)
  turtle.fd(2.5)
turtle.width(20)
mov(35,-20)
turtle.fd(1)
#right eye
turtle.width(5)
mov(-35,-45)
turtle.color("#f2f2f2")
turtle.begin_fill()
turtle.lt(90)
for i in range(60):
  turtle.rt(6)
  turtle.fd(2.5)
turtle.end_fill()
mov(-35,-45)
turtle.color("black")
turtle.lt(90)
for i in range(60):
  turtle.rt(6)
  turtle.fd(2.5)
turtle.width(20)
mov(-35,-20)
turtle.fd(1)
#moustache
turtle.width(2)
mov(15,-120)
turtle.lt(110)
turtle.fd(40)
mov(-15,-120)
turtle.rt(110)
turtle.fd(40)
mov(15,-110)
turtle.lt(90)
turtle.fd(40)
mov(-15,-110)
turtle.rt(90)
turtle.fd(40)
mov(15,-100)
turtle.lt(70)
turtle.fd(40)
mov(-15,-100)
turtle.rt(70)
turtle.fd(40)
turtle.width(11)
turtle.color("#3377ff")
cory=-250
for a1 in range(3):
  mov(135,cory)
  cory+=25
  turtle.fd(1)
cory=-243
for a1 in range(3):
  mov(-135,cory)
  cory+=25
  turtle.fd(1)
cory=-268
for a1 in range(3):
  mov(105,cory)
  cory+=25
  turtle.fd(1)
cory=-263
for a1 in range(3):
  mov(-105,cory)
  cory+=25
  turtle.fd(1)
cory=-282
for a1 in range(3):
  mov(75,cory)
  cory+=25
  turtle.fd(1)
cory=-280
for a1 in range(3):
  mov(-75,cory)
  cory+=25
  turtle.fd(1)
cory=-291
for a1 in range(3):
  mov(40,cory)
  cory+=25
  turtle.fd(1)
cory=-289
for a1 in range(3):
  mov(-40,cory)
  cory+=25
  turtle.fd(1)
cory=-297
for a1 in range(3):
  mov(0,cory)
  cory+=25
  turtle.fd(1)
#bow
mov(0,-195)
turtle.width(3)
turtle.color("#ff3333")
turtle.begin_fill()
turtle.lt(60)
turtle.fd(40)
turtle.lt(120)
turtle.fd(40)
turtle.lt(120)
turtle.fd(80)
turtle.rt(120)
turtle.fd(40)
turtle.rt(120)
turtle.fd(40)
turtle.end_fill()
mov(0,-195)
turtle.width(3)
turtle.color("black")
turtle.lt(60)
turtle.fd(40)
turtle.lt(120)
turtle.fd(40)
turtle.lt(120)
turtle.fd(80)
turtle.rt(120)
turtle.fd(40)
turtle.rt(120)
turtle.fd(40)
mov(0,-195)
turtle.color("#cca300")
turtle.begin_fill()
turtle.lt(90)
for i in range(60):
  turtle.lt(6)
  turtle.fd(1)
turtle.end_fill()
mov(0,-195)
turtle.color("black")
turtle.lt(90)
for i in range(60):
  turtle.lt(6)
  turtle.fd(1)
#candles
turtle.width(6)
turtle.color("yellow")
mov(125,-55)
turtle.fd(60)
turtle.width(1)
turtle.color("black")
mov(125,5)
turtle.fd(5)
mov(125,10)
turtle.color("#ff9900")
x=12
while x>0:
    turtle.width(x)
    turtle.fd(2)
    x-=2
turtle.color("#ff0066")
turtle.width(6)
mov(-125,-55)
turtle.fd(60)
turtle.width(1)
turtle.color("black")
mov(-125,5)
turtle.fd(5)
mov(-125,10)
turtle.color("#ff9900")
x=12
while x>0:
    turtle.width(x)
    turtle.fd(2)
    x-=2 

#emoji
mov(270,-320)
turtle.width(11)
turtle.speed(100)
turtle.color("yellow")
turtle.begin_fill()
turtle.lt(90)
for x in range(30):
  turtle.fd(15)
  turtle.rt(12)
turtle.end_fill()
turtle.color("dark orange")
mov(270,-320)
turtle.lt(90)
for x in range(30):
  turtle.fd(15)
  turtle.rt(12)
turtle.color("#4d2800")
turtle.width(16)
mov(310,-245)
turtle.fd(1)
turtle.color("yellow")
turtle.width(6)
mov(310,-242)
turtle.fd(1)
turtle.color("#4d2800")
turtle.width(6)
mov(325,-230)
turtle.rt(30)
for x in range(8):
  turtle.rt(6)
  turtle.fd(3)
mov(245,-230)
turtle.rt(90)
for x in range(6):
  turtle.rt(6)
  turtle.fd(4)
turtle.width(9)
mov(245,-245)
turtle.rt(75)
for x in range(10):
  turtle.rt(4)
  turtle.fd(1)
mov(280,-265)
turtle.width(4)
turtle.fd(2)
turtle.rt(80)
for x in range(30):
  turtle.fd(0.8)
  turtle.rt(6)
mov(278,-278)
turtle.rt(90)
for x in range(30):
  turtle.rt(6)
  turtle.fd(0.8)
turtle.color("red")
mov(231,-309)
turtle.begin_fill()
turtle.lt(30)
for x in range(8):
  turtle.fd(5)
  turtle.rt(5)
for x in range(30):
  turtle.rt(6)
  turtle.fd(1.8)
turtle.lt(125)
for x in range(30):
  turtle.fd(1.8)
  turtle.rt(6)
for x in range(8):
  turtle.rt(5)
  turtle.fd(5)
turtle.end_fill()

mov(-264.5,-152.5)
happy.exitonclick()
