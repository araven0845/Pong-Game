from turtle import Screen, Turtle
import time
from ball import Ball
from scoreboard import Scoreboard
from paddles import Paddle

# --- Setup the game screen ---
screen = Screen()
screen.setup(width=1200, height=900)
screen.bgcolor("black")
screen.title("Arjun's Pong Game")
screen.tracer(0)  # Turn off animation for manual screen updates

# --- Draw the midline ---
midline = Turtle()
midline.penup()
midline.goto(0, 450)
midline.setheading(270)
midline.color("white")
for num in range(60):
    if num % 2 == 1:  # Alternate between pen up and down for dashed line
        midline.penup()
    else:
        midline.pendown()
    midline.forward(15)
midline.hideturtle()

# --- Initialize game components ---
scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle((525, 0))  # Right paddle at the right edge
l_paddle = Paddle((-525, 0))  # Left paddle at the left edge

# --- Key bindings for paddle movement ---
screen.listen()
screen.onkey(r_paddle.up, 'Up')      # Move right paddle up
screen.onkey(r_paddle.down, 'Down')  # Move right paddle down
screen.onkey(l_paddle.up, 'w')       # Move left paddle up
screen.onkey(l_paddle.down, 's')     # Move left paddle down

# --- Game loop ---
game_on = True
while game_on:
    time.sleep(0.01)  # Pause briefly to control ball speed
    screen.update()   # Refresh the screen
    ball.move()       # Move the ball

    # --- Detect collision with top and bottom walls ---
    if ball.ycor() > 420 or ball.ycor() < -420:
        ball.bounce_y()

    # --- Detect collision with paddles ---
    elif (ball.distance(r_paddle) < 75 and ball.xcor() > 495) or (ball.distance(l_paddle) < 75 and ball.xcor() < -495):
        ball.bounce_x()

    # --- Detect ball out of bounds on the right ---
    elif ball.xcor() > 580:
        ball.reset()
        scoreboard.l_point()  # Left player scores a point

    # --- Detect ball out of bounds on the left ---
    elif ball.xcor() < -580:
        ball.reset()
        scoreboard.r_point()  # Right player scores a point

# --- Close the game window on click ---
screen.exitonclick()
