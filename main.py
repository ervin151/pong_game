from turtle import Turtle,Screen
from pong_screen import My_Screen
from pong_screen import *
from paddle import Paddle
from ball import Ball
import score
import time



pong_screen = Screen()
pong_screen.bgcolor(SCREEN_COLOR)
pong_screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
pong_screen.title = "My Pong Game"

pong_screen.tracer(0)



def GameOver():
    global game
    game = False
game = True

left_paddle = Paddle('left')
right_paddle = Paddle('right')


pong_screen.listen()

pong_screen.onkeypress(fun=left_paddle.move_up,key='w')
pong_screen.onkeypress(fun=left_paddle.move_down,key='s')
pong_screen.onkeypress(fun=right_paddle.move_up,key='Up')
pong_screen.onkeypress(fun=right_paddle.move_down,key='Down')
pong_screen.onkeypress(fun=GameOver,key='space')


ball : Ball = Ball()
# ball.vector = [0,0]

print(ball.print_comment())

game = True
# print(ball.__dict__)

print(ball.vector)
while game :
    pong_screen.update()
    # ball.move(paddle_l=left_paddle,paddle_r=right_paddle)
    # time.sleep(0.1)

    pass
#

pong_screen.screen.exitonclick()
