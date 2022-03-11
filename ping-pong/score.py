from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()

        self.left_player_score = 0
        self.right_player_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.left_player_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 220)
        self.write(self.right_player_score, align='center', font=('Courier', 50, 'normal'))

    def increment_left_player_score(self):
        self.left_player_score += 1
        self.update_score()

    def increment_right_player_score(self):
        self.right_player_score += 1
        self.update_score()
