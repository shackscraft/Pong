import turtle
import sys
import winsound
import pygame

class Menu():   
    def __init__(self):
        #Main Screen
        mn = turtle.Screen()
        mn.title("Pantalla de menu")
        mn.bgcolor("black")
        mn.setup(width=950, height=750)
        mn.tracer(0)

        #margin
        pon = turtle.Turtle()
        pon.speed(0)
        pon.hideturtle()
        pon.penup()
        pon.color("white")
        pon.goto(400,300)
        pon.pendown()
        
        for n in range(10):            
            pon.right(40)         
            pon.forward(90)
            pon.left(40)
            pon.forward(-70)

        pon.right(90)
        for n in range(13):
            pon.right(40)         
            pon.forward(90)
            pon.left(40)
            pon.forward(-70)
        
        pon.left(90)
        for n in range(10):
            pon.right(40)         
            pon.forward(-90)
            pon.left(40)
            pon.forward(70)
        
        pon.right(90)
        for n in range(13):
            pon.right(40)         
            pon.forward(-90)
            pon.left(40)
            pon.forward(70)

        #as the variable says, its the title XD
        title = turtle.Turtle()
        title.hideturtle()
        title.speed(0)
        title.penup()
        title.color("white")
        title.goto(0,120)
        title.write("PONG", align = "center", font = ("Arial", 100, "bold"))

        #start selection
        estr = turtle.Turtle()
        estr.hideturtle()
        estr.speed(0)
        estr.penup()
        estr.color("Red")
        estr.goto(0,-30)
        estr.write("Start", align = "center", font = ("calibri", 45, "normal"))

        #exit selection
        ext = turtle.Turtle()
        ext.hideturtle()
        ext.speed(0)
        ext.penup()
        ext.color("white")
        ext.goto(0,-160)
        ext.write("Exit", align = "center", font = ("calibri", 45, "normal"))

        #select arrow
        slct = turtle.Turtle()
        slct.penup()
        slct.speed(0)
        slct.color("white")
        slct.shape("triangle")
        slct.shapesize(2)
        slct.goto(-130, 5)

        #move select arrow code
        def slct_up():
            slct.goto(-130,5)
            estr.clear()
            ext.clear()
            estr.color("red")
            estr.write("Start", align = "center", font = ("calibri", 45, "normal")) 
            ext.color("White")
            ext.write("Exit", align = "center", font = ("calibri", 45, "normal"))
       
        def slct_down():
            slct.goto(-130,-125)
            estr.clear()
            ext.clear()
            estr.color("White")
            estr.write("Start", align = "center", font = ("calibri", 45, "normal"))
            ext.color("red")
            ext.write("Exit", align = "center", font = ("calibri", 45, "normal"))
            

        def slct_pressed():
            if slct.ycor() == 5:
                Game = 1
                mn.clear()
                #Want your Main menu be normal just erase From here
                mn.title("Pong Pro :v")
                mn.bgcolor("black")
                mn.setup(width=800, height=600)
                mn.tracer(0)
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
                    mn.listen()
                    mn.onkeypress(paddle_a_up, "w")
                    mn.onkeypress(paddle_a_down, "s")
                    mn.onkeypress(paddle_b_up, "Up")
                    mn.onkeypress(paddle_b_down, "Down")

                                    #Main Game Loop
                    while True:
                        mn.update()
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
                            mn.clear()
                            mn.bgcolor("black")
                            pen.goto(0,60)
                            pen.write("PLAYER A WINS",align="center", font=("Courier", 54, "normal"))
                            pygame.time.wait(8000)
                            mn.clear()
                            Menu()

                        #player win 
                        if point_b > 4:
                            mn.clear()
                            mn.bgcolor("black")
                            pen.goto(0,60)
                            pen.write("PLAYER B WINS",align="center", font=("Courier", 54, "normal"))
                            pygame.time.wait(8000)
                            mn.clear()
                            Menu()
                #To here
            elif slct.ycor() == -125:
                mn.bye()
                
        #listen keyboard
        mn.listen()
        mn.onkeypress(slct_up, "w")
        mn.onkeypress(slct_up, "Up")
        mn.onkeypress(slct_down, "s")
        mn.onkeypress(slct_down, "Down")
        mn.onkeypress(slct_pressed, "space")

        while True:
            mn.update()

Menu()
