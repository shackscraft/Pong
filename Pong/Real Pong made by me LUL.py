import turtle
import winsound
import sys
wn = turtle.Screen()
wn.title("Pong Pro :v")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Points
point_a = 0
point_b = 0
PRound = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")

while point_a or point_b < 6: 
    pen.write("round 1 of PONG",align="center", font=("Courier", 24, "normal"))
    
    #scenario
    scenenario = turtle.Turtle()
    scenenario.hideturtle()
    scenenario.penup()
    scenenario.speed(0)
    scenenario.color("white")
    scenenario.goto(400,300)
    scenenario.pendown()
    scenenario.goto(400,-300)
    scenenario.pendown()
    scenenario.goto(-400,-300)
    scenenario.pendown()
    scenenario.goto(-400,300)
    scenenario.pendown()
    scenenario.goto(400,300)
    scenenario.penup()

    #paddle A 
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=9, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    #Paddle B 
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=9, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    #Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.280
    ball.dy = 0.280

    #Pen
    
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player A: {}   Player B: {}".format(point_a, point_b),align="center", font=("Courier", 24, "normal"))

    #Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 70
        paddle_a.sety(y)
    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 70
        paddle_a.sety(y)
    def paddle_b_up():
        y = paddle_b.ycor()
        y += 70
        paddle_b.sety(y)
    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 70
        paddle_b.sety(y)

    #Keyboard biding
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    #Main Game Loop
    while True:
        wn.update()
        #PADDLE LIMITS
        if paddle_a.ycor() > 205:
            paddle_a.goto(-350, 205)
        if paddle_a.ycor() < -205:
            paddle_a.goto(-350, -205)
        if paddle_b.ycor() > 205:
            paddle_b.goto(350, 205)
        if paddle_b.ycor() < -205:
            paddle_b.goto(350, -205)

        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Border Checking 
        if ball.ycor() > 289:
            ball.sety(289)
            ball.dy *= -1
            
        if ball.ycor() < -289:
            ball.sety(-289)
            ball.dy *= -1
            
        if ball.xcor() > 385:
            ball.goto(0,0)
            ball.dx = 0.280
            ball.dy = 0.280
            ball.dx *= -1.15
            point_a += 1
            pen.clear()
            pen.goto(0,260)
            pen.write("Player A: {}   Player B: {}".format(point_a, point_b),align="center", font=("Courier", 24, "normal"))
            pen.goto(0,0)
            PRound = point_a + point_b + 1
            pen.write("round {} of PONG".format(PRound),align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("ara ma ma.wav", winsound.SND_ASYNC)
            
        if ball.xcor() < -385:
            ball.goto(0,0)
            ball.dx = -0.280
            ball.dy = -0.280
            ball.dx *= -1.15
            point_b += 1
            pen.clear()
            pen.goto(0,260)
            pen.write("Player A: {}   Player B: {}".format(point_a, point_b),align="center", font=("Courier", 24, "normal"))
            pen.goto(0,0)
            PRound = point_a + point_b + 1
            pen.write("round {} of PONG".format(PRound),align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("ara ma ma.wav", winsound.SND_ASYNC)
        
        #paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 95 and ball.ycor() > paddle_b.ycor() -95):
            ball.setx(340)
            ball.dx *= -1.06
            winsound.PlaySound("ara.wav", winsound.SND_ASYNC)
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 95 and ball.ycor() > paddle_a.ycor() -95):
            ball.setx(-340)
            ball.dx *= -1.06
            winsound.PlaySound("ara.wav", winsound.SND_ASYNC)
        
        #player win 
        if point_a > 4:
            pen.goto(0,60)
            pen.write("PLAYER A WINS",align="center", font=("Courier", 54, "normal"))
            PA = wn.numinput("player A WINS", "type 1 if you want to play again, type 2 if you don't and click to leave",1,1,2)
            if PA == 1:
                point_a = 0
                point_b = 0
                PRound = 0
                pen.clear()
                pen.goto(0,260)
                pen.write("Player A: {}   Player B: {}".format(point_a, point_b),align="center", font=("Courier", 24, "normal"))
                pen.goto(0,0)
                PRound = point_a + point_b + 1
                pen.write("round {} of PONG".format(PRound),align="center", font=("Courier", 24, "normal"))
                wn.listen()
            if PA == 2: 
                point_a = 0
                point_b = 0
                wn.resetscreen()
                pen.goto(0,0)
                pen.speed(0)
                pen.color("white")
                pen.write("PLAYER A WINS CLICK TO LEAVE",align="center", font=("Courier", 34, "normal"))
                wn.exitonclick()
        #player win 
        if point_b > 4:
            pen.goto(0,60)
            pen.write("PLAYER B WINS",align="center", font=("Courier", 34, "normal"))
            PA = wn.numinput("player B WINS", "type 1 if you want to play again, type 2 if you don't and click to leave",1,1,2)
            if PA == 1:
                point_a = 0
                point_b = 0
                PRound = 0
                pen.clear()
                pen.goto(0,260)
                pen.write("Player A: {}   Player B: {}".format(point_a, point_b),align="center", font=("Courier", 24, "normal"))
                PRound = point_a + point_b + 1
                pen.goto(0,0)
                pen.write("round {} of PONG".format(PRound),align="center", font=("Courier", 24, "normal"))
                wn.listen()
            if PA == 2: 
                point_a = 0
                point_b = 0
                wn.resetscreen()
                pen.goto(0,0)
                pen.speed(0)
                pen.color("white")
                pen.write("PLAYER B WINS CLICK TO LEAVE",align="center", font=("Courier", 34, "normal"))
                wn.exitonclick()