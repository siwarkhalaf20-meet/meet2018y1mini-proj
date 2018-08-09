# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random #We'll need this later in the lab




SIZE_X=1000
SIZE_Y=1000
GAME_WINDOW_SIZE_X = 600
GAME_WINDOW_SIZE_Y = 600
turtle.setup(SIZE_X, SIZE_Y)

turtle.tracer(1,0) #This helps the turtle move more smoothly

 #Curious? It's the turtle window               #size. 

SQUARE_SIZE = 20
START_LENGTH = 6

turtle.write("snake game!!", align="center", font=("Arial",60))

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

turtle.penup()
turtle.goto(-GAME_WINDOW_SIZE_X /2,0)
turtle.pendown()
turtle.pencolor("blue")
turtle.goto(-GAME_WINDOW_SIZE_X/2,-GAME_WINDOW_SIZE_Y/2)
turtle.goto(GAME_WINDOW_SIZE_X/2,-GAME_WINDOW_SIZE_Y/2)
turtle.goto(GAME_WINDOW_SIZE_X/2,GAME_WINDOW_SIZE_Y/2)
turtle.goto(0,GAME_WINDOW_SIZE_Y/2)
turtle.goto(-GAME_WINDOW_SIZE_X/2,GAME_WINDOW_SIZE_Y/2)
turtle.goto(-GAME_WINDOW_SIZE_X/2,0)
turtle.penup()

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")
snake.color("yellow")


turtle.register_shape("trash.gif")

food = turtle.clone()
food.shape("trash.gif")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for pieces in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 
    
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 
    
    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
    
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 
    
    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    snake_stamp1 = snake.stamp()
    stamp_list.append(snake_stamp1)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 250 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, UP_ARROW) # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    print("You pressed the LEFT key!")
turtle.onkeypress(left, LEFT_ARROW)

def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    print("You pressed the DOWN key!")
turtle.onkeypress(down, DOWN_ARROW)
    
def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    print("You pressed the RIGHT key!")
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()
    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    turtle.ontimer(move_snake,TIME_STEP)
    
    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    elif direction==UP:
        snake.goto(x_pos,y_pos + SQUARE_SIZE)
        print("You moved up!")

    elif direction==DOWN:
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print("You moved down!")

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
    
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    #piece of the tail
    

    if len(food_stamps) <= 6:
        make_food()
    
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(GAME_WINDOW_SIZE_X/2/2/SQUARE_SIZE)+1
    max_x=int(GAME_WINDOW_SIZE_X/2/2/SQUARE_SIZE)-1
    min_y=-int(GAME_WINDOW_SIZE_Y/2/2/SQUARE_SIZE)-1
    max_y=int(GAME_WINDOW_SIZE_Y/2/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##position
    food.goto(food_x,food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append(food.pos())
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food_stamps.append(food.stamp())
    


food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    
    food_stamps.append(food.stamp())
    ####WRITE YOUR CODE HERE!!


move_snake()

