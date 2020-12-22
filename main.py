from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time


# Screen Setup:
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.title("Play Snake")


# init snake object from Snake class
snake = Snake()
food = Food()

# listen for events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

is_game_on = True
while is_game_on:
    # update the screen after snake parts have moved to their positions
    screen.update()
    # snake moves slower
    time.sleep(0.1)
    # call move func from Snake class
    snake.move()
    # detect food collision - change food position
    if snake.head.distance(food) < 15:
        food.refresh_position()


        
screen.exitonclick()