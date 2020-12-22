from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    
    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))


    def increase_score(self):
       self.score += 1
       self.clear()
       self.update_score()

    
    def game_over_message(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 18, "normal"))
       


        



   

