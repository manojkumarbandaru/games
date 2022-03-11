from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_BOARD_POSITION = (-200, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_score_on_screen()

    def update_score_on_screen(self):
        self.clear()
        self.goto(SCORE_BOARD_POSITION)
        self.write(f"Score:{self.score}", align='center', font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score_on_screen()
