from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.color("white")
        self.write(self.lscore, False, "center", ("Courier", 80, "normal"))

    def scorer(self):
        self.rscore= self.rscore+1
        self.clear()
        self.write(self.rscore, False, "center", ("Courier", 80, "normal"))

    def scorel(self):
        self.lscore= self.lscore+1
        self.clear()
        self.write(self.lscore, False, "center", ("Courier", 80, "normal"))
