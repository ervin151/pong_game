from random import randint,random
from turtle import Turtle
from paddle import Paddle
import math

from pong_parameters  import *

class Ball(Turtle):
    def __init__(self) -> None:       
        super().__init__()
        self = Turtle(BALL_SHAPE)
        self.commnet = "JOpa Comment"
        self.vector = [0,0]
        self.color(BALL_COLOR)
        self.penup()
        x = randint(int(-GAME_FIELD_X/2), int(GAME_FIELD_X/2))
        y = randint(int(-GAME_FIELD_Y/2), int(GAME_FIELD_Y/2))
        self.goto(x,y)
        self.vector[0] = randint(50,100)*BALL_SPEED/100
        self.vector[1] = math.sqrt(BALL_SPEED**2 - self.vector[0]**2)
        pass
    
    # def set_ball(self):
    
    def print_comment(self):
        return self.commnet
    def move(self,paddle_l,paddle_r):
        # paddle_l = paddle1.
        # paddle_r = 

        old_x = self.xcor()
        old_y = self.ycor()

        if old_x >= GAME_FIELD_X - BALL_SIZE :
            if self.distance(paddle_r) > 50:

                self.vector[0] *= -1
                self.bounce()

                pass
            else:
                # Right Player missed the ball
                pass
            

            pass

        elif old_x <= -GAME_FIELD_X + BALL_SIZE:
            if self.distance(paddle_l) > 50 :
                self.vector[0] *= -1
                self.bounce()


            pass

        elif not -GAME_FIELD_Y <= old_y <= GAME_FIELD_Y:
            self.vector[1] *= -1
            pass

        self.bounce()   

        pass

    def bounce(self):
        
        old_x = self.xcor()
        old_y = self.ycor()
        new_x = old_x + self.vector[0]
        new_y = old_y + self.vector[1]
        self.goto(x=new_x,y=new_y)