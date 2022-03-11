from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        # creating paddle
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)

        # moving the paddle to right corner
        self.penup()
        self.goto(x_pos, y_pos)

    def go_up(self):
        y_cor = self.ycor() + 20
        print(f"go up {y_cor}")
        self.goto(self.xcor(), y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        print(f"go down {y_cor}")
        self.goto(self.xcor(), y_cor)
