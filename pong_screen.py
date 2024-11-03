from turtle import Turtle,Screen

from  pong_parameters import *

# a = Turtle()



class  My_Screen():
    def __init__(self):
        self.score = [0,0]
       
        self.screen = Screen()
        self.screen.bgcolor(SCREEN_COLOR)
        self.screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
        self.screen.title = "My Pong Game"
        self.screen.tracer(0)
        self.draw_center()
        
        # self.draw_score()
    
        pass
    def draw_score(self):
        tim  = Turtle()
        tim.penup()
        tim.goto(GAME_FIELD_X /2 - 50,GAME_FIELD_Y/2 - 50)
        tim.write(arg=self.draw_score[0])


        pass
    def draw_center(self):
        
        tim = Turtle()
        tim.penup()
        
        start_y =  int((SCREEN_HEIGHT / 2 )- BALL_SIZE)
      
        tim.goto(0,-start_y)
        tim.setheading(90)
      
        step = int(BALL_SIZE/2)
       
        tim.pensize(BALL_SIZE/4)
        tim.color(SCREEN_DOT_LINE_COLOR)
        
       
        while tim.ycor() < SCREEN_HEIGHT / 2 - BALL_SIZE - step :
            tim.pd() 
            tim.forward(BALL_SIZE)
            tim.penup()
            tim.forward(step)
        
        tim.penup()









# def init_tim():
#     tim = Screen()
#     tim.bgcolor('black')
#     tim.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
#     tim.title = "My Pong Game"
#     draw_center()



#     score = [0,0]

#     return tim

# def draw(screen = Screen()):

#     screen.bgcolor('green')
#     screen.delay(15)
#     # draw_center(screen)
#     pass

# def draw_score(self):

#     pass
    