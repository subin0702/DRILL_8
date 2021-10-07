import turtle
import random
import math


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
   #draw_big_point(p1)
   #draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    k = 0.7
    a = 7
    b = 10

    x = (a-b) * math.cos(t) + b * math.cos(t * (k - 1))
    y = (a-b) * math.sin(t) - b * math.sin(t * (k - 1))

    j = (y2-y1)/(x2-x1)
    l = y1 - x1 * a

    for x in range(x1, x2 + 1, 10):
           y = j * x + l
           draw_point((x, y))

    draw_point(p2)

pass



def draw_line(p1, p2):      # 평행한 직선도 그릴 수 있음
    draw_big_point(p1)
    draw_big_point(p2)
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    for i in range(0,100 +1, 2):
        k = 0.7
        a = 7
        b = 10
        t = i / 100         # x,y를 t 파라미터로 표현
        x = (a - b) * math.cos(t) + b * math.cos(t * (k - 1))
        y = (a - b) * math.sin(t) - b * math.sin(t * (k - 1))
        #x = (1-t)*x1 + t*x2
        #y = (1-t)*y1 + t*y2

        draw_point(x,y)

    draw_point(x1,y1)
    pass


prepare_turtle_canvas()

# draw_line_basic((-100, 50), (100, 50))
draw_line((100,300),(200,50))

turtle.done()