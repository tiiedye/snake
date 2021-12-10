from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
