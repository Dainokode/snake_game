from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=("Arial", 18, "normal"))


    def increase_score(self):
       self.score += 1
       self.update_score()

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

        



   

