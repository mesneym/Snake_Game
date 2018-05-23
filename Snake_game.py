import turtle
import random
import time
import math

##############################################
#            BOARD
##############################################
HEIGHT=WIDTH=600
STP =20 # STEP SIZE
BD_H=HEIGHT/2-STP #BOARD HEIGHT
BD_W=BD_SW=WIDTH/2-STP #BOARD WIDTH
BD_SH=HEIGHT/2-2*STP

window=turtle.Screen()
window.title("snake game")
window.bgcolor("yellow")
window.setup(WIDTH,HEIGHT)

#############################################
#            SNAKE
#############################################
class Snake(turtle.Turtle):
    def __init__(self):
        super(Snake,self).__init__()
        self.dir_x=-1
        self.dir_y=0
        self.coordinates=[(0,0),(0,20),(0,40)]  

    def UpdateDirection(self,new_x,new_y):
       self.dir_x = new_x
       self.dir_y = new_y
        
    def move(self):
        self.clearstamps(len(self.coordinates))
        if (len(self.coordinates)>1):
            for i in range(len(self.coordinates)-1,0,-1):
               self.coordinates[i]=self.coordinates[i-1]      
               self.goto(self.coordinates[i][0],self.coordinates[i][1])
               self.stamp()
        
        if(self.coordinates[0][0]>(BD_SW)):
            self.coordinates[0] =(-1*BD_SW, self.coordinates[0][1]+STP*self.dir_y)
        if(self.coordinates[0][0]<(-1*BD_SW)):
            self.coordinates[0] =(1*BD_SW, self.coordinates[0][1]+STP*self.dir_y)
        if(self.coordinates[0][1]>(BD_H)):
            self.coordinates[0] =(self.coordinates[0][0]+STP*self.dir_x, -1*BD_H)
        if(self.coordinates[0][1]<(-1*BD_H)):
            self.coordinates[0] =(self.coordinates[0][0]+STP*self.dir_x,BD_H)
        else:
            self.coordinates[0] =(self.coordinates[0][0]+STP*self.dir_x, self.coordinates[0][1]+STP*self.dir_y)
        self.goto(self.coordinates[0][0],self.coordinates[0][1])
        self.stamp()
    
    def collision(self):
        return (len(set(self.coordinates))<len(self.coordinates))

    def grow(self):
        self.coordinates.append(self.coordinates[len(self.coordinates)-1]) 
        

############################################
#           CREATING OBJECT
############################################
#------------------------------------------
#              SCORE 
#-----------------------------------------
scoreT=turtle.Turtle()
scoreT.penup()
scoreT.hideturtle()
scoreT.setposition(-1*BD_W,BD_W)

#------------------------------------------
#              FOOD 
#------------------------------------------
food=turtle.Turtle()
food.color("red")
food.penup()
food.shape("square")
food.setposition(random.randint(-1*BD_SH/STP,BD_SH/STP)*STP,random.randint(-1*BD_SW/STP,BD_SW/STP)*STP)
#-------------------------------------------
#              SNAKE
#-------------------------------------------
snk=Snake()
snk.color("blue")
snk.shape("square")
snk.penup()

###########################################
#             G-METHODS
###########################################
def Right():
    snk.UpdateDirection(1, 0)
def Left():
    snk.UpdateDirection(-1, 0)
def Up():  
    snk.UpdateDirection(0, 1)
def Down():
    snk.UpdateDirection(0, -1)

def hit():
    distance=math.sqrt(math.pow(snk.xcor()-food.xcor(),2)+math.pow(snk.ycor()-food.ycor(),2))
    return distance<20

############################################
#            DRIVER
############################################
if __name__=='__main__':
    window.listen()
    window.onkey(Left,"Left")
    window.onkey(Up,"Up")
    window.onkey(Down,"Down")
    window.onkey(Right,"Right")

    score=0
    while True:
        window.tracer(0)
        if(hit()):
            score+=1
            snk.grow()
            food.setposition(random.randint(-1*BD_SH/STP,BD_SH/STP)*STP,random.randint(-1*BD_SW/STP,BD_SW/STP)*STP)
            scoreT.undo()
            scoreT.setposition(-1*BD_W,BD_H)
            scorestring="Score: %s" %score
            scoreT.write(scorestring,False,align="Left",font=("Arial",14,"normal"))
        snk.move()
        if(snk.collision()):
            scoreT.undo()
            scoreT.penup()
            scoreT.setposition(-300,280)
            scorestring="Score: " +str(score) + " GAMEOVER"
            scoreT.write(scorestring,False,align="Left",font=("Arial",14,"normal"))
            break
        time.sleep(0.09)
        window.tracer(1)
    turtle.mainloop()
        





