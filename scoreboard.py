from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.score = 0
        self.position = position
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(self.position)
        self.write(self.score, align="center", font=("Courier", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
