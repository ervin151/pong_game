from turtle import Turtle
from pong_parameters import *

class Paddle(Turtle):
    def __init__(self,left_or_right = 'right'):
        super().__init__()

        # self = Turtle(PADDLE_SHAPE)
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=PADDLE_LENGTH,stretch_len=1)
        self.color(PADDLE_COLOR)

        x_pos = GAME_FIELD_X
        if left_or_right == 'left' : 
            x_pos = - x_pos
        y_pos = 0

        self.goto(x_pos,y_pos)
        pass
        # self = []
        # self.direction = 1

     
        # for _ in range(PADDLE_LENGTH):
            
        #     tim = Turtle(PADDLE_SHAPE) 
        #     tim.color(PADDLE_COLOR)
        #     tim.penup()
        #     tim.goto(x=x_pos,y=y_pos)
        #     tim.setheading(90)
            
        #     y_pos += PADDLE_SIZE
        #     self.append(tim)
        
    def move_up(self): 
        new_y = self.ycor() + BALL_SIZE             
        self.goto(self.xcor(),new_y)
        self.direction = 1
       
    def move_down(self): 
        new_y = self.ycor() - BALL_SIZE              
        self.goto(self.xcor(),new_y)
        self.direction = -1

        # segment.forward(BALL_SPEED)
        # self.move()
    
    # def move_down(self):
    #     for segment in self:
    #         segment.setheading(270)
    #         self.direction = -1
    #         segment.forward(BALL_SPEED)
    #     self.move()
   
    
    # def move(self):
    #     if self[-1].ycor() < GAME_FIELD_Y and self[0].ycor() > - (GAME_FIELD_Y) :
 
    #           for segment in self:
    #             segment.forward(BALL_SPEED)
    #     else :
    #         for segment in self:
    #             segment.setheading(segment.heading() + 180)
    #             segment.forward(BALL_SPEED)
    #         self.direction *= -1
    #         pass
        