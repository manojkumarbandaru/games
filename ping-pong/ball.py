from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.x_cor_move = 10
        self.y_cor_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_cor_move
        y_cor = self.ycor() + self.y_cor_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_cor_move *= -1

    def bounce_x(self):
        self.x_cor_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        # for moving the ball to opposite direction
        self.bounce_x()
