
import turtle
import time
import random

delay = 0.1

#scores
score = 0
high_score = 0

#set up screen
snake = turtle.Screen()
snake.title("Snake Game")
snake.bgcolor('light pink')
snake.setup(width=600, height=600)
snake.tracer(0)

#snake head
snake2= turtle.Turtle()
snake2.speed(0)
snake2.shape("square")
snake2.color("red")
snake2.penup()
snake2.goto(0,0)
snake2.direction = "stop"

#snake food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []


#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 24, "normal"))



#Functions
def goup():
    if snake2.direction != "down":
        snake2.direction = "up"
def godown():
    if snake2.direction != "up":
        snake2.direction = "down"
def goleft():
    if snake2.direction != "right":
        snake2.direction = "left"
def goright():
    if snake2.direction != "left":
        snake2.direction = "right"
def move():
    if snake2.direction == "up":
        y = snake2.ycor()
        snake2.sety(y+20)
    if snake2.direction == "down":
        y =snake2.ycor()
        snake2.sety(y-20)
    if snake2.direction == "left":
        x = snake2.xcor()
        snake2.setx(x-20)
    if snake2.direction == "right":
        x = snake2.xcor()
        snake2.setx(x+20)

#keyboard bindings
snake.listen()
snake.onkeypress(goup, "Up")
snake.onkeypress(godown, "Down")
snake.onkeypress(goleft, "Left")
snake.onkeypress(goright, "Right")

while True:
    snake.update()
      
    #collision with border area
    if snake2.xcor()>290 or snake2.xcor()<-290 or snake2.ycor()>290 or snake2.ycor()<-290:
        time.sleep(1)
        snake2.goto(0,0)
        snake2.direction = "stop"

        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()

        #reset score
        score = 0

        #reset delay
        delay = 0.2

        sc.clear()
        sc.write("score:{} High score:{}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))



    #check collision with food
    if snake2.distance(food) <20:
        # move the food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001
        
        #increase the score
        score += 5

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

    #move segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to head
    if len(segments)>0:
        x =snake2.xcor()
        y = snake2.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(snake2)<20:
            time.sleep(1)
            snake2.goto(0,0)
            snake2.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1


            #updating score     
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
snake.mainloop()



    



    
    


  
    
    
    



      
    



    
    



    
    
        
        
    
