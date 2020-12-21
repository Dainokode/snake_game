from turtle import Turtle, Screen
import time


# Screen Setup:
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.title("Play Snake")


# snake individual parts stored in a list - start position of each part
snake_parts = []
snake_parts_coordinates = [-20, -30, 0]


# create a new object for each number in range func and add it to snake_parts list
for snake_index in range(1, 4):
    new_snake_part = Turtle()
    new_snake_part.penup()
    new_snake_part.color("white")
    new_snake_part.shape("square")
    new_snake_part.shapesize(1.5)
    snake_parts.append(new_snake_part)


# each snake part gets moved to a random coordinate chosen from snake_parts_coordinates and correctly positioned in the middle of the screen
for snake_part in range(len(snake_parts)):
    snake_parts[snake_part].goto(snake_parts_coordinates[snake_part], 0)


is_game_on = True
while is_game_on:
    # update the screen after snake parts have moved to their positions
    screen.update()
    # snake moves slower
    time.sleep(0.1)
    # for each snake part in the snake_parts list move the last part coordinates to the first and the first part forward by 20px
    for snake_part in range(len(snake_parts)- 1, 0, -1):
        new_x = snake_parts[snake_part - 1].xcor()
        new_y = snake_parts[snake_part - 1].ycor()
        snake_parts[snake_part].goto(new_x, new_y)
    snake_parts[0].forward(20)

        


screen.exitonclick()