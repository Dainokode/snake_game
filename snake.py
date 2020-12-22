from turtle import Turtle


# CONSTANT VARIABLES:

# snake individual parts stored in a list(snake_parts) - start position of each part + headings variables
SNAKE_COORDINATES = [-20, -30, 0]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        # create a new object for each number in range func and add it to snake_parts list
        for snake_index in range(1, 4):
            new_snake_part = Turtle()
            new_snake_part.penup()
            new_snake_part.color("white")
            new_snake_part.shape("square")
            new_snake_part.shapesize(1.5)
            new_snake_part.goto(SNAKE_COORDINATES[snake_index - 1], 0)
            self.snake_parts.append(new_snake_part)

    
    def move(self):
        # for each snake part in the snake_parts list move the last part coordinates to the first and the first part forward by 20px
        for snake_part in range(len(self.snake_parts)- 1, 0, -1):
            new_x = self.snake_parts[snake_part - 1].xcor()
            new_y = self.snake_parts[snake_part - 1].ycor()
            self.snake_parts[snake_part].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)

    
    def add_part(self):
        new_snake_part = Turtle()
        new_snake_part.penup()
        new_snake_part.color("white")
        new_snake_part.shape("square")
        new_snake_part.shapesize(1.5)
        self.snake_parts.append(new_snake_part)


    
    # snake movements
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

