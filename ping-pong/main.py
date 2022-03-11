from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from time import sleep

# creating screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
# for turning off animation. when tracer is off, screen needs to be updated manually
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()

# for listening to the events on screen
screen.listen()
# for binding key events
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # for detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # for detecting collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -310):
        ball.bounce_x()

    # for detecting ball not colliding with right paddle
    if ball.xcor() > 380:
        score.increment_left_player_score()
        ball.reset_position()

    # for detecting ball not colliding with left paddle
    if ball.xcor() < -380:
        score.increment_right_player_score()
        ball.reset_position()

screen.exitonclick()
